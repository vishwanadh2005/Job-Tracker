from google_auth_oauthlib.flow import Flow


SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]


def authenticate():

    flow = Flow.from_client_secrets_file(
        "credentials.json",
        scopes=SCOPES
    )


    flow.run_local_server(
        port=8080
    )


    credentials = flow.credentials


    with open(
        "token.json",
        "w"
    ) as file:

        file.write(
            credentials.to_json()
        )
