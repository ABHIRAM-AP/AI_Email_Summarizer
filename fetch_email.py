from imapclient import IMAPClient
import os
from dotenv import load_dotenv


load_dotenv()

EMAIL = os.getenv("EMAIL_ID")
PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = "imap.gmail.com"

def fetch_unread_emails():
    emails = []
    try:
        with IMAPClient(IMAP_SERVER, ssl=True) as client:
            client.login(EMAIL, PASSWORD)
            client.select_folder('INBOX')

            messages = client.search(["UNSEEN"])
            print(f"Found {len(messages)} unread emails")

            if not messages:
                return []

            # Batch fetch all at once
            fetch_data = client.fetch(messages, ["ENVELOPE", "BODY[TEXT]"])

            for uid, data in fetch_data.items():
                try:
                    envelope = data[b'ENVELOPE']
                    subject = envelope.subject.decode() if envelope.subject else "No Subject"
                    body = data[b"BODY[TEXT]"].decode("utf-8", errors="ignore")

                    sender = envelope.from_[0]
                    sender_email = f"{sender.mailbox.decode()}@{sender.host.decode()}"

                    emails.append({
                        "sender":sender_email,
                        "uid": uid,
                        "subject": subject,
                        "body": body[:2000]  
                    })

                except Exception as e:
                    print(f"Error parsing UID {uid}: {e}")

    except Exception as e:
        print(f"Error connecting to server: {e}")

    return emails



