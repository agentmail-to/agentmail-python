# Reference
## Inboxes
<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.inboxes.list()

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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.inboxes.get(
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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.inboxes.create(
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

## Messages
<details><summary><code>client.messages.<a href="src/agentmail/messages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List messages in inbox. If neither or both `received` and `sent` query parameters are set, all messages are returned.
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
from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.messages.list(
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

**received:** `Received` 
    
</dd>
</dl>

<dl>
<dd>

**sent:** `Sent` 
    
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

<details><summary><code>client.messages.<a href="src/agentmail/messages/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.messages.get(
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

<details><summary><code>client.messages.<a href="src/agentmail/messages/client.py">send</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.messages.send(
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

<details><summary><code>client.messages.<a href="src/agentmail/messages/client.py">reply</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.messages.reply(
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
<details><summary><code>client.threads.<a href="src/agentmail/threads/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List threads in inbox. If neither or both `received` and `sent` query parameters are set, all threads are returned.
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
from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.threads.list(
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

**received:** `Received` 
    
</dd>
</dl>

<dl>
<dd>

**sent:** `Sent` 
    
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

<details><summary><code>client.threads.<a href="src/agentmail/threads/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.threads.get(
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

