# Reference
## Inboxes
<details><summary><code>client.inboxes.<a href="src/agent_mail/inboxes/client.py">list_inboxes</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.inboxes.list_inboxes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `QueryLimit` 
    
</dd>
</dl>

<dl>
<dd>

**last_key:** `LastKey` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inboxes.<a href="src/agent_mail/inboxes/client.py">get_inbox</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.inboxes.get_inbox(
    inbox_id="inbox_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inboxes.<a href="src/agent_mail/inboxes/client.py">create_inbox</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.inboxes.create_inbox(
    domain="yourdomain.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**username:** `typing.Optional[str]` — Username of address. Randomly generated if not specified.
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — Domain of address. Must be verified domain. Defaults to `agentmail.to`.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[DisplayName]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inboxes.<a href="src/agent_mail/inboxes/client.py">delete_inbox</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete inbox and all of its threads, messages, and attachments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.inboxes.delete_inbox(
    inbox_id="yourinbox@agentmail.to",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Messages
<details><summary><code>client.messages.<a href="src/agent_mail/messages/client.py">list_messages</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.messages.list_messages(
    inbox_id="inbox_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `QueryLimit` 
    
</dd>
</dl>

<dl>
<dd>

**last_key:** `LastKey` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/agent_mail/messages/client.py">get_message</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.messages.get_message(
    inbox_id="inbox_id",
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `MessageId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/agent_mail/messages/client.py">delete_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete message and its attachments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.messages.delete_message(
    inbox_id="inbox_id",
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `MessageId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/agent_mail/messages/client.py">send_message</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.messages.send_message(
    inbox_id="inbox_id",
    to="to",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `SendMessageTo` 
    
</dd>
</dl>

<dl>
<dd>

**cc:** `SendMessageCc` 
    
</dd>
</dl>

<dl>
<dd>

**bcc:** `SendMessageBcc` 
    
</dd>
</dl>

<dl>
<dd>

**subject:** `MessageSubject` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `MessageText` 
    
</dd>
</dl>

<dl>
<dd>

**html:** `MessageHtml` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.messages.<a href="src/agent_mail/messages/client.py">reply_to_message</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.messages.reply_to_message(
    inbox_id="inbox_id",
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `MessageId` 
    
</dd>
</dl>

<dl>
<dd>

**cc:** `SendMessageCc` 
    
</dd>
</dl>

<dl>
<dd>

**bcc:** `SendMessageBcc` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `MessageText` 
    
</dd>
</dl>

<dl>
<dd>

**html:** `MessageHtml` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[SendMessageTo]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Threads
<details><summary><code>client.threads.<a href="src/agent_mail/threads/client.py">list_threads</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.threads.list_threads(
    inbox_id="inbox_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `QueryLimit` 
    
</dd>
</dl>

<dl>
<dd>

**last_key:** `LastKey` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.threads.<a href="src/agent_mail/threads/client.py">get_thread</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.threads.get_thread(
    inbox_id="inbox_id",
    thread_id="thread_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `ThreadId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.threads.<a href="src/agent_mail/threads/client.py">delete_thread</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete thread and all of its messages and attachments.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agent_mail import AgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)
client.threads.delete_thread(
    inbox_id="inbox_id",
    thread_id="thread_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `ThreadId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

