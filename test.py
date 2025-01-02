from client import AgentMail

BASE_URL = "https://api.agentmail.dev"
USERNAME = "test"
DOMAIN = "agentmail.dev"


def main():
    client = AgentMail(BASE_URL)

    response = client.create_inbox()
    print(response)

    print(client.delete_inbox(response.address))


if __name__ == "__main__":
    main()
