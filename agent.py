from typing import Optional, List

from dotenv import load_dotenv
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from client import AgentMail

BASE_URL = "https://api.agentmail.dev"


load_dotenv()

client = AgentMail(BASE_URL)


@tool
def create_inbox(username: str):
    """Create email inbox"""
    inbox = client.create_inbox(username)
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
def get_sent_emails(address: str):
    """Get sent emails from inbox"""
    return client.get_sent_emails(address)


@tool
def get_sent_email(address: str, id: str):
    """Get sent email from inbox"""
    return client.get_sent_email(address, id)


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


def main():
    inbox = client.create_inbox()

    agent_executor = create_react_agent(
        model=ChatOpenAI(model="gpt-4o", temperature=0),
        tools=[create_inbox, get_emails, get_email, get_sent_emails, get_sent_email, send_email, reply_to_email],
        state_modifier=SystemMessage(content=f"Your email address is {inbox.address}"),
        checkpointer=MemorySaver(),
    )

    def invoke_agent(message: str):
        config = {"configurable": {"thread_id": "0"}}
        messages = agent_executor.invoke({"messages": [message]}, config)
        return messages["messages"][-1]

    while True:
        prompt = input("---------------------Prompt---------------------\n\n")
        if prompt.lower() == "quit":
            break

        print(f"\n--------------------Response--------------------\n")

        message = HumanMessage(content=prompt)
        response = invoke_agent(message).content

        print(f"\n{response}\n")

    client.delete_inbox(inbox.address)


if __name__ == "__main__":
    main()
