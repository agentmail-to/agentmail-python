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
    """Create an email inbox"""
    client.delete_inbox(f"{username}@{DOMAIN}")
    inbox = client.create_inbox(username, DOMAIN)
    sleep(3)
    return inbox


@tool
def get_emails(address: str):
    """Get emails from an inbox"""
    return client.get_emails(address)


agent = initialize_agent(
    tools=[create_inbox.as_tool(), get_emails.as_tool()],
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
