pip install fastapi uvicorn google-auth google-auth-oauthlib google-api-python-client sqlalchemy psycopg2-binary python-dotenv

from fastapi import FastAPI
from gmail import get_job_emails
from nlp import classify_email

app = FastAPI(
    title="Job Application Intelligence Platform"
)


@app.get("/")
def home():
    return {
        "message": "Job Application Tracker API"
    }


@app.get("/applications")
def applications():

    emails = get_job_emails()

    results = []

    for email in emails:

        category = classify_email(
            email["content"]
        )

        results.append(
            {
                "company": email["sender"],
                "subject": email["subject"],
                "category": category
            }
        )

    return results
