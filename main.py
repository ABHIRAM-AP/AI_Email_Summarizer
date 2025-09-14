from fetch_email import fetch_unread_emails
from email_summarizer import summarize_email
from telegram_send import send_summary_to_telegram

if __name__ == "__main__":
    unread_emails = fetch_unread_emails()
    
    if not unread_emails:
        send_summary_to_telegram("No unread emails.")
        print("No unread emails.")

    else:
        for i, mail in enumerate(unread_emails, 1):
            summary = summarize_email(mail['body'])

            final_summarized_msg = f"{mail['subject']}\nFrom: {mail['sender']}\n\n{summary}"
            send_summary_to_telegram(final_summarized_msg)

            print(f"\nEmail {i}")
            print(f"   Subject: {mail['subject']}")
            print(f"   AI Summary: {summary}")
