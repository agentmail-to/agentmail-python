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
client = AgentMail(api_key="YOUR_API_KEY", )
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

**limit:** `typing.Optional[Limit]` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
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
client.inboxes.get(inbox_id='inbox_id', )

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
client.inboxes.create()

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

**display_name:** `typing.Optional[str]` — Display name: `Display Name <username@domain.com>`. Defaults to `AgentMail`. Pass empty string to omit.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ClientId]` 
    
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

## Contexts
<details><summary><code>client.contexts.<a href="src/agentmail/contexts/client.py">list</a>(...)</code></summary>
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
client.contexts.list()

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

**page_token:** `typing.Optional[PageToken]` 
    
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

<details><summary><code>client.contexts.<a href="src/agentmail/contexts/client.py">get</a>(...)</code></summary>
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
client.contexts.get(context_id='context_id', )

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

**context_id:** `ContextId` 
    
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

<details><summary><code>client.contexts.<a href="src/agentmail/contexts/client.py">create</a>(...)</code></summary>
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
client.contexts.create(type='type', data={'data': {'key': 'value'}
}, is_event=True, )

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

**type:** `ContextType` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `ContextData` 
    
</dd>
</dl>

<dl>
<dd>

**is_event:** `ContextIsEvent` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[ContextMetadata]` 
    
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

<details><summary><code>client.contexts.<a href="src/agentmail/contexts/client.py">delete</a>(...)</code></summary>
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
client.contexts.delete(context_id='context_id', )

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

**context_id:** `ContextId` 
    
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
client.drafts.list()

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

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[Labels]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[Ascending]` 
    
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
client.drafts.get(draft_id='draft_id', )

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

## Inboxes Drafts
<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">list</a>(...)</code></summary>
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
client.inboxes.drafts.list(inbox_id='inbox_id', )

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

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[Labels]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[Ascending]` 
    
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">get</a>(...)</code></summary>
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
client.inboxes.drafts.get(inbox_id='inbox_id', draft_id='draft_id', )

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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">create</a>(...)</code></summary>
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
client.inboxes.drafts.create(inbox_id='inbox_id', )

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

**labels:** `typing.Optional[DraftLabels]` 
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[DraftReplyTo]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[DraftTo]` 
    
</dd>
</dl>

<dl>
<dd>

**cc:** `typing.Optional[DraftCc]` 
    
</dd>
</dl>

<dl>
<dd>

**bcc:** `typing.Optional[DraftBcc]` 
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[DraftSubject]` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[DraftText]` 
    
</dd>
</dl>

<dl>
<dd>

**html:** `typing.Optional[DraftHtml]` 
    
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">send</a>(...)</code></summary>
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
client.inboxes.drafts.send(inbox_id='inbox_id', draft_id='draft_id', )

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

**add_labels:** `typing.Optional[typing.Sequence[str]]` — Labels to add to message.
    
</dd>
</dl>

<dl>
<dd>

**remove_labels:** `typing.Optional[typing.Sequence[str]]` — Labels to remove from message.
    
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

## Inboxes Messages
<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">list</a>(...)</code></summary>
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
client.inboxes.messages.list(inbox_id='inbox_id', )

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

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[Labels]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[Ascending]` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">get</a>(...)</code></summary>
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
client.inboxes.messages.get(inbox_id='inbox_id', message_id='message_id', )

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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">send</a>(...)</code></summary>
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
client.inboxes.messages.send(inbox_id='inbox_id', )

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

**labels:** `typing.Optional[MessageLabels]` 
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[SendMessageReplyTo]` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">reply</a>(...)</code></summary>
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
client.inboxes.messages.reply(inbox_id='inbox_id', message_id='message_id', )

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

**labels:** `typing.Optional[MessageLabels]` 
    
</dd>
</dl>

<dl>
<dd>

**reply_to:** `typing.Optional[SendMessageReplyTo]` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">update</a>(...)</code></summary>
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
client.inboxes.messages.update(inbox_id='inbox_id', message_id='message_id', )

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

**add_labels:** `typing.Optional[typing.Sequence[str]]` — Labels to add to message.
    
</dd>
</dl>

<dl>
<dd>

**remove_labels:** `typing.Optional[typing.Sequence[str]]` — Labels to remove from message.
    
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

## Inboxes Threads
<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">list</a>(...)</code></summary>
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
client.inboxes.threads.list(inbox_id='inbox_id', )

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

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[Labels]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[Ascending]` 
    
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

<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">get</a>(...)</code></summary>
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
client.inboxes.threads.get(inbox_id='inbox_id', thread_id='thread_id', )

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
client.threads.list()

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

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[Labels]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[Ascending]` 
    
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
client.threads.get(thread_id='thread_id', )

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

**page_token:** `typing.Optional[PageToken]` 
    
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
client.webhooks.create(url='url', event_types=["message.received", "message.received"], )

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

**event_types:** `EventTypes` 
    
</dd>
</dl>

<dl>
<dd>

**inbox_ids:** `typing.Optional[InboxIds]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[ClientId]` 
    
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

