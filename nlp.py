from google.cloud import language_v1


def classify_email(text):

    client = language_v1.LanguageServiceClient()


    document = language_v1.Document(
        content=text,
        type_=language_v1.Document.Type.PLAIN_TEXT
    )


    response = client.classify_text(
        request={
            "document": document
        }
    )


    categories = response.categories


    if len(categories)==0:
        return "Unknown"


    return categories[0].name
