# Reference
## Drafts
<details><summary><code>client.drafts.<a href="src/agentmail/drafts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail
client = AgentMail(api_key="YOUR_API_KEY", )
client.drafts.list(inbox_id='yourinbox@agentmail.to', limit=10, )

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

**limit:** `typing.Optional[Limit]` 
    
</dd>
</dl>

<dl>
<dd>

**last_key:** `typing.Optional[LastKey]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[Labels]` 
    
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

<details><summary><code>client.drafts.<a href="src/agentmail/drafts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail
client = AgentMail(api_key="YOUR_API_KEY", )
client.drafts.get(inbox_id='yourinbox@agentmail.to', draft_id='draft_123', )

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

**draft_id:** `DraftId` 
    
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
client = AgentMail(api_key="YOUR_API_KEY", )
client.inboxes.list(limit=10, last_key='123e4567-e89b-12d3-a456-426614174000', )

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

**limit:** `typing.Optional[Limit]` 
    
</dd>
</dl>

<dl>
<dd>

**last_key:** `typing.Optional[LastKey]` 
    
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
client = AgentMail(api_key="YOUR_API_KEY", )
client.inboxes.get(inbox_id='yourinbox@agentmail.to', )

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
client = AgentMail(api_key="YOUR_API_KEY", )
client.inboxes.create(domain='yourdomain.com', )

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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail
client = AgentMail(api_key="YOUR_API_KEY", )
client.messages.list(inbox_id='yourinbox@agentmail.to', limit=10, )

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

**limit:** `typing.Optional[Limit]` 
    
</dd>
</dl>

<dl>
<dd>

**last_key:** `typing.Optional[LastKey]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[Labels]` 
    
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
client = AgentMail(api_key="YOUR_API_KEY", )
client.messages.get(inbox_id='yourinbox@agentmail.to', message_id='msg_123', )

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
client = AgentMail(api_key="YOUR_API_KEY", )
client.messages.send(inbox_id='yourinbox@agentmail.to', to=['bob@example.com'], cc=['charlie@example.com'], bcc=['david@example.com'], subject='Project Discussion', text="Let's review the timeline for the project.", html="<p>Let's review the timeline for the project.</p>", )

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

**cc:** `typing.Optional[SendMessageCc]` 
    
</dd>
</dl>

<dl>
<dd>

**bcc:** `typing.Optional[SendMessageBcc]` 
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[MessageSubject]` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[MessageText]` 
    
</dd>
</dl>

<dl>
<dd>

**html:** `typing.Optional[MessageHtml]` 
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[SendMessageAttachments]` 
    
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
client = AgentMail(api_key="YOUR_API_KEY", )
client.messages.reply(inbox_id='yourinbox@agentmail.to', message_id='msg_123', text="Thanks for the update. Let's meet tomorrow at 2 PM.", html="<p>Thanks for the update. Let's meet tomorrow at 2 PM.</p>", cc=['charlie@example.com'], bcc=['david@example.com'], )

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

**to:** `typing.Optional[SendMessageTo]` 
    
</dd>
</dl>

<dl>
<dd>

**cc:** `typing.Optional[SendMessageCc]` 
    
</dd>
</dl>

<dl>
<dd>

**bcc:** `typing.Optional[SendMessageBcc]` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[MessageText]` 
    
</dd>
</dl>

<dl>
<dd>

**html:** `typing.Optional[MessageHtml]` 
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[SendMessageAttachments]` 
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail
client = AgentMail(api_key="YOUR_API_KEY", )
client.threads.list(inbox_id='yourinbox@agentmail.to', limit=10, )

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

**limit:** `typing.Optional[Limit]` 
    
</dd>
</dl>

<dl>
<dd>

**last_key:** `typing.Optional[LastKey]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[Labels]` 
    
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
client = AgentMail(api_key="YOUR_API_KEY", )
client.threads.get(inbox_id='yourinbox@agentmail.to', thread_id='thread_123', )

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

## Webhooks
<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail
client = AgentMail(api_key="YOUR_API_KEY", )
client.webhooks.list()

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

**limit:** `typing.Optional[Limit]` 
    
</dd>
</dl>

<dl>
<dd>

**last_key:** `typing.Optional[LastKey]` 
    
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail
client = AgentMail(api_key="YOUR_API_KEY", )
client.webhooks.get(webhook_id='webhook_id', )

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

**webhook_id:** `WebhookId` 
    
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail
client = AgentMail(api_key="YOUR_API_KEY", )
client.webhooks.create(url='url', )

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

**url:** `Url` 
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Optional[Events]` 
    
</dd>
</dl>

<dl>
<dd>

**inboxes:** `typing.Optional[Inboxes]` 
    
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from agentmail import AgentMail
client = AgentMail(api_key="YOUR_API_KEY", )
client.webhooks.delete(webhook_id='webhook_id', )

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

**webhook_id:** `WebhookId` 
    
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

