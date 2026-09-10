import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime


# ============================================================
# USER INPUT
# ============================================================

company_name = input("Enter company name: ")
company_location = input("Enter company location: ")


# ============================================================
# TEMPORARY GREENHOUSE INPUT
# ============================================================

greenhouse_board_token = input(
    "Enter Greenhouse board token: "
)


# ============================================================
# GET JOBS
# ============================================================

def get_greenhouse_jobs(board_token):

    url = (
        f"https://boards-api.greenhouse.io/v1/boards/"
        f"{board_token}/jobs"
    )

    params = {
        "content": "true"
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    return response.json().get("jobs", [])


# ============================================================
# CLEAN HTML
# ============================================================

def clean_html(html):

    if not html:
        return ""

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    return soup.get_text(
        separator="\n",
        strip=True
    )


# ============================================================
# EXTRACT JOBS
# ============================================================

def extract_jobs(raw_jobs):

    jobs = []

    for job in raw_jobs:

        location = job.get(
            "location",
            {}
        )

        departments = job.get(
            "departments",
            []
        )

        offices = job.get(
            "offices",
            []
        )

        jobs.append({

            "company": company_name,

            "company_location": company_location,

            "job_id": job.get("id"),

            "job_title": job.get("title"),

            "job_location": location.get(
                "name",
                ""
            ),

            "department": ", ".join(
                d.get("name", "")
                for d in departments
            ),

            "office": ", ".join(
                o.get("name", "")
                for o in offices
            ),

            "updated_at": job.get(
                "updated_at"
            ),

            "job_url": job.get(
                "absolute_url"
            ),

            "description": clean_html(
                job.get("content", "")
            ),

            "source": "Greenhouse",

            "scraped_at": datetime.now().isoformat()

        })

    return jobs


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 60)
    print("JOB FINDER")
    print("=" * 60)

    print(
        f"Company  : {company_name}"
    )

    print(
        f"Location : {company_location}"
    )

    print()
    print("Searching...")

    try:

        raw_jobs = get_greenhouse_jobs(
            greenhouse_board_token
        )

        jobs = extract_jobs(
            raw_jobs
        )

        df = pd.DataFrame(jobs)

        print()
        print("=" * 60)
        print(f"Found {len(df)} jobs")
        print("=" * 60)

        if not df.empty:

            print(
                df[
                    [
                        "job_title",
                        "job_location",
                        "department",
                        "job_url"
                    ]
                ].to_string(index=False)
            )

        else:

            print("No jobs found.")

    except Exception as e:

        print()
        print("ERROR:")
        print(e)


if __name__ == "__main__":
    main()