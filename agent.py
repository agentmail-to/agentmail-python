from typing import Optional, List
from time import sleep

from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

from client import AgentMail

BASE_URL = "https://api.agentmail.dev"
USERNAME = "test"
DOMAIN = "agentmail.dev"


load_dotenv()

client = AgentMail(BASE_URL)


@tool
def create_inbox(username: str):
    """Create email inbox"""
    client.delete_inbox(f"{username}@{DOMAIN}")
    inbox = client.create_inbox(username, DOMAIN)
    sleep(3)
    return inbox


@tool
def get_emails(address: str):
    """Get emails from inbox"""
    return client.get_emails(address)


@tool
def get_email(address: str, id: str):
    """Get email from inbox"""
    return client.get_email(address, id)


@tool
def send_email(
    address: str, to: Optional[List[str]] = None, cc: Optional[List[str]] = None, bcc: Optional[List[str]] = None, subject: Optional[str] = None, text: Optional[str] = None
):
    """Send email"""
    return client.send_email(address, to, cc, bcc, subject, text)


@tool
def reply_to_email(
    address: str,
    id: str,
    to: Optional[List[str]] = None,
    cc: Optional[List[str]] = None,
    bcc: Optional[List[str]] = None,
    subject: Optional[str] = None,
    text: Optional[str] = None,
):
    """Reply to email"""
    return client.reply_to_email(address, id, to, cc, bcc, subject, text)


agent = initialize_agent(
    tools=[create_inbox.as_tool(), get_emails.as_tool(), get_email.as_tool(), send_email.as_tool(), reply_to_email.as_tool()],
    llm=ChatOpenAI(model="gpt-4o", temperature=0),
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
)


def main():
    result = agent.invoke("Create an email inbox with username 'test'. Get the emails from the inbox and desribe them.")

    print("----------Input----------")
    print(result["input"])
    print("----------Output----------")
    print(result["output"])


if __name__ == "__main__":
    main()
