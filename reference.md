# Reference
## Inboxes
<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">list</a>(...) -> ListInboxesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes list
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">search</a>(...) -> SearchInboxesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches inboxes in the organization by address or display name, ranked
by relevance. Each word in the query matches the start of a word in the
address or display name, so `sup` matches `support@example.com` but
`port` does not. An exact address match always ranks first. `limit`
cannot exceed 100. A page can be empty and still carry a
`next_page_token`; keep paging until the token is absent.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.search(
    q="q",
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

**q:** `str` — Address or display name to search for. Matches word prefixes. Must be 2 to 256 characters.
    
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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">get</a>(...) -> Inbox</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes get --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">create</a>(...) -> Inbox</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes create --display-name "My Agent" --username myagent --domain agentmail.to
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">update</a>(...) -> Inbox</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes update --inbox-id <inbox_id> --display-name "Updated Name"
```

To pause an inbox, set `status` to `paused`; set it back to `active` to
resume. See [Pausing an inbox](/inboxes#pausing-an-inbox).
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.update(
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

**request:** `UpdateInboxRequest` — Expects an object; provide at least one of `display_name`, `status`, or `metadata`.
    
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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes delete --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.inboxes.<a href="src/agentmail/inboxes/client.py">authorize</a>(...) -> AuthorizeInboxResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Authorizes the AgentID sign-in a client is already waiting in, for the
inbox in the path, and returns the ID of the pending public key it will
activate. Read the key with Get API Key. A repeat for the same token,
inbox, and bearer returns the same key ID. A `403` `AppSignupLimitError`
means the app accepts no more sign-ups from your organization.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.authorize(
    inbox_id="inbox_id",
    auth_token="blackcurrant..........",
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

**request:** `AuthorizeInboxRequest` 
    
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
<details><summary><code>client.pods.<a href="src/agentmail/pods/client.py">list</a>(...) -> ListPodsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods list
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.pods.<a href="src/agentmail/pods/client.py">get</a>(...) -> Pod</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods get --pod-id <pod_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.pods.<a href="src/agentmail/pods/client.py">create</a>(...) -> Pod</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods create --client-id my-pod
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request:** `CreatePodRequest` 
    
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

<details><summary><code>client.pods.<a href="src/agentmail/pods/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods delete --pod-id <pod_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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
<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">list</a>(...) -> ListWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail webhooks list
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">get</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail webhooks get --webhook-id <webhook_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">get_headers</a>(...) -> WebhookHeaderNamesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the names of custom HTTP headers included with deliveries to this webhook. Header values are
write-only and are never returned.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.webhooks.get_headers(
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">create</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail webhooks create --url https://example.com/webhook --event-types message.received
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.webhooks.create(
    url="url",
    event_types=[
        "message.received",
        "message.received"
    ],
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

**request:** `CreateWebhookRequest` 
    
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">update</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update inbox or pod subscriptions, or replace the webhook's `event_types` in full when you pass a
non-empty `event_types` array (see request field docs). Inbox and pod changes use add/remove lists.

**CLI:**
```bash
agentmail webhooks update --webhook-id <webhook_id> --add-inbox-ids <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request:** `UpdateWebhookRequest` 
    
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

<details><summary><code>client.webhooks.<a href="src/agentmail/webhooks/client.py">update_headers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Atomically set, replace, or remove custom HTTP headers included with deliveries to this webhook.
Header values remain write-only.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.webhooks.update_headers(
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

**request:** `UpdateWebhookHeadersRequest` 
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail webhooks delete --webhook-id <webhook_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

## Accounts
<details><summary><code>client.accounts.<a href="src/agentmail/accounts/client.py">list</a>(...) -> ListAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists accounts across all apps, scoped to the API key: an
organization key sees every account, a pod key its pod's, an inbox key
its inbox's. Requires `inbox_read`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.accounts.list()

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

<details><summary><code>client.accounts.<a href="src/agentmail/accounts/client.py">get</a>(...) -> Account</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one account by ID. An account outside the key's scope is a 404.
Requires `inbox_read`.
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
from agentmail.environment import AgentMailEnvironment
import uuid

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.accounts.get(
    account_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
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

**account_id:** `AccountId` 
    
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

<details><summary><code>client.accounts.<a href="src/agentmail/accounts/client.py">update</a>(...) -> Account</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates one account. Set `status` to `disabled` to stop the inbox from
signing in at the app again, or to `enabled` to re-enable it.
Idempotent: disabling an already disabled account keeps its original
`disabled_at`, and enabling an enabled account is a no-op.

Find the `account_id` with List Accounts. An account exists only after an
inbox's first sign-in at an app, so it cannot be disabled in advance.
A disable applies to that inbox at that app whichever sign-in key is
used: the app's next authorization ends in `access_denied`, and a code
issued earlier is refused with `invalid_grant`. Access tokens already
issued stay valid until they expire, and the app's own session is
unaffected.

Requires `account_update`, which sign-in keys (`type: public_key`) cannot
hold, so call this with a bearer API key. An account outside the key's
scope is a 404. A 409 means the account changed during the write; read it
again and retry.
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
from agentmail.environment import AgentMailEnvironment
import uuid

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.accounts.update(
    account_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
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

**account_id:** `AccountId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateAccountRequest` 
    
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

## Agent
<details><summary><code>client.agent.<a href="src/agentmail/agent/client.py">sign_up</a>(...) -> AgentSignupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new agent organization with an inbox and API key. This endpoint is for signing up for the first time. If you've already signed up, you're all set — just use your existing API key.

A 6-digit OTP is sent to the human's email for verification.

`human_email` is optional. Without it, the inbox can receive email but cannot send to anyone until a human is attached with the attach human endpoint or, for a US-region inbox, claims it in the AgentMail Console with the API key (see [How do I claim my agent's inbox?](https://docs.agentmail.to/knowledge-base/claiming-agent-inbox)). There is also no way to recover the API key, so store it durably. Calling sign-up again without `human_email` creates a new organization, which needs a different `username`: the original username stays with the lost organization's inbox.

This endpoint is idempotent. Calling it again with the same `human_email` will rotate the API key and resend the OTP if expired.

The returned API key has limited permissions until the organization is verified via the verify endpoint.

**CLI:**
```bash
agentmail agent sign-up --human-email user@example.com --username my-agent
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.agent.sign_up(
    username="username",
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

**request:** `AgentSignupRequest` 
    
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

<details><summary><code>client.agent.<a href="src/agentmail/agent/client.py">attach_human</a>(...) -> AgentAttachHumanResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a human to an unverified agent organization. A 6-digit OTP is sent to the human's email, which you then submit to the verify endpoint.

Use it after signing up without a `human_email`. Once the human is attached, the organization can send email to that human only, and verification lifts the remaining restrictions. For up to 5 minutes after attaching, sends to the human can still be rejected with a `429` daily send limit error while the API key's cached limits catch up. Wait and retry.

Calling it again with the same `human_email` does not rotate the API key. It resends the OTP if it was never delivered, or issues a new one if it expired. While the current OTP is still valid, calling it again keeps that OTP and its attempt count. If all 10 attempts are used up, wait until the OTP expires, 24 hours after it was issued, then call it again for a new one.

Calling it with a different `human_email` replaces the attached human and sends the new human an OTP. An organization can replace its human at most 2 times.

Only available until the organization is verified.

**CLI:**
```bash
agentmail agent attach-human --human-email user@example.com
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.agent.attach_human(
    human_email="human_email",
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

**request:** `AgentAttachHumanRequest` 
    
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

<details><summary><code>client.agent.<a href="src/agentmail/agent/client.py">verify</a>(...) -> AgentVerifyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify an agent organization using the 6-digit OTP sent to the human's email during sign-up.

On success, the organization is upgraded from `agent_unverified` to `agent_verified`, the send allowlist is removed, and free plan entitlements are applied.

The OTP expires after 24 hours and allows a maximum of 10 attempts. If the OTP expired, call the attach human endpoint with the same `human_email` to get a new one without rotating the API key. Once all 10 attempts are used, even the correct OTP is rejected, and attach human keeps returning the same OTP until it expires, so wait for it to expire before asking for a new one. An organization that signed up without a `human_email` has no OTP until a human is attached. If you run into any difficulties receiving the OTP code, you can also create an account on [console.agentmail.to](https://console.agentmail.to) using the human email address you provided to verify your account.

**CLI:**
```bash
agentmail agent verify --otp-code 123456
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.agent.verify(
    otp_code="otp_code",
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

**request:** `AgentVerifyRequest` 
    
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
<details><summary><code>client.api_keys.<a href="src/agentmail/api_keys/client.py">list</a>(...) -> ListApiKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists every credential, newest first. Filter one family with `type`.
Page to token exhaustion: a page can be empty and still carry a
`next_page_token`.

**CLI:**
```bash
agentmail api-keys list
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**type:** `typing.Optional[ApiKeyType]` — Restrict the list to one credential family. Omit for every family.
    
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

<details><summary><code>client.api_keys.<a href="src/agentmail/api_keys/client.py">get</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one credential of any family. Public keys also resolve by
`client_id`. Poll a sign-in key until `status` is `active`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.api_keys.get(
    api_key_id="api_key_id",
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

**api_key_id:** `ApiKeyId` 
    
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

<details><summary><code>client.api_keys.<a href="src/agentmail/api_keys/client.py">create</a>(...) -> CreateApiKeyResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a bearer key, or registers a public key when the body carries
`public_key`. The route selects the scope. Bearer secrets are returned once.

**CLI:**
```bash
agentmail api-keys create --name "My Key"
```
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
from agentmail.environment import AgentMailEnvironment
from agentmail.api_keys import CreateBearerApiKeyRequest

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.api_keys.create(
    request=CreateBearerApiKeyRequest(),
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

**request:** `CreateApiKeyRequest` 
    
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

<details><summary><code>client.api_keys.<a href="src/agentmail/api_keys/client.py">update</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Renames a credential or changes its permissions. Public keys also resolve
by `client_id`; a sign-in key accepts only `app_connect` and
`app_share_owner`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.api_keys.update(
    api_key_id="api_key_id",
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

**api_key_id:** `ApiKeyId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateApiKeyRequest` 
    
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

<details><summary><code>client.api_keys.<a href="src/agentmail/api_keys/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes one credential of any family. A pending sign-in key is
cancelled; an active one is revoked. Public keys also resolve by `client_id`.

**CLI:**
```bash
agentmail api-keys delete --api-key-id <api_key_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.api_keys.delete(
    api_key_id="api_key_id",
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

**api_key_id:** `ApiKeyId` 
    
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

## Apps
<details><summary><code>client.apps.<a href="src/agentmail/apps/client.py">list</a>(...) -> ListAppsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists apps, most popular first.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.apps.list()

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

**category:** `typing.Optional[AppCategory]` — Only apps in this category. A filtered page can hold fewer than `limit` apps while more remain, so page until `next_page_token` is absent. A `page_token` works only with the `category` it was returned for.
    
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

<details><summary><code>client.apps.<a href="src/agentmail/apps/client.py">search</a>(...) -> SearchAppsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches apps by name prefix.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.apps.search(
    q="q",
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

**q:** `str` — Name prefix to search for.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[Limit]` 
    
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

<details><summary><code>client.apps.<a href="src/agentmail/apps/client.py">get</a>(...) -> App</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets one app by ID or slug. A catalog app returns its full entry.
A registered app that the catalog does not list returns its ID and
name only, without `updated_at`, so anyone holding its ID can still look
it up; a slug finds catalog apps only. List Apps and Search Apps show
catalog entries only.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.apps.get(
    app_id="app_id",
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

**app_id:** `str` — ID of app, or the `slug` of an app in the catalog. A slug ignores case, spaces and punctuation.
    
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

<details><summary><code>client.apps.<a href="src/agentmail/apps/client.py">list_accounts</a>(...) -> ListAppAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists accounts at one app, most recent sign-in first.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.apps.list_accounts(
    app_id="app_id",
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

**app_id:** `str` — ID of app, or the `slug` of an app in the catalog. A slug ignores case, spaces and punctuation.
    
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

<details><summary><code>client.apps.<a href="src/agentmail/apps/client.py">connect</a>(...) -> ConnectAccepted</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts signing an inbox in to an app. Returns a single-use `magic_url`,
valid for five minutes, to open in the client that will hold the sign-in;
the client enrolls as the inbox and continues to the app.
An app in the catalog can be named by its `slug`, as in
`POST /v0/apps/firecrawl/connect`.
A `404` names the missing resource: `App` or `Inbox`.
A `403` `AppSignupLimitError` means the app accepts no more sign-ups from
your organization; sign in with an inbox that already has an account there.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.apps.connect(
    app_id="app_id",
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

**app_id:** `str` — ID of app, or the `slug` of an app in the catalog. A slug ignores case, spaces and punctuation.
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[ConnectAppBody]` 
    
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

## Auth
<details><summary><code>client.auth.<a href="src/agentmail/auth/client.py">me</a>() -> Identity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the identity and scope of the authenticated credential. Useful when a client holds a pod-scoped or inbox-scoped API key and needs to discover the parent organization, pod, or inbox without prior knowledge.

**CLI:**
```bash
agentmail auth me
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.auth.me()

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

## Domains
<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">list</a>(...) -> ListDomainsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail domains list
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">get</a>(...) -> Domain</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail domains get --domain-id <domain_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">get_zone_file</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail domains get-zone-file --domain-id <domain_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">create</a>(...) -> Domain</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail domains create --domain example.com
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.domains.create(
    domain="domain",
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

**request:** `CreateDomainRequest` 
    
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

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">update</a>(...) -> Domain</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail domains update --domain-id <domain_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.domains.update(
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

**request:** `UpdateDomainRequest` 
    
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

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail domains delete --domain-id <domain_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">verify</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail domains verify --domain-id <domain_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.domains.<a href="src/agentmail/domains/client.py">get_setup_link</a>(...) -> GetSetupLinkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Build a one-click DNS setup link for the domain via the Domain Connect standard. When the domain's DNS provider supports Domain Connect and carries the AgentMail template, the response contains a signed URL: opening it lets the domain owner approve the required DNS records at their provider, which writes them automatically — no copy-paste. When the provider does not support it, `supported` is `false` and the domain's `records` should be added manually instead.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.domains.get_setup_link(
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
<details><summary><code>client.drafts.<a href="src/agentmail/drafts/client.py">list</a>(...) -> ListDraftsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail drafts list
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.drafts.<a href="src/agentmail/drafts/client.py">get</a>(...) -> Draft</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail drafts get --draft-id <draft_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.drafts.<a href="src/agentmail/drafts/client.py">get_attachment</a>(...) -> AttachmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail drafts get-attachment --draft-id <draft_id> --attachment-id <attachment_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.drafts.get_attachment(
    draft_id="draft_id",
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

**draft_id:** `DraftId` 
    
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

## Inboxes Accounts
<details><summary><code>client.inboxes.accounts.<a href="src/agentmail/inboxes/accounts/client.py">list</a>(...) -> ListAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists accounts held by the inbox, across all apps. Requires `inbox_read`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.accounts.list(
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

<details><summary><code>client.inboxes.accounts.<a href="src/agentmail/inboxes/accounts/client.py">get</a>(...) -> Account</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one account held by the inbox. An account elsewhere is a 404. Requires
`inbox_read`.
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
from agentmail.environment import AgentMailEnvironment
import uuid

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.accounts.get(
    inbox_id="inbox_id",
    account_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
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

**account_id:** `AccountId` 
    
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

## Inboxes ApiKeys
<details><summary><code>client.inboxes.api_keys.<a href="src/agentmail/inboxes/api_keys/client.py">list</a>(...) -> ListApiKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes api-keys list --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.api_keys.list(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inboxes.api_keys.<a href="src/agentmail/inboxes/api_keys/client.py">create</a>(...) -> CreateApiKeyResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes api-keys create --inbox-id <inbox_id> --name "My Key"
```
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
from agentmail.environment import AgentMailEnvironment
from agentmail.api_keys import CreateBearerApiKeyRequest

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.api_keys.create(
    inbox_id="inbox_id",
    request=CreateBearerApiKeyRequest(),
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

**request:** `CreateApiKeyRequest` 
    
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

<details><summary><code>client.inboxes.api_keys.<a href="src/agentmail/inboxes/api_keys/client.py">update</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes api-keys update --inbox-id <inbox_id> --api-key-id <api_key_id> --name "Renamed"
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.api_keys.update(
    inbox_id="inbox_id",
    api_key_id="api_key_id",
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

**api_key_id:** `ApiKeyId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateApiKeyRequest` 
    
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

<details><summary><code>client.inboxes.api_keys.<a href="src/agentmail/inboxes/api_keys/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes api-keys delete --inbox-id <inbox_id> --api-key-id <api_key_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.api_keys.delete(
    inbox_id="inbox_id",
    api_key_id="api_key_id",
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

**api_key_id:** `ApiKeyId` 
    
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

## Inboxes Calendar
<details><summary><code>client.inboxes.calendar.<a href="src/agentmail/inboxes/calendar/client.py">get</a>(...) -> Calendar</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the inbox's calendar. Every inbox has one calendar, so this works before any event is
created. Its `etag` (also the `ETag` response header) is the value to send in `If-Match` to
make an update conditional.

Requires the `calendar_read` permission. Calendar is in private beta in US production
(`api.agentmail.to`) and is unavailable in EU production (`api.agentmail.eu`).
Organizations without access receive a `403`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.calendar.get(
    inbox_id="scheduler@agentmail.to",
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

**consistency:** `typing.Optional[CalendarConsistency]` 
    
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

<details><summary><code>client.inboxes.calendar.<a href="src/agentmail/inboxes/calendar/client.py">update</a>(...) -> Calendar</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the calendar's default time zone. Existing events keep their own `timezone`; only
events created later without a `timezone` use the new default.

Requires the `calendar_update` permission. To make the update conditional, send the
calendar's current `etag` in `If-Match`: a stale value returns `412`. Without `If-Match` the
update applies to the calendar as it is.

Calendar is in private beta in US production (`api.agentmail.to`). It is unavailable in EU
production (`api.agentmail.eu`). Organizations without access receive a `403`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.calendar.update(
    inbox_id="scheduler@agentmail.to",
    timezone="America/New_York",
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

**timezone:** `IanaTimezone` — New default time zone for events created without a `timezone`.
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[str]` — The calendar's current `etag`, for example `"rv-0"`. Optional; makes the update conditional; `*` matches any current version.
    
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

<details><summary><code>client.inboxes.calendar.<a href="src/agentmail/inboxes/calendar/client.py">list_events</a>(...) -> ListCalendarEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the events stored on the calendar: one item per one-off or recurring event, plus one
item for each edited date of a recurring event (as that dated event, with
`is_exception: true`). Ordered by most recently updated, and cancelled events are included.
Use it to sync or manage what you created. To see what is on the calendar in a time window,
use Get Agenda.

The list is always read in the region that serves the request, so it can trail a change made
moments earlier by a few seconds. Requires the `calendar_event_read` permission.

Calendar is in private beta in US production (`api.agentmail.to`). It is unavailable in EU
production (`api.agentmail.eu`). Organizations without access receive a `403`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.calendar.list_events(
    inbox_id="scheduler@agentmail.to",
    limit=50,
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

**limit:** `typing.Optional[CalendarLimit]` 
    
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

<details><summary><code>client.inboxes.calendar.<a href="src/agentmail/inboxes/calendar/client.py">get_agenda</a>(...) -> ListCalendarEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists every date on the calendar in a time window, ordered by start time: one-off events,
and recurring events expanded into their individual dates, with cancelled dates left out.
Use it to answer "what is on the calendar".

The window defaults to now through 90 days from now and can be at most 366 days. Items omit
`description`, `metadata` and `attendees`; get an event by ID for the full object. An item
the inbox is invited to still carries `response_status`, so `needs_action` marks an
invitation waiting for a reply. Dates of
recurring events appear only up to about 90 days from now; use List Event Instances for a
recurring event's later dates. While a recurring event's dates are being regenerated after a
schedule change, which takes a few seconds, the agenda can briefly leave out some of them;
dates that have already started or ended stay as they ran.

The agenda is read in the region that serves the request, so it can trail a change made
moments earlier by a few seconds. Pass `consistency=primary` to read your own change right
away. Requires the `calendar_event_read` permission.

Calendar is in private beta in US production (`api.agentmail.to`). It is unavailable in EU
production (`api.agentmail.eu`). Organizations without access receive a `403`.
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
from agentmail.environment import AgentMailEnvironment
import datetime

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.calendar.get_agenda(
    inbox_id="scheduler@agentmail.to",
    after=datetime.datetime.fromisoformat("2026-10-07T00:00:00+00:00"),
    before=datetime.datetime.fromisoformat("2026-10-16T00:00:00+00:00"),
    limit=3,
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

**consistency:** `typing.Optional[CalendarConsistency]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[WindowAfter]` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[WindowBefore]` 
    
</dd>
</dl>

<dl>
<dd>

**include_overlapping:** `typing.Optional[IncludeOverlapping]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[CalendarLimit]` 
    
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

<details><summary><code>client.inboxes.calendar.<a href="src/agentmail/inboxes/calendar/client.py">create_event</a>(...) -> CalendarEventMutationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a one-off or recurring event on the inbox's calendar. Times are wall-clock values in
`timezone` (the calendar's default time zone if omitted); the response also gives each
boundary as a UTC instant in `start_at` and `end_at`.

`calendar.event.created` is sent once the event is stored, then `calendar.event.starting`
and `calendar.event.ending` as each date begins and ends. With `send_invites: true` the
inbox also emails an invitation to every attendee.

Pass `client_id` to make retries safe: repeating the request with the same `client_id` and
body returns the original event with status `200` instead of `201`, for as long as the event
exists.

With `send_invites: true`, each attendee counts as one send against the organization, pod
and inbox send limits, charged before the event is stored. An over-limit request returns
`429` `rate_limit_exceeded` and creates nothing. A replay of an earlier create is not
charged again.

The event's `etag` is the value to send in `If-Match` to make a later update or delete
conditional. Requires the `calendar_event_create` permission.

Calendar is in private beta in US production (`api.agentmail.to`). It is unavailable in EU
production (`api.agentmail.eu`). Organizations without access receive a `403`.
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
from agentmail.environment import AgentMailEnvironment
from agentmail.calendar import Attendee

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.calendar.create_event(
    inbox_id="scheduler@agentmail.to",
    client_id="intro-acme-2026-10-15",
    title="Intro call with Acme",
    description="Walk Jane through the onboarding plan.",
    location="https://meet.example.com/acme-intro",
    metadata={"crm_deal_id": "D-1042"},
    start="2026-10-15T14:00:00",
    end="2026-10-15T14:30:00",
    timezone="America/New_York",
    attendees=[
        Attendee(
            email="jane@acme.com",
            name="Jane Doe",
        )
    ],
    send_invites=True,
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

**request:** `CreateCalendarEventRequest` 
    
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

<details><summary><code>client.inboxes.calendar.<a href="src/agentmail/inboxes/calendar/client.py">get_event</a>(...) -> CalendarEvent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets an event by its UUID, or one date of a recurring event by its dated ID
(`<uuid>_<slot>`). A dated ID returns the date as it currently stands, including any edit
to it, with `kind: instance`.

The response's `etag` (also the `ETag` header) is the value to send in `If-Match` to make an
update, delete or response to this event or date conditional. Treat it as opaque.

Reads can trail a change made moments earlier by a few seconds; pass `consistency=primary`
to read the latest state of an event or a date. A date that has already started or ended
reads back as it ran, even if a later change to the series no longer produces it. Requires
the `calendar_event_read` permission.

Calendar is in private beta in US production (`api.agentmail.to`). It is unavailable in EU
production (`api.agentmail.eu`). Organizations without access receive a `403`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.calendar.get_event(
    inbox_id="scheduler@agentmail.to",
    event_id="3f8a2c1e-6b4d-4e9f-a7c2-5d1b8e0f9a36",
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

**event_id:** `CalendarEventId` 
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[CalendarConsistency]` 
    
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

<details><summary><code>client.inboxes.calendar.<a href="src/agentmail/inboxes/calendar/client.py">update_event</a>(...) -> CalendarEventMutationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an event. Send only the fields to change. To make the update conditional, send the
event's current `etag` in `If-Match`: a stale value returns `412`. Without `If-Match` the
update applies to the event as it is; a change that lands while it runs returns `409`
`race_condition`, so retry. Send `If-Match` when replacing `attendees`, so you don't
overwrite a response that arrived in the meantime.

- **One-off or series UUID:** changes the event itself. For a series, the change applies to
  every date that has not been edited individually.
- **Dated ID (`<uuid>_<slot>`):** changes one date (`mode=single`, the default) or that date
  and every later date (`mode=future`). `all_day`, `timezone` and `recurrence` cannot be sent
  for a dated ID.

Once a date has started, its start can no longer change (409 `event_already_started`), but
its end and status can; for a one-off or series UUID, send the unchanged `start` with the new
`end`. Once it has ended, only `title`, `description`, `location`,
`metadata` and `attendees` can change. During the few seconds a date is starting, schedule
changes return 409 `event_starting`; retry shortly.

Sends `calendar.event.updated`. With `send_invites: true` the organizer inbox also emails the
updated invitation to every attendee. Requires the `calendar_event_update` permission.

Emailing attendees counts one send per attendee against the organization, pod and inbox
send limits, charged before the change is saved; an over-limit request returns `429`
`rate_limit_exceeded` and changes nothing.

Calendar is in private beta in US production (`api.agentmail.to`). It is unavailable in EU
production (`api.agentmail.eu`). Organizations without access receive a `403`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.calendar.update_event(
    inbox_id="scheduler@agentmail.to",
    event_id="3f8a2c1e-6b4d-4e9f-a7c2-5d1b8e0f9a36",
    start="2026-10-15T15:00:00",
    end="2026-10-15T15:30:00",
    send_invites=True,
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

**event_id:** `CalendarEventId` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[InstanceMutationMode]` 
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[str]` — The event's or date's current `etag`, from the latest read or write response. Optional; makes the update conditional; `*` matches any current version.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Set to `null` to clear.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[str]` — Set to `null` to clear.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Any]` — Replaces the metadata (any JSON value, usually an object). Set to `null` to clear.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[CalendarEventStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**all_day:** `typing.Optional[bool]` — Changing `all_day` requires `start`, `end` and `timezone` in the same request. Not accepted for dated event IDs.
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[WallTime]` — New start. For a one-off or series UUID, send it together with `end`. Not accepted with `mode=future`.
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[WallTime]` — New end. For a one-off or series UUID, send it together with `start`. A dated ID accepts `end` alone.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[IanaTimezone]` — New time zone. Not accepted for dated event IDs.
    
</dd>
</dl>

<dl>
<dd>

**duration_mode:** `typing.Optional[DurationMode]` 
    
</dd>
</dl>

<dl>
<dd>

**recurrence:** `typing.Optional[RecurrenceInput]` 

Replaces the recurrence. Set to `null` to turn a series into a one-off event (only when no
date of it has been edited). Not accepted for dated event IDs.
    
</dd>
</dl>

<dl>
<dd>

**attendees:** `typing.Optional[typing.List[Attendee]]` — Replaces the attendee list.
    
</dd>
</dl>

<dl>
<dd>

**send_invites:** `typing.Optional[bool]` 

When `true`, emails the updated invitation to every attendee. Only the organizer (an `api`
event) can send. Defaults to `false`.
    
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

<details><summary><code>client.inboxes.calendar.<a href="src/agentmail/inboxes/calendar/client.py">delete_event</a>(...) -> DeleteCalendarEventResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an event, or cancels dates of a recurring event.

- **One-off or series UUID:** deletes the event and every date of it. The event disappears
  from reads immediately and is removed in the background; the response is `202` with a
  `deletion_id`. A retry returns the same `deletion_id` while removal runs (send the same
  `Idempotency-Key`, or none and the same `send_invites`); once it has finished, the event
  no longer exists and a retry returns `404`. No `calendar.event.starting` or
  `calendar.event.ending` webhook is sent for the event after the delete is accepted.
- **Dated ID (`<uuid>_<slot>`):** cancels that date (`mode=single`, the default) or that date
  and every later date (`mode=future`). Returns `202` with the cancelled date. A `mode=future`
  delete from the first date deletes the whole series and returns a `deletion_id` instead.
  A date that is already running still gets its `calendar.event.ending`.

Deleting a one-off or series event sends `calendar.event.deleted`. Cancelling dates sends
`calendar.event.updated` with the cancelled date. With `send_invites=true` the organizer
inbox also emails a cancellation to every attendee. Requires the `calendar_event_delete`
permission. To make the delete conditional, send the current `etag` in `If-Match`.

Emailing cancellations counts one send per attendee against the organization, pod and inbox
send limits, charged before the delete; an over-limit request returns `429`
`rate_limit_exceeded` and deletes nothing.

Calendar is in private beta in US production (`api.agentmail.to`). It is unavailable in EU
production (`api.agentmail.eu`). Organizations without access receive a `403`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.calendar.delete_event(
    inbox_id="scheduler@agentmail.to",
    event_id="3f8a2c1e-6b4d-4e9f-a7c2-5d1b8e0f9a36",
    send_invites=True,
    idempotency_key="delete-intro-acme",
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

**event_id:** `CalendarEventId` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[InstanceMutationMode]` 
    
</dd>
</dl>

<dl>
<dd>

**send_invites:** `typing.Optional[bool]` — When `true`, emails a cancellation (iCalendar `CANCEL`) to every attendee. Only the organizer can send. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[str]` — The event's or date's current `etag`. Optional; makes the delete conditional; `*` matches any current version.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` 

1 to 128 visible ASCII characters. Optional. Retrying a delete with the same key
returns the original result; without a key, retries of the same delete share one
derived from the event and `send_invites`, so a keyless retry that changes
`send_invites` is a different delete and returns `404` while removal runs. Keys are
unique across your organization: reusing one to delete a different event returns
`409` `idempotency_conflict`.
    
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

<details><summary><code>client.inboxes.calendar.<a href="src/agentmail/inboxes/calendar/client.py">list_event_instances</a>(...) -> ListCalendarEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the dates of one recurring event in a time window, in start order, with each date's
edits applied. Dates are computed from the rule, so this works for any window up to 366
days, including dates far in the future. Cancelled dates are left out.

The window defaults to now through 90 days from now. Items omit `description`, `metadata`
and `attendees`; get a date by its ID for the full object. Like other reads, the list can
trail a change made moments earlier by a few seconds; pass `consistency=primary` to read
your own change right away. Requires the `calendar_event_read` permission.

Calendar is in private beta in US production (`api.agentmail.to`). It is unavailable in EU
production (`api.agentmail.eu`). Organizations without access receive a `403`.
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
from agentmail.environment import AgentMailEnvironment
import datetime

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.calendar.list_event_instances(
    inbox_id="scheduler@agentmail.to",
    event_id="7c4e9b2a-1f3d-4a8e-b6c5-2e9d0f1a8b47",
    after=datetime.datetime.fromisoformat("2026-10-05T00:00:00+00:00"),
    before=datetime.datetime.fromisoformat("2026-10-10T00:00:00+00:00"),
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

**event_id:** `str` — UUID of the recurring event.
    
</dd>
</dl>

<dl>
<dd>

**consistency:** `typing.Optional[CalendarConsistency]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[WindowAfter]` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[WindowBefore]` 
    
</dd>
</dl>

<dl>
<dd>

**include_overlapping:** `typing.Optional[IncludeOverlapping]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[CalendarLimit]` 
    
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

<details><summary><code>client.inboxes.calendar.<a href="src/agentmail/inboxes/calendar/client.py">respond_to_event</a>(...) -> CalendarEventMutationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accepts, declines or tentatively accepts an invitation the inbox received by email. Pass the
event's UUID to respond for every date, or a dated ID to respond for one date only.

Only works on `email` events where the inbox is an attendee; anything else returns 409
`calendar_response_invalid`. Updates the inbox's attendee entry and sends
`calendar.event.responded`. With `send_reply` (default `true`) the inbox emails the response
to the organizer.

Requires the `calendar_event_update` permission. To make the response conditional, send the
current `etag` in `If-Match`.

A reply email counts as one send against the organization, pod and inbox send limits,
charged before the response is saved; an over-limit request returns `429`
`rate_limit_exceeded` and changes nothing.

Calendar is in private beta in US production (`api.agentmail.to`). It is unavailable in EU
production (`api.agentmail.eu`). Organizations without access receive a `403`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.calendar.respond_to_event(
    inbox_id="scheduler@agentmail.to",
    event_id="a1d5c7e9-2b4f-4c6a-9e8d-3f7b1c5a9d20",
    status="accepted",
    comment="See you there.",
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

**event_id:** `CalendarEventId` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `RespondStatus` 
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[str]` — The event's or date's current `etag`. Optional; makes the response conditional; `*` matches any current version.
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` 

Comment to include with the response. At most 4,096 UTF-8 bytes, with no control characters
other than tab, line feed and carriage return; a longer comment returns `400`. It is stored
as the inbox's attendee `comment`.
    
</dd>
</dl>

<dl>
<dd>

**send_reply:** `typing.Optional[bool]` — When `true` (default), emails the response (iCalendar `REPLY`) to the organizer.
    
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
<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">list</a>(...) -> ListDraftsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes drafts list --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">get</a>(...) -> Draft</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes drafts get --inbox-id <inbox_id> --draft-id <draft_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">get_attachment</a>(...) -> AttachmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes drafts get-attachment --inbox-id <inbox_id> --draft-id <draft_id> --attachment-id <attachment_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.drafts.get_attachment(
    inbox_id="inbox_id",
    draft_id="draft_id",
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

**draft_id:** `DraftId` 
    
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">create</a>(...) -> Draft</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a draft. Supply `in_reply_to` to create a reply draft (with
`reply_all` to address the whole thread), whose recipients, subject, and
threading are derived from the referenced message, or `forward_of` to
create a forward draft, which derives the subject, threading, and
forwarded content from the source but keeps recipients caller-supplied.

**CLI:**
```bash
agentmail inboxes drafts create --inbox-id <inbox_id> --to recipient@example.com --subject "Draft subject" --text "Draft body"
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request:** `CreateDraftRequest` 
    
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">update</a>(...) -> Draft</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edit fields on an existing draft. Passing `null` clears a field (or `[]`
for a recipient field); `send_at: null` un-schedules a scheduled draft.
A draft that is already being sent cannot be edited.

**CLI:**
```bash
agentmail inboxes drafts update --inbox-id <inbox_id> --draft-id <draft_id> --subject "Updated subject"
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request:** `UpdateDraftRequest` 
    
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes drafts delete --inbox-id <inbox_id> --draft-id <draft_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.inboxes.drafts.<a href="src/agentmail/inboxes/drafts/client.py">send</a>(...) -> SendMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes drafts send --inbox-id <inbox_id> --draft-id <draft_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request:** `UpdateMessageRequest` 
    
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

## Inboxes Events
<details><summary><code>client.inboxes.events.<a href="src/agentmail/inboxes/events/client.py">list</a>(...) -> ListInboxEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List label change events for an inbox. Returns events in reverse chronological order by default. Use for IMAP UID projection or audit logging.

**CLI:**
```bash
agentmail inboxes events list --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.events.list(
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

## Inboxes Lists
<details><summary><code>client.inboxes.lists.<a href="src/agentmail/inboxes/lists/client.py">list</a>(...) -> PodListListEntriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes lists list --inbox-id <inbox_id> --direction <direction> --type <type>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.lists.list(
    inbox_id="inbox_id",
    direction="send",
    type="allow",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
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

<details><summary><code>client.inboxes.lists.<a href="src/agentmail/inboxes/lists/client.py">get</a>(...) -> PodListEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes lists get --inbox-id <inbox_id> --direction <direction> --type <type> --entry <entry>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.lists.get(
    inbox_id="inbox_id",
    direction="send",
    type="allow",
    entry="entry",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
</dd>
</dl>

<dl>
<dd>

**entry:** `str` — Email address or domain.
    
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

<details><summary><code>client.inboxes.lists.<a href="src/agentmail/inboxes/lists/client.py">create</a>(...) -> PodListEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes lists create --inbox-id <inbox_id> --direction <direction> --type <type> --entry user@example.com
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.lists.create(
    inbox_id="inbox_id",
    direction="send",
    type="allow",
    entry="entry",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateListEntryRequest` 
    
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

<details><summary><code>client.inboxes.lists.<a href="src/agentmail/inboxes/lists/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes lists delete --inbox-id <inbox_id> --direction <direction> --type <type> --entry <entry>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.lists.delete(
    inbox_id="inbox_id",
    direction="send",
    type="allow",
    entry="entry",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
</dd>
</dl>

<dl>
<dd>

**entry:** `str` — Email address or domain.
    
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
<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">list</a>(...) -> ListMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists messages in the inbox, most recent first. Pass `from`, `to`, or
`subject` to filter by substring. Filtered requests are served by
search, which caps `limit` at 100. For relevance-ranked full-text
search across sender, recipients, subject, and message body, use
`Search Messages`.

**CLI:**
```bash
agentmail inboxes messages list --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**include_blocked:** `typing.Optional[IncludeBlocked]` 
    
</dd>
</dl>

<dl>
<dd>

**include_unauthenticated:** `typing.Optional[IncludeUnauthenticated]` 
    
</dd>
</dl>

<dl>
<dd>

**include_trash:** `typing.Optional[IncludeTrash]` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[typing.List[str]]` — Filter to messages whose sender contains this value (substring match). Repeatable; all values must match.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[typing.List[str]]` — Filter to messages whose recipients (to, cc, or bcc) contain this value (substring match). Repeatable; all values must match.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[typing.List[str]]` — Filter to messages whose subject contains this value (substring match). Repeatable; all values must match.
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">search</a>(...) -> SearchMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Full-text search across messages in the inbox, ranked by relevance. The
query is matched against the sender, recipients, and subject (substring)
and the message body (tokenized full text). Spam, trash, blocked, and
unauthenticated messages are always excluded. `limit` cannot exceed 100.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.messages.search(
    inbox_id="inbox_id",
    q="q",
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

**q:** `Query` 
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">get</a>(...) -> Message</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes messages get --inbox-id <inbox_id> --message-id <message_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">batch_get</a>(...) -> BatchGetMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch metadata for up to 500 messages in one request. Missing or
restricted IDs are silently omitted; compare `count` against `limit`
to detect misses.

**CLI:**
```bash
agentmail inboxes messages batch-get --inbox-id <inbox_id> --message-ids <id1> --message-ids <id2>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.messages.batch_get(
    inbox_id="inbox_id",
    message_ids=[
        "message_ids",
        "message_ids"
    ],
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

**request:** `BatchGetMessagesRequest` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">batch_update</a>(...) -> BatchUpdateMessagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Apply one label change to up to 50 messages in a single request. The
same add_labels and remove_labels apply to every message id, and at
least one of them must be provided. The update is atomic: either all
resolved messages are updated or none are. Missing or restricted ids
are silently excluded; compare `count` against `limit` to detect
exclusions.

**CLI:**
```bash
agentmail inboxes messages batch-update --inbox-id <inbox_id> --message-ids <id1> --message-ids <id2> --add-labels read --remove-labels unread
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.messages.batch_update(
    inbox_id="inbox_id",
    message_ids=[
        "message_ids",
        "message_ids"
    ],
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

**request:** `BatchUpdateMessagesRequest` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">get_attachment</a>(...) -> AttachmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes messages get-attachment --inbox-id <inbox_id> --message-id <message_id> --attachment-id <attachment_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">get_raw</a>(...) -> RawMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes messages get-raw --inbox-id <inbox_id> --message-id <message_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">update</a>(...) -> UpdateMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes messages update --inbox-id <inbox_id> --message-id <message_id> --add-labels read --remove-labels unread
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request:** `UpdateMessageRequest` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a message.

**CLI:**
```bash
agentmail inboxes messages delete --inbox-id <inbox_id> --message-id <message_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.messages.delete(
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">send</a>(...) -> SendMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes messages send --inbox-id <inbox_id> --to recipient@example.com --subject "Hello" --text "Body"
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request:** `SendMessageRequest` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">reply</a>(...) -> SendMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes messages reply --inbox-id <inbox_id> --message-id <message_id> --text "Reply text"
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request:** `ReplyToMessageRequest` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">reply_all</a>(...) -> SendMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes messages reply-all --inbox-id <inbox_id> --message-id <message_id> --text "Reply text"
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request:** `ReplyAllMessageRequest` 
    
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

<details><summary><code>client.inboxes.messages.<a href="src/agentmail/inboxes/messages/client.py">forward</a>(...) -> SendMessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes messages forward --inbox-id <inbox_id> --message-id <message_id> --to recipient@example.com
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request:** `SendMessageRequest` 
    
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
<details><summary><code>client.inboxes.metrics.<a href="src/agentmail/inboxes/metrics/client.py">query_events</a>(...) -> QueryMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Counts of email events (sent, delivered, bounced, etc.) over time for
the inbox. Defaults to the last 24 hours; `start` must be within the
last 90 days, and a future `end` is clamped to now. Omit `period` for
individual event counts, or set it to sum counts into buckets of that
many seconds.

**CLI:**
```bash
agentmail inboxes metrics query-events --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.metrics.query_events(
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

**event_types:** `typing.Optional[MetricEventTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[Start]` 
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[End]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[Period]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[MetricLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**descending:** `typing.Optional[Descending]` 
    
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

<details><summary><code>client.inboxes.metrics.<a href="src/agentmail/inboxes/metrics/client.py">query_usage</a>(...) -> QueryUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cumulative usage series for the inbox. Each point is the running total
of the usage type at that timestamp, not the change within the bucket.
Inbox-scoped queries carry `storage_bytes`, `message_count`, and
`thread_count`; requested types that don't apply to the scope are
ignored. Defaults to the last 24 hours; `start` must be within the
last 90 days, and a future `end` is clamped to now. The range divided
by `period` must not exceed 1000 buckets.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.metrics.query_usage(
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

**usage_types:** `typing.Optional[UsageTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[Start]` 
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[End]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[Period]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[MetricLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**descending:** `typing.Optional[Descending]` 
    
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

<details><summary><code>client.inboxes.metrics.<a href="src/agentmail/inboxes/metrics/client.py">query_rates</a>(...) -> QueryRatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rolling bounce and complaint rates for the inbox. At each `period`
grid point, the bounced (or complained) messages over the preceding
`window` divided by the messages sent over the same window, with the
send count alongside. Account moderation evaluates the organization-wide
rate, so use the organization endpoint to see the number it acts on;
the inbox view shows which inboxes contribute. Defaults to the rolling
24-hour rate sampled hourly over the last day; `start` must be within
the last 90 days, `window` must be a whole multiple of `period`, and
the range plus window divided by `period` must not exceed 1000
buckets.

**CLI:**
```bash
agentmail inboxes metrics query-rates --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.metrics.query_rates(
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

**rate_types:** `typing.Optional[RateTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[Start]` 
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[End]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[RatePeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**window:** `typing.Optional[Window]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[MetricLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**descending:** `typing.Optional[Descending]` 
    
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
<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">list</a>(...) -> ListThreadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists threads in the inbox, most recent first. Pass `senders`,
`recipients`, or `subject` to filter by substring. Filtered requests are
served by search, which caps `limit` at 100. For relevance-ranked
full-text search, use `Search Threads`.

**CLI:**
```bash
agentmail inboxes threads list --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**include_blocked:** `typing.Optional[IncludeBlocked]` 
    
</dd>
</dl>

<dl>
<dd>

**include_unauthenticated:** `typing.Optional[IncludeUnauthenticated]` 
    
</dd>
</dl>

<dl>
<dd>

**include_trash:** `typing.Optional[IncludeTrash]` 
    
</dd>
</dl>

<dl>
<dd>

**senders:** `typing.Optional[typing.List[str]]` — Filter to threads whose senders contain this value (substring match). Repeatable; all values must match.
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[typing.List[str]]` — Filter to threads whose recipients contain this value (substring match). Repeatable; all values must match.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[typing.List[str]]` — Filter to threads whose subject contains this value (substring match). Repeatable; all values must match.
    
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

<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">search</a>(...) -> SearchThreadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Full-text search across threads in the inbox, ranked by relevance. The
query is matched against senders, recipients, and subject (substring)
and the message body (tokenized full text). Spam, trash, blocked, and
unauthenticated threads are always excluded. `limit` cannot exceed 100.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.threads.search(
    inbox_id="inbox_id",
    q="q",
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

**q:** `Query` 
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">get</a>(...) -> Thread</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes threads get --inbox-id <inbox_id> --thread-id <thread_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**limit:** `typing.Optional[Limit]` — Maximum number of messages to return. Cannot exceed 100.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` — Token returned by the previous response for retrieving the next, older page.
    
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

<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">get_attachment</a>(...) -> AttachmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes threads get-attachment --inbox-id <inbox_id> --thread-id <thread_id> --attachment-id <attachment_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">update</a>(...) -> UpdateThreadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates thread labels. Cannot add or remove system labels (sent, received, bounced, etc.). Rejects requests with a `422` for threads with 100 or more messages.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.threads.update(
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

**request:** `UpdateThreadRequest` 
    
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

<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a thread and all of its messages.

**CLI:**
```bash
agentmail inboxes threads delete --inbox-id <inbox_id> --thread-id <thread_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

## Inboxes Webhooks
<details><summary><code>client.inboxes.webhooks.<a href="src/agentmail/inboxes/webhooks/client.py">list</a>(...) -> ListWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes webhooks list --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.webhooks.list(
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

<details><summary><code>client.inboxes.webhooks.<a href="src/agentmail/inboxes/webhooks/client.py">get</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes webhooks get --inbox-id <inbox_id> --webhook-id <webhook_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.webhooks.get(
    inbox_id="inbox_id",
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

**inbox_id:** `InboxId` 
    
</dd>
</dl>

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

<details><summary><code>client.inboxes.webhooks.<a href="src/agentmail/inboxes/webhooks/client.py">get_headers</a>(...) -> WebhookHeaderNamesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the names of custom HTTP headers included with deliveries to this inbox-scoped webhook.
Header values are write-only and are never returned.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.webhooks.get_headers(
    inbox_id="inbox_id",
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

**inbox_id:** `InboxId` 
    
</dd>
</dl>

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

<details><summary><code>client.inboxes.webhooks.<a href="src/agentmail/inboxes/webhooks/client.py">create</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a webhook scoped to this inbox.

**CLI:**
```bash
agentmail inboxes webhooks create --inbox-id <inbox_id> --url https://example.com/webhook --event-types message.received
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.webhooks.create(
    inbox_id="inbox_id",
    url="url",
    event_types=[
        "message.received",
        "message.received"
    ],
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

**request:** `CreateInboxWebhookRequest` 
    
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

<details><summary><code>client.inboxes.webhooks.<a href="src/agentmail/inboxes/webhooks/client.py">update</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes webhooks update --inbox-id <inbox_id> --webhook-id <webhook_id> --event-types message.received
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.webhooks.update(
    inbox_id="inbox_id",
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

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `WebhookId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateInboxWebhookRequest` 
    
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

<details><summary><code>client.inboxes.webhooks.<a href="src/agentmail/inboxes/webhooks/client.py">update_headers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Atomically set, replace, or remove custom HTTP headers included with deliveries to this
inbox-scoped webhook. Header values remain write-only.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.webhooks.update_headers(
    inbox_id="inbox_id",
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

**inbox_id:** `InboxId` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `WebhookId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateWebhookHeadersRequest` 
    
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

<details><summary><code>client.inboxes.webhooks.<a href="src/agentmail/inboxes/webhooks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes webhooks delete --inbox-id <inbox_id> --webhook-id <webhook_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.inboxes.webhooks.delete(
    inbox_id="inbox_id",
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

**inbox_id:** `InboxId` 
    
</dd>
</dl>

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

## Lists
<details><summary><code>client.lists.<a href="src/agentmail/lists/client.py">list</a>(...) -> ListListEntriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail lists list --direction <direction> --type <type>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.lists.list(
    direction="send",
    type="allow",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
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

<details><summary><code>client.lists.<a href="src/agentmail/lists/client.py">get</a>(...) -> ListEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail lists get --direction <direction> --type <type> --entry <entry>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.lists.get(
    direction="send",
    type="allow",
    entry="entry",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
</dd>
</dl>

<dl>
<dd>

**entry:** `str` — Email address or domain.
    
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

<details><summary><code>client.lists.<a href="src/agentmail/lists/client.py">create</a>(...) -> ListEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail lists create --direction <direction> --type <type> --entry user@example.com
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.lists.create(
    direction="send",
    type="allow",
    entry="entry",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateListEntryRequest` 
    
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

<details><summary><code>client.lists.<a href="src/agentmail/lists/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail lists delete --direction <direction> --type <type> --entry <entry>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.lists.delete(
    direction="send",
    type="allow",
    entry="entry",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
</dd>
</dl>

<dl>
<dd>

**entry:** `str` — Email address or domain.
    
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
<details><summary><code>client.metrics.<a href="src/agentmail/metrics/client.py">query_events</a>(...) -> QueryMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Counts of email events (sent, delivered, bounced, etc.) over time for
the organization. Defaults to the last 24 hours; `start` must be within
the last 90 days, and a future `end` is clamped to now. Omit `period`
for individual event counts, or set it to sum counts into buckets of
that many seconds.

**CLI:**
```bash
agentmail metrics query-events
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.metrics.query_events()

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

**event_types:** `typing.Optional[MetricEventTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[Start]` 
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[End]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[Period]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[MetricLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**descending:** `typing.Optional[Descending]` 
    
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

<details><summary><code>client.metrics.<a href="src/agentmail/metrics/client.py">query_usage</a>(...) -> QueryUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cumulative usage series for the organization. Each point is the running
total of the usage type at that timestamp, not the change within the
bucket. Defaults to the last 24 hours; `start` must be within the last
90 days, and a future `end` is clamped to now. The range divided by
`period` must not exceed 1000 buckets.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.metrics.query_usage()

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

**usage_types:** `typing.Optional[UsageTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[Start]` 
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[End]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[Period]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[MetricLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**descending:** `typing.Optional[Descending]` 
    
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

<details><summary><code>client.metrics.<a href="src/agentmail/metrics/client.py">query_rates</a>(...) -> QueryRatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rolling bounce and complaint rates for the organization. At each
`period` grid point, the bounced (or complained) messages over the
preceding `window` divided by the messages sent over the same window,
with the send count alongside so you can see the volume behind
it. This is the number AgentMail's account moderation acts on: a
warning at a 5% bounce rate and suspension at 10%, evaluated over a
rolling 24 hours once at least 1,000 messages were sent in that
window. Defaults to the rolling 24-hour rate sampled hourly over the
last day; `start` must be within the last 90 days, `window` must be a
whole multiple of `period`, and the range plus window divided by
`period` must not exceed 1000 buckets.

**CLI:**
```bash
agentmail metrics query-rates
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.metrics.query_rates()

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

**rate_types:** `typing.Optional[RateTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[Start]` 
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[End]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[RatePeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**window:** `typing.Optional[Window]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[MetricLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**descending:** `typing.Optional[Descending]` 
    
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
<details><summary><code>client.organizations.<a href="src/agentmail/organizations/client.py">get</a>() -> Organization</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the organization for the authenticated API key (usage limits, counts, and billing metadata).

**CLI:**
```bash
agentmail organizations get
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

## Pods Accounts
<details><summary><code>client.pods.accounts.<a href="src/agentmail/pods/accounts/client.py">list</a>(...) -> ListAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists accounts held by inboxes in the pod, across all apps. Requires `inbox_read`.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.accounts.list(
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

<details><summary><code>client.pods.accounts.<a href="src/agentmail/pods/accounts/client.py">get</a>(...) -> Account</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one account held by inboxes in the pod. An account elsewhere is a 404. Requires
`inbox_read`.
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
from agentmail.environment import AgentMailEnvironment
import uuid

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.accounts.get(
    pod_id="pod_id",
    account_id=uuid.UUID("d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"),
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

**account_id:** `AccountId` 
    
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

## Pods ApiKeys
<details><summary><code>client.pods.api_keys.<a href="src/agentmail/pods/api_keys/client.py">list</a>(...) -> ListApiKeysResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods api-keys list --pod-id <pod_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.api_keys.list(
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

<details><summary><code>client.pods.api_keys.<a href="src/agentmail/pods/api_keys/client.py">create</a>(...) -> CreateApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods api-keys create --pod-id <pod_id> --name "My Key"
```
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
from agentmail.environment import AgentMailEnvironment
from agentmail.api_keys import CreateBearerApiKeyRequest

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.api_keys.create(
    pod_id="pod_id",
    request=CreateBearerApiKeyRequest(),
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

**request:** `CreateApiKeyRequest` 
    
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

<details><summary><code>client.pods.api_keys.<a href="src/agentmail/pods/api_keys/client.py">update</a>(...) -> ApiKey</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods api-keys update --pod-id <pod_id> --api-key-id <api_key_id> --name "Renamed"
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.api_keys.update(
    pod_id="pod_id",
    api_key_id="api_key_id",
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

**api_key_id:** `ApiKeyId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateApiKeyRequest` 
    
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

<details><summary><code>client.pods.api_keys.<a href="src/agentmail/pods/api_keys/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods api-keys delete --pod-id <pod_id> --api-key-id <api_key_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.api_keys.delete(
    pod_id="pod_id",
    api_key_id="api_key_id",
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

**api_key_id:** `ApiKeyId` 
    
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

## Pods Domains
<details><summary><code>client.pods.domains.<a href="src/agentmail/pods/domains/client.py">list</a>(...) -> ListDomainsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods domains list --pod-id <pod_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.pods.domains.<a href="src/agentmail/pods/domains/client.py">get</a>(...) -> Domain</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods domains get --pod-id <pod_id> --domain-id <domain_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.domains.get(
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

<details><summary><code>client.pods.domains.<a href="src/agentmail/pods/domains/client.py">get_zone_file</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods domains get-zone-file --pod-id <pod_id> --domain-id <domain_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.domains.get_zone_file(
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

<details><summary><code>client.pods.domains.<a href="src/agentmail/pods/domains/client.py">create</a>(...) -> Domain</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods domains create --pod-id <pod_id> --domain example.com
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.domains.create(
    pod_id="pod_id",
    domain="domain",
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

**request:** `CreateDomainRequest` 
    
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

<details><summary><code>client.pods.domains.<a href="src/agentmail/pods/domains/client.py">update</a>(...) -> Domain</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods domains update --pod-id <pod_id> --domain-id <domain_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.domains.update(
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

**request:** `UpdateDomainRequest` 
    
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

<details><summary><code>client.pods.domains.<a href="src/agentmail/pods/domains/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods domains delete --pod-id <pod_id> --domain-id <domain_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.pods.domains.<a href="src/agentmail/pods/domains/client.py">verify</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods domains verify --pod-id <pod_id> --domain-id <domain_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.domains.verify(
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
<details><summary><code>client.pods.drafts.<a href="src/agentmail/pods/drafts/client.py">list</a>(...) -> ListDraftsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods drafts list --pod-id <pod_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.pods.drafts.<a href="src/agentmail/pods/drafts/client.py">get</a>(...) -> Draft</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods drafts get --pod-id <pod_id> --draft-id <draft_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.pods.drafts.<a href="src/agentmail/pods/drafts/client.py">get_attachment</a>(...) -> AttachmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods drafts get-attachment --pod-id <pod_id> --draft-id <draft_id> --attachment-id <attachment_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.drafts.get_attachment(
    pod_id="pod_id",
    draft_id="draft_id",
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

**draft_id:** `DraftId` 
    
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

## Pods Inboxes
<details><summary><code>client.pods.inboxes.<a href="src/agentmail/pods/inboxes/client.py">list</a>(...) -> ListInboxesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods inboxes list --pod-id <pod_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.pods.inboxes.<a href="src/agentmail/pods/inboxes/client.py">search</a>(...) -> SearchInboxesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches inboxes in the pod by address or display name, ranked by
relevance. Each word in the query matches the start of a word in the
address or display name, so `sup` matches `support@example.com` but
`port` does not. An exact address match always ranks first. `limit`
cannot exceed 100. A page can be empty and still carry a
`next_page_token`; keep paging until the token is absent.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.inboxes.search(
    pod_id="pod_id",
    q="q",
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

**q:** `str` — Address or display name to search for. Matches word prefixes. Must be 2 to 256 characters.
    
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

<details><summary><code>client.pods.inboxes.<a href="src/agentmail/pods/inboxes/client.py">get</a>(...) -> Inbox</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods inboxes get --pod-id <pod_id> --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.pods.inboxes.<a href="src/agentmail/pods/inboxes/client.py">create</a>(...) -> Inbox</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods inboxes create --pod-id <pod_id> --username myagent --domain example.com
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**request:** `CreateInboxRequest` 
    
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

<details><summary><code>client.pods.inboxes.<a href="src/agentmail/pods/inboxes/client.py">update</a>(...) -> Inbox</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods inboxes update --pod-id <pod_id> --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.inboxes.update(
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

**request:** `UpdateInboxRequest` 
    
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

<details><summary><code>client.pods.inboxes.<a href="src/agentmail/pods/inboxes/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods inboxes delete --pod-id <pod_id> --inbox-id <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

## Pods Lists
<details><summary><code>client.pods.lists.<a href="src/agentmail/pods/lists/client.py">list</a>(...) -> PodListListEntriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods lists list --pod-id <pod_id> --direction <direction> --type <type>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.lists.list(
    pod_id="pod_id",
    direction="send",
    type="allow",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
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

<details><summary><code>client.pods.lists.<a href="src/agentmail/pods/lists/client.py">get</a>(...) -> PodListEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods lists get --pod-id <pod_id> --direction <direction> --type <type> --entry <entry>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.lists.get(
    pod_id="pod_id",
    direction="send",
    type="allow",
    entry="entry",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
</dd>
</dl>

<dl>
<dd>

**entry:** `str` — Email address or domain.
    
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

<details><summary><code>client.pods.lists.<a href="src/agentmail/pods/lists/client.py">create</a>(...) -> PodListEntry</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods lists create --pod-id <pod_id> --direction <direction> --type <type> --entry user@example.com
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.lists.create(
    pod_id="pod_id",
    direction="send",
    type="allow",
    entry="entry",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateListEntryRequest` 
    
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

<details><summary><code>client.pods.lists.<a href="src/agentmail/pods/lists/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods lists delete --pod-id <pod_id> --direction <direction> --type <type> --entry <entry>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.lists.delete(
    pod_id="pod_id",
    direction="send",
    type="allow",
    entry="entry",
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

**direction:** `Direction` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `ListType` 
    
</dd>
</dl>

<dl>
<dd>

**entry:** `str` — Email address or domain.
    
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

## Pods Metrics
<details><summary><code>client.pods.metrics.<a href="src/agentmail/pods/metrics/client.py">query_events</a>(...) -> QueryMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Counts of email events (sent, delivered, bounced, etc.) over time for
the pod. Defaults to the last 24 hours; `start` must be within the last
90 days, and a future `end` is clamped to now. Omit `period` for
individual event counts, or set it to sum counts into buckets of that
many seconds.

**CLI:**
```bash
agentmail pods metrics query-events --pod-id <pod_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.metrics.query_events(
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

**event_types:** `typing.Optional[MetricEventTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[Start]` 
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[End]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[Period]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[MetricLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**descending:** `typing.Optional[Descending]` 
    
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

<details><summary><code>client.pods.metrics.<a href="src/agentmail/pods/metrics/client.py">query_usage</a>(...) -> QueryUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cumulative usage series for the pod. Each point is the running total of
the usage type at that timestamp, not the change within the bucket.
Pod-scoped queries carry every usage type except `pod_count`; requested
types that don't apply to the scope are ignored. Defaults to the last
24 hours; `start` must be within the last 90 days, and a future `end`
is clamped to now. The range divided by `period` must not exceed 1000
buckets.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.metrics.query_usage(
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

**usage_types:** `typing.Optional[UsageTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[Start]` 
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[End]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[Period]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[MetricLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**descending:** `typing.Optional[Descending]` 
    
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

<details><summary><code>client.pods.metrics.<a href="src/agentmail/pods/metrics/client.py">query_rates</a>(...) -> QueryRatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rolling bounce and complaint rates for the pod. At each `period` grid
point, the bounced (or complained) messages over the preceding
`window` divided by the messages sent over the same window, with the
send count alongside. Account moderation evaluates the organization-wide
rate, so use the organization endpoint to see the number it acts on;
the pod view shows which pods contribute. Defaults to the rolling
24-hour rate sampled hourly over the last day; `start` must be within
the last 90 days, `window` must be a whole multiple of `period`, and
the range plus window divided by `period` must not exceed 1000
buckets.

**CLI:**
```bash
agentmail pods metrics query-rates --pod-id <pod_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.metrics.query_rates(
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

**rate_types:** `typing.Optional[RateTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[Start]` 
    
</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[End]` 
    
</dd>
</dl>

<dl>
<dd>

**period:** `typing.Optional[RatePeriod]` 
    
</dd>
</dl>

<dl>
<dd>

**window:** `typing.Optional[Window]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[MetricLimit]` 
    
</dd>
</dl>

<dl>
<dd>

**descending:** `typing.Optional[Descending]` 
    
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
<details><summary><code>client.pods.threads.<a href="src/agentmail/pods/threads/client.py">list</a>(...) -> ListThreadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists threads in the pod, most recent first. Pass `senders`,
`recipients`, or `subject` to filter by substring. Filtered requests are
served by search, which caps `limit` at 100. For relevance-ranked
full-text search, use `Search Threads`.

**CLI:**
```bash
agentmail pods threads list --pod-id <pod_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**include_blocked:** `typing.Optional[IncludeBlocked]` 
    
</dd>
</dl>

<dl>
<dd>

**include_unauthenticated:** `typing.Optional[IncludeUnauthenticated]` 
    
</dd>
</dl>

<dl>
<dd>

**include_trash:** `typing.Optional[IncludeTrash]` 
    
</dd>
</dl>

<dl>
<dd>

**senders:** `typing.Optional[typing.List[str]]` — Filter to threads whose senders contain this value (substring match). Repeatable; all values must match.
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[typing.List[str]]` — Filter to threads whose recipients contain this value (substring match). Repeatable; all values must match.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[typing.List[str]]` — Filter to threads whose subject contains this value (substring match). Repeatable; all values must match.
    
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

<details><summary><code>client.pods.threads.<a href="src/agentmail/pods/threads/client.py">search</a>(...) -> SearchThreadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Full-text search across threads in the pod, ranked by relevance. The
query is matched against senders, recipients, and subject (substring)
and the message body (tokenized full text). Spam, trash, blocked, and
unauthenticated threads are always excluded. `limit` cannot exceed 100.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.threads.search(
    pod_id="pod_id",
    q="q",
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

**q:** `Query` 
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pods.threads.<a href="src/agentmail/pods/threads/client.py">get</a>(...) -> Thread</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods threads get --pod-id <pod_id> --thread-id <thread_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**limit:** `typing.Optional[Limit]` — Maximum number of messages to return. Cannot exceed 100.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` — Token returned by the previous response for retrieving the next, older page.
    
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

<details><summary><code>client.pods.threads.<a href="src/agentmail/pods/threads/client.py">get_attachment</a>(...) -> AttachmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods threads get-attachment --pod-id <pod_id> --thread-id <thread_id> --attachment-id <attachment_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.pods.threads.<a href="src/agentmail/pods/threads/client.py">update</a>(...) -> UpdateThreadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates thread labels. Cannot add or remove system labels (sent, received, bounced, etc.). Rejects requests with a `422` for threads with 100 or more messages.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.threads.update(
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

**request:** `UpdateThreadRequest` 
    
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

<details><summary><code>client.pods.threads.<a href="src/agentmail/pods/threads/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a thread and all of its messages.

**CLI:**
```bash
agentmail pods threads delete --pod-id <pod_id> --thread-id <thread_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.threads.delete(
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

## Pods Webhooks
<details><summary><code>client.pods.webhooks.<a href="src/agentmail/pods/webhooks/client.py">list</a>(...) -> ListWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods webhooks list --pod-id <pod_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.webhooks.list(
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

<details><summary><code>client.pods.webhooks.<a href="src/agentmail/pods/webhooks/client.py">get</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods webhooks get --pod-id <pod_id> --webhook-id <webhook_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.webhooks.get(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
</dd>
</dl>

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

<details><summary><code>client.pods.webhooks.<a href="src/agentmail/pods/webhooks/client.py">get_headers</a>(...) -> WebhookHeaderNamesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the names of custom HTTP headers included with deliveries to this pod-scoped webhook.
Header values are write-only and are never returned.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.webhooks.get_headers(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
</dd>
</dl>

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

<details><summary><code>client.pods.webhooks.<a href="src/agentmail/pods/webhooks/client.py">create</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a webhook scoped to this pod.

**CLI:**
```bash
agentmail pods webhooks create --pod-id <pod_id> --url https://example.com/webhook --event-types message.received
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.webhooks.create(
    pod_id="pod_id",
    url="url",
    event_types=[
        "message.received",
        "message.received"
    ],
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

**request:** `CreatePodWebhookRequest` 
    
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

<details><summary><code>client.pods.webhooks.<a href="src/agentmail/pods/webhooks/client.py">update</a>(...) -> Webhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods webhooks update --pod-id <pod_id> --webhook-id <webhook_id> --add-inbox-ids <inbox_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.webhooks.update(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `WebhookId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdatePodWebhookRequest` 
    
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

<details><summary><code>client.pods.webhooks.<a href="src/agentmail/pods/webhooks/client.py">update_headers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Atomically set, replace, or remove custom HTTP headers included with deliveries to this
pod-scoped webhook. Header values remain write-only.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.webhooks.update_headers(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `WebhookId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateWebhookHeadersRequest` 
    
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

<details><summary><code>client.pods.webhooks.<a href="src/agentmail/pods/webhooks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods webhooks delete --pod-id <pod_id> --webhook-id <webhook_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.pods.webhooks.delete(
    pod_id="pod_id",
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

**pod_id:** `PodId` 
    
</dd>
</dl>

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

## Threads
<details><summary><code>client.threads.<a href="src/agentmail/threads/client.py">list</a>(...) -> ListThreadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists threads, most recent first. Pass `senders`, `recipients`, or
`subject` to filter by substring. Filtered requests are served by
search, which caps `limit` at 100. For relevance-ranked full-text
search across senders, recipients, subject, and message body, use
`Search Threads`.

**CLI:**
```bash
agentmail threads list
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**include_blocked:** `typing.Optional[IncludeBlocked]` 
    
</dd>
</dl>

<dl>
<dd>

**include_unauthenticated:** `typing.Optional[IncludeUnauthenticated]` 
    
</dd>
</dl>

<dl>
<dd>

**include_trash:** `typing.Optional[IncludeTrash]` 
    
</dd>
</dl>

<dl>
<dd>

**senders:** `typing.Optional[typing.List[str]]` — Filter to threads whose senders contain this value (substring match). Repeatable; all values must match.
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[typing.List[str]]` — Filter to threads whose recipients contain this value (substring match). Repeatable; all values must match.
    
</dd>
</dl>

<dl>
<dd>

**subject:** `typing.Optional[typing.List[str]]` — Filter to threads whose subject contains this value (substring match). Repeatable; all values must match.
    
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

<details><summary><code>client.threads.<a href="src/agentmail/threads/client.py">search</a>(...) -> SearchThreadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Full-text search across threads in the organization, ranked by
relevance. The query is matched against senders, recipients, and
subject (substring) and the message body (tokenized full text). Spam,
trash, blocked, and unauthenticated threads are always excluded.
`limit` cannot exceed 100.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.threads.search(
    q="q",
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

**q:** `Query` 
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.threads.<a href="src/agentmail/threads/client.py">get</a>(...) -> Thread</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail threads get --thread-id <thread_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

**limit:** `typing.Optional[Limit]` — Maximum number of messages to return. Cannot exceed 100.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` — Token returned by the previous response for retrieving the next, older page.
    
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

<details><summary><code>client.threads.<a href="src/agentmail/threads/client.py">get_attachment</a>(...) -> AttachmentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail threads get-attachment --thread-id <thread_id> --attachment-id <attachment_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
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

<details><summary><code>client.threads.<a href="src/agentmail/threads/client.py">update</a>(...) -> UpdateThreadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates thread labels. Cannot add or remove system labels (sent, received, bounced, etc.). Rejects requests with a `422` for threads with 100 or more messages.
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.threads.update(
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

**request:** `UpdateThreadRequest` 
    
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

<details><summary><code>client.threads.<a href="src/agentmail/threads/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes a thread and all of its messages.

**CLI:**
```bash
agentmail threads delete --thread-id <thread_id>
```
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
from agentmail.environment import AgentMailEnvironment

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.threads.delete(
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

