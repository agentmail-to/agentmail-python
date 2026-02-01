# Reference
## Inboxes
<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListInboxesResponse]</code></summary>
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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">get</a>(...) -&gt; AsyncHttpResponse[Inbox]</code></summary>
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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">create</a>(...) -&gt; AsyncHttpResponse[Inbox]</code></summary>
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

**request:** `typing.Optional[CreateInboxRequest]` 
    
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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">update</a>(...) -&gt; AsyncHttpResponse[Inbox]</code></summary>
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
client.inboxes.update(
    inbox_id="inbox_id",
    display_name="display_name",
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

**display_name:** `DisplayName` 
    
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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
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
client.inboxes.delete(
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

## Pods
<details><summary><code>client.pods.<a href="src/agentmail/pods/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListPodsResponse]</code></summary>
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
client.pods.list()

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

<details><summary><code>client.pods.<a href="src/agentmail/pods/client.py">get</a>(...) -&gt; AsyncHttpResponse[Pod]</code></summary>
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
client.pods.get(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
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

<details><summary><code>client.pods.<a href="src/agentmail/pods/client.py">create</a>(...) -&gt; AsyncHttpResponse[Pod]</code></summary>
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
client.pods.create()

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

**name:** `typing.Optional[Name]` 
    
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

<details><summary><code>client.pods.<a href="src/agentmail/pods/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
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
client.pods.delete(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
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
<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListWebhooksResponse]</code></summary>
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">get</a>(...) -&gt; AsyncHttpResponse[Webhook]</code></summary>
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
client.webhooks.get(
    webhook_id="webhook_id",
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">update</a>(...) -&gt; AsyncHttpResponse[Webhook]</code></summary>
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
client.webhooks.update(
    webhook_id="webhook_id",
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

**webhook_id:** `WebhookId` 
    
</dd>
</dl>

<dl>
<dd>

**add_inbox_ids:** `typing.Optional[InboxIds]` — Inbox IDs to subscribe to the webhook.
    
</dd>
</dl>

<dl>
<dd>

**remove_inbox_ids:** `typing.Optional[InboxIds]` — Inbox IDs to unsubscribe from the webhook.
    
</dd>
</dl>

<dl>
<dd>

**add_pod_ids:** `typing.Optional[PodIds]` — Pod IDs to subscribe to the webhook.
    
</dd>
</dl>

<dl>
<dd>

**remove_pod_ids:** `typing.Optional[PodIds]` — Pod IDs to unsubscribe from the webhook.
    
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">create</a>(...) -&gt; AsyncHttpResponse[Webhook]</code></summary>
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
client.webhooks.create(
    url="url",
    event_types=["message.received", "message.received"],
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

**pod_ids:** `typing.Optional[PodIds]` 
    
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
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
client.webhooks.delete(
    webhook_id="webhook_id",
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

## ApiKeys
<details><summary><code>client.api_keys.<a href="src/agentmail/api_keys/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListApiKeysResponse]</code></summary>
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
client.api_keys.list()

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

<details><summary><code>client.api_keys.<a href="src/agentmail/api_keys/client.py">create</a>(...) -&gt; AsyncHttpResponse[CreateApiKeyResponse]</code></summary>
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
client.api_keys.create(
    name="name",
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

**name:** `Name` 
    
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

<details><summary><code>client.api_keys.<a href="src/agentmail/api_keys/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
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
client.api_keys.delete(
    api_key="api_key",
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

**api_key:** `ApiKeyId` 
    
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

## Domains
<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListDomainsResponse]</code></summary>
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
client.domains.list()

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

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">get</a>(...) -&gt; AsyncHttpResponse[Domain]</code></summary>
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
client.domains.get(
    domain_id="domain_id",
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

**domain_id:** `DomainId` 
    
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

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">get_zone_file</a>(...) -&gt; typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]</code></summary>
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
client.domains.get_zone_file(
    domain_id="domain_id",
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

**domain_id:** `DomainId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">create</a>(...) -&gt; AsyncHttpResponse[Domain]</code></summary>
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
client.domains.create(
    domain="domain",
    feedback_enabled=True,
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

**domain:** `DomainName` 
    
</dd>
</dl>

<dl>
<dd>

**feedback_enabled:** `FeedbackEnabled` 
    
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

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
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
client.domains.delete(
    domain_id="domain_id",
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

**domain_id:** `DomainId` 
    
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

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">verify</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
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
client.domains.verify(
    domain_id="domain_id",
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

**domain_id:** `DomainId` 
    
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
<details><summary><code>client.drafts.<a href="src/agentmail/drafts/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListDraftsResponse]</code></summary>
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

**before:** `typing.Optional[Before]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[After]` 
    
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

<details><summary><code>client.drafts.<a href="src/agentmail/drafts/client.py">get</a>(...) -&gt; AsyncHttpResponse[Draft]</code></summary>
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
client.drafts.get(
    draft_id="draft_id",
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
<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListDraftsResponse]</code></summary>
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
client.inboxes.drafts.list(
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

**before:** `typing.Optional[Before]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[After]` 
    
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">get</a>(...) -&gt; AsyncHttpResponse[Draft]</code></summary>
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
client.inboxes.drafts.get(
    inbox_id="inbox_id",
    draft_id="draft_id",
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">create</a>(...) -&gt; AsyncHttpResponse[Draft]</code></summary>
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
client.inboxes.drafts.create(
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

**attachments:** `typing.Optional[typing.Sequence[SendAttachment]]` — Attachments to include in draft.
    
</dd>
</dl>

<dl>
<dd>

**in_reply_to:** `typing.Optional[DraftInReplyTo]` 
    
</dd>
</dl>

<dl>
<dd>

**send_at:** `typing.Optional[DraftSendAt]` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[DraftClientId]` 
    
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">update</a>(...) -&gt; AsyncHttpResponse[Draft]</code></summary>
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
client.inboxes.drafts.update(
    inbox_id="inbox_id",
    draft_id="draft_id",
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

**draft_id:** `DraftId` 
    
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

**send_at:** `typing.Optional[DraftSendAt]` 
    
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">send</a>(...) -&gt; AsyncHttpResponse[SendMessageResponse]</code></summary>
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
client.inboxes.drafts.send(
    inbox_id="inbox_id",
    draft_id="draft_id",
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
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
client.inboxes.drafts.delete(
    inbox_id="inbox_id",
    draft_id="draft_id",
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

## Inboxes Messages
<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListMessagesResponse]</code></summary>
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
client.inboxes.messages.list(
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

**before:** `typing.Optional[Before]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[After]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[Ascending]` 
    
</dd>
</dl>

<dl>
<dd>

**include_spam:** `typing.Optional[IncludeSpam]` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">get</a>(...) -&gt; AsyncHttpResponse[Message]</code></summary>
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
client.inboxes.messages.get(
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">get_attachment</a>(...) -&gt; AsyncHttpResponse[AttachmentResponse]</code></summary>
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
client.inboxes.messages.get_attachment(
    inbox_id="inbox_id",
    message_id="message_id",
    attachment_id="attachment_id",
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

**attachment_id:** `AttachmentId` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">get_raw</a>(...) -&gt; typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]</code></summary>
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
client.inboxes.messages.get_raw(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">send</a>(...) -&gt; AsyncHttpResponse[SendMessageResponse]</code></summary>
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
client.inboxes.messages.send(
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

**headers:** `typing.Optional[SendMessageHeaders]` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">reply</a>(...) -&gt; AsyncHttpResponse[SendMessageResponse]</code></summary>
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
client.inboxes.messages.reply(
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

**reply_all:** `typing.Optional[ReplyAll]` 
    
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

**headers:** `typing.Optional[SendMessageHeaders]` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">reply_all</a>(...) -&gt; AsyncHttpResponse[SendMessageResponse]</code></summary>
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
client.inboxes.messages.reply_all(
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

**headers:** `typing.Optional[SendMessageHeaders]` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">forward</a>(...) -&gt; AsyncHttpResponse[SendMessageResponse]</code></summary>
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
client.inboxes.messages.forward(
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

**headers:** `typing.Optional[SendMessageHeaders]` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">update</a>(...) -&gt; AsyncHttpResponse[Message]</code></summary>
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
client.inboxes.messages.update(
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

## Inboxes Metrics
<details><summary><code>client.inboxes.metrics.<a href="src/agentmail/inboxes/metrics/client.py">get</a>(...) -&gt; AsyncHttpResponse[ListMetricsResponse]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.inboxes.metrics.get(
    inbox_id="inbox_id",
    start_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
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

**start_timestamp:** `MetricStartTimestamp` 
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `MetricEndTimestamp` 
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[MetricEventTypes]` 
    
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
<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListThreadsResponse]</code></summary>
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
client.inboxes.threads.list(
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

**before:** `typing.Optional[Before]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[After]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[Ascending]` 
    
</dd>
</dl>

<dl>
<dd>

**include_spam:** `typing.Optional[IncludeSpam]` 
    
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

<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">get</a>(...) -&gt; AsyncHttpResponse[Thread]</code></summary>
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
client.inboxes.threads.get(
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

<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">get_attachment</a>(...) -&gt; AsyncHttpResponse[AttachmentResponse]</code></summary>
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
client.inboxes.threads.get_attachment(
    inbox_id="inbox_id",
    thread_id="thread_id",
    attachment_id="attachment_id",
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

**attachment_id:** `AttachmentId` 
    
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

<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
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
client.inboxes.threads.delete(
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

## Metrics
<details><summary><code>client.metrics.<a href="src/agentmail/metrics/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListMetricsResponse]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.metrics.list(
    start_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    end_timestamp=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
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

**start_timestamp:** `MetricStartTimestamp` 
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `MetricEndTimestamp` 
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[MetricEventTypes]` 
    
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

## Organizations
<details><summary><code>client.organizations.<a href="src/agentmail/organizations/client.py">get</a>() -&gt; AsyncHttpResponse[Organization]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the current organization.
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
client.organizations.get()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Pods Domains
<details><summary><code>client.pods.domains.<a href="src/agentmail/pods/domains/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListDomainsResponse]</code></summary>
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
client.pods.domains.list(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pods.domains.<a href="src/agentmail/pods/domains/client.py">create</a>(...) -&gt; AsyncHttpResponse[Domain]</code></summary>
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
client.pods.domains.create(
    pod_id="pod_id",
    domain="domain",
    feedback_enabled=True,
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

**pod_id:** `PodId` 
    
</dd>
</dl>

<dl>
<dd>

**domain:** `DomainName` 
    
</dd>
</dl>

<dl>
<dd>

**feedback_enabled:** `FeedbackEnabled` 
    
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

<details><summary><code>client.pods.domains.<a href="src/agentmail/pods/domains/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
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
client.pods.domains.delete(
    pod_id="pod_id",
    domain_id="domain_id",
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

**pod_id:** `PodId` 
    
</dd>
</dl>

<dl>
<dd>

**domain_id:** `DomainId` 
    
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

## Pods Drafts
<details><summary><code>client.pods.drafts.<a href="src/agentmail/pods/drafts/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListDraftsResponse]</code></summary>
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
client.pods.drafts.list(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
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

**before:** `typing.Optional[Before]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[After]` 
    
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

<details><summary><code>client.pods.drafts.<a href="src/agentmail/pods/drafts/client.py">get</a>(...) -&gt; AsyncHttpResponse[Draft]</code></summary>
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
client.pods.drafts.get(
    pod_id="pod_id",
    draft_id="draft_id",
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

**pod_id:** `PodId` 
    
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

## Pods Inboxes
<details><summary><code>client.pods.inboxes.<a href="src/agentmail/pods/inboxes/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListInboxesResponse]</code></summary>
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
client.pods.inboxes.list(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pods.inboxes.<a href="src/agentmail/pods/inboxes/client.py">get</a>(...) -&gt; AsyncHttpResponse[Inbox]</code></summary>
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
client.pods.inboxes.get(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
</dd>
</dl>

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

<details><summary><code>client.pods.inboxes.<a href="src/agentmail/pods/inboxes/client.py">create</a>(...) -&gt; AsyncHttpResponse[Inbox]</code></summary>
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
client.pods.inboxes.create(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
</dd>
</dl>

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

<details><summary><code>client.pods.inboxes.<a href="src/agentmail/pods/inboxes/client.py">delete</a>(...) -&gt; AsyncHttpResponse[None]</code></summary>
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
client.pods.inboxes.delete(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
</dd>
</dl>

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

## Pods Threads
<details><summary><code>client.pods.threads.<a href="src/agentmail/pods/threads/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListThreadsResponse]</code></summary>
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
client.pods.threads.list(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
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

**before:** `typing.Optional[Before]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[After]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[Ascending]` 
    
</dd>
</dl>

<dl>
<dd>

**include_spam:** `typing.Optional[IncludeSpam]` 
    
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

<details><summary><code>client.pods.threads.<a href="src/agentmail/pods/threads/client.py">get</a>(...) -&gt; AsyncHttpResponse[Thread]</code></summary>
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
client.pods.threads.get(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
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

<details><summary><code>client.pods.threads.<a href="src/agentmail/pods/threads/client.py">get_attachment</a>(...) -&gt; AsyncHttpResponse[AttachmentResponse]</code></summary>
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
client.pods.threads.get_attachment(
    pod_id="pod_id",
    thread_id="thread_id",
    attachment_id="attachment_id",
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

**pod_id:** `PodId` 
    
</dd>
</dl>

<dl>
<dd>

**thread_id:** `ThreadId` 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `AttachmentId` 
    
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
<details><summary><code>client.threads.<a href="src/agentmail/threads/client.py">list</a>(...) -&gt; AsyncHttpResponse[ListThreadsResponse]</code></summary>
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

**before:** `typing.Optional[Before]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[After]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[Ascending]` 
    
</dd>
</dl>

<dl>
<dd>

**include_spam:** `typing.Optional[IncludeSpam]` 
    
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

<details><summary><code>client.threads.<a href="src/agentmail/threads/client.py">get</a>(...) -&gt; AsyncHttpResponse[Thread]</code></summary>
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

<details><summary><code>client.threads.<a href="src/agentmail/threads/client.py">get_attachment</a>(...) -&gt; AsyncHttpResponse[AttachmentResponse]</code></summary>
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
client.threads.get_attachment(
    thread_id="thread_id",
    attachment_id="attachment_id",
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

**thread_id:** `ThreadId` 
    
</dd>
</dl>

<dl>
<dd>

**attachment_id:** `AttachmentId` 
    
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

