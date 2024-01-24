from azure.communication.email import EmailClient
from schemas.address import Recipients
import os


def send_mail(recipients: Recipients, subject: str, content: str):
    try:
        connection_string = os.environ.get("connection_communication_services")
        client = EmailClient.from_connection_string(connection_string)
        message = {
            "senderAddress": "DoNotReply@9166101c-80c3-42b4-9977-2d1950c42921.azurecomm.net",
            "recipients": recipients.model_dump(),
            "content": {
                "subject": subject,
                "plainText": content,
            }
        }

        poller = client.begin_send(message)
        result = poller.result()
        return result
    except Exception:
        print("It could not send email")
