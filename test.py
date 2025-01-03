from client import AgentMail
from time import sleep

BASE_URL = "https://api.agentmail.dev"
USERNAME = "test"
DOMAIN = "agentmail.dev"


def main():
    client = AgentMail(BASE_URL)

    status = client.delete_inbox(f"{USERNAME}@{DOMAIN}")
    print(status, "\n")

    inbox = client.create_inbox(username=USERNAME, domain=DOMAIN)
    print(inbox, "\n")

    sleep(3)

    emails = client.get_emails(inbox.address)
    print(emails, "\n")

    email = client.get_email(inbox.address, emails.emails[0].id)
    print(email, "\n")

    sent_email = client.send_email(inbox.address, inbox.address, subject="Send subject", text="Send body")
    print(sent_email, "\n")

    sleep(3)

    emails = client.get_emails(inbox.address)
    print(emails, "\n")

    email = client.get_email(inbox.address, emails.emails[0].id)
    print(email, "\n")

    sent_email = client.reply_to_email(inbox.address, emails.emails[0].id, text="Reply body")
    print(sent_email, "\n")

    sleep(3)

    emails = client.get_emails(inbox.address)
    print(emails, "\n")

    email = client.get_email(inbox.address, emails.emails[0].id)
    print(email, "\n")

    status = client.delete_inbox(inbox.address)
    print(status, "\n")


if __name__ == "__main__":
    main()
