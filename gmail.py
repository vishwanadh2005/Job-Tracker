from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]


def get_service():

    creds = Credentials.from_authorized_user_file(
        "token.json",
        SCOPES
    )

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    return service



def get_job_emails():

    service = get_service()


    response = service.users().messages().list(
        userId="me",
        q="job OR interview OR application"
    ).execute()


    messages = response.get(
        "messages",
        []
    )


    emails = []


    for msg in messages[:20]:

        data = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()


        headers = data["payload"]["headers"]


        subject = ""
        sender = ""


        for h in headers:

            if h["name"] == "Subject":
                subject = h["value"]

            if h["name"] == "From":
                sender = h["value"]


        emails.append(
            {
                "sender": sender,
                "subject": subject,
                "content": subject
            }
        )


    return emails
