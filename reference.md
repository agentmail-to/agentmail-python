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
agentmail webhooks create --url https://example.com/webhook --event-type message.received
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

**CLI:**
```bash
agentmail webhooks update --webhook-id <webhook_id> --add-inbox-id <inbox_id>
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
    human_email="human_email",
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

The OTP expires after 24 hours and allows a maximum of 10 attempts.

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

<details><summary><code>client.api_keys.<a href="src/agentmail/api_keys/client.py">create</a>(...) -> CreateApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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

client = AgentMail(
    api_key="<token>",
    environment=AgentMailEnvironment.PROD,
)

client.api_keys.create()

```
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

<details><summary><code>client.api_keys.<a href="src/agentmail/api_keys/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
agentmail inboxes:api-keys list --inbox-id <inbox_id>
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

<details><summary><code>client.inboxes.api_keys.<a href="src/agentmail/inboxes/api_keys/client.py">create</a>(...) -> CreateApiKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes:api-keys create --inbox-id <inbox_id> --name "My Key"
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

client.inboxes.api_keys.create(
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
agentmail inboxes:api-keys delete --inbox-id <inbox_id> --api-key-id <api_key_id>
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
agentmail inboxes:drafts list --inbox-id <inbox_id>
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
agentmail inboxes:drafts get --inbox-id <inbox_id> --draft-id <draft_id>
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
agentmail inboxes:drafts get-attachment --inbox-id <inbox_id> --draft-id <draft_id> --attachment-id <attachment_id>
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

**CLI:**
```bash
agentmail inboxes:drafts create --inbox-id <inbox_id> --to recipient@example.com --subject "Draft subject" --text "Draft body"
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

**CLI:**
```bash
agentmail inboxes:drafts update --inbox-id <inbox_id> --draft-id <draft_id> --subject "Updated subject"
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
agentmail inboxes:drafts delete --inbox-id <inbox_id> --draft-id <draft_id>
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
agentmail inboxes:drafts send --inbox-id <inbox_id> --draft-id <draft_id>
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
agentmail inboxes:events list --inbox-id <inbox_id>
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
agentmail inboxes:lists list --inbox-id <inbox_id> --direction <direction> --type <type>
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
agentmail inboxes:lists get --inbox-id <inbox_id> --direction <direction> --type <type> --entry <entry>
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
agentmail inboxes:lists create --inbox-id <inbox_id> --direction <direction> --type <type> --entry user@example.com
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
agentmail inboxes:lists delete --inbox-id <inbox_id> --direction <direction> --type <type> --entry <entry>
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

**CLI:**
```bash
agentmail inboxes:messages list --inbox-id <inbox_id>
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

**include_trash:** `typing.Optional[IncludeTrash]` 
    
</dd>
</dl>

<dl>
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
agentmail inboxes:messages get --inbox-id <inbox_id> --message-id <message_id>
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
agentmail inboxes:messages get-attachment --inbox-id <inbox_id> --message-id <message_id> --attachment-id <attachment_id>
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
agentmail inboxes:messages get-raw --inbox-id <inbox_id> --message-id <message_id>
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
agentmail inboxes:messages update --inbox-id <inbox_id> --message-id <message_id> --add-label read --remove-label unread
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
agentmail inboxes:messages delete --inbox-id <inbox_id> --message-id <message_id>
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
agentmail inboxes:messages send --inbox-id <inbox_id> --to recipient@example.com --subject "Hello" --text "Body"
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
agentmail inboxes:messages reply --inbox-id <inbox_id> --message-id <message_id> --text "Reply text"
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
agentmail inboxes:messages reply-all --inbox-id <inbox_id> --message-id <message_id> --text "Reply text"
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
agentmail inboxes:messages forward --inbox-id <inbox_id> --message-id <message_id> --to recipient@example.com
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
<details><summary><code>client.inboxes.metrics.<a href="src/agentmail/inboxes/metrics/client.py">query</a>(...) -> QueryMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes:metrics query --inbox-id <inbox_id>
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

client.inboxes.metrics.query(
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

## Inboxes Threads
<details><summary><code>client.inboxes.threads.<a href="src/agentmail/inboxes/threads/client.py">list</a>(...) -> ListThreadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail inboxes:threads list --inbox-id <inbox_id>
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

**include_trash:** `typing.Optional[IncludeTrash]` 
    
</dd>
</dl>

<dl>
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
agentmail inboxes:threads get --inbox-id <inbox_id> --thread-id <thread_id>
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
agentmail inboxes:threads get-attachment --inbox-id <inbox_id> --thread-id <thread_id> --attachment-id <attachment_id>
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

Moves the thread to trash by adding a trash label to all messages. If the thread is already in trash, it will be permanently deleted. Use `permanent=true` to force permanent deletion.

**CLI:**
```bash
agentmail inboxes:threads delete --inbox-id <inbox_id> --thread-id <thread_id>
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

**permanent:** `typing.Optional[bool]` — If true, permanently delete the thread instead of moving to trash.
    
</dd>
</dl>

<dl>
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
<details><summary><code>client.metrics.<a href="src/agentmail/metrics/client.py">query</a>(...) -> QueryMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail metrics list
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

client.metrics.query()

```
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
agentmail pods:api-keys list --pod-id <pod_id>
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
agentmail pods:api-keys create --pod-id <pod_id> --name "My Key"
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

client.pods.api_keys.create(
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
agentmail pods:api-keys delete --pod-id <pod_id> --api-key-id <api_key_id>
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
agentmail pods:domains list --pod-id <pod_id>
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
agentmail pods:domains get --pod-id <pod_id> --domain-id <domain_id>
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
agentmail pods:domains get-zone-file --pod-id <pod_id> --domain-id <domain_id>
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
agentmail pods:domains create --pod-id <pod_id> --domain example.com
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
agentmail pods:domains update --pod-id <pod_id> --domain-id <domain_id>
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
agentmail pods:domains delete --pod-id <pod_id> --domain-id <domain_id>
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
agentmail pods:domains verify --pod-id <pod_id> --domain-id <domain_id>
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
agentmail pods:drafts list --pod-id <pod_id>
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
agentmail pods:drafts get --pod-id <pod_id> --draft-id <draft_id>
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
agentmail pods:drafts get-attachment --pod-id <pod_id> --draft-id <draft_id> --attachment-id <attachment_id>
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
agentmail pods:inboxes list --pod-id <pod_id>
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
agentmail pods:inboxes get --pod-id <pod_id> --inbox-id <inbox_id>
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
agentmail pods:inboxes create --pod-id <pod_id> --username myagent --domain example.com
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
agentmail pods:inboxes update --pod-id <pod_id> --inbox-id <inbox_id>
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
agentmail pods:inboxes delete --pod-id <pod_id> --inbox-id <inbox_id>
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
agentmail pods:lists list --pod-id <pod_id> --direction <direction> --type <type>
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
agentmail pods:lists get --pod-id <pod_id> --direction <direction> --type <type> --entry <entry>
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
agentmail pods:lists create --pod-id <pod_id> --direction <direction> --type <type> --entry user@example.com
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
agentmail pods:lists delete --pod-id <pod_id> --direction <direction> --type <type> --entry <entry>
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
<details><summary><code>client.pods.metrics.<a href="src/agentmail/pods/metrics/client.py">query</a>(...) -> QueryMetricsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods:metrics query --pod-id <pod_id>
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

client.pods.metrics.query(
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

## Pods Threads
<details><summary><code>client.pods.threads.<a href="src/agentmail/pods/threads/client.py">list</a>(...) -> ListThreadsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**CLI:**
```bash
agentmail pods:threads list --pod-id <pod_id>
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

**include_trash:** `typing.Optional[IncludeTrash]` 
    
</dd>
</dl>

<dl>
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
agentmail pods:threads get --pod-id <pod_id> --thread-id <thread_id>
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
agentmail pods:threads get-attachment --pod-id <pod_id> --thread-id <thread_id> --attachment-id <attachment_id>
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

Moves the thread to trash by adding a trash label to all messages. If the thread is already in trash, it will be permanently deleted. Use `permanent=true` to force permanent deletion.

**CLI:**
```bash
agentmail pods:threads delete --pod-id <pod_id> --thread-id <thread_id>
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

**permanent:** `typing.Optional[bool]` — If true, permanently delete the thread instead of moving to trash.
    
</dd>
</dl>

<dl>
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

**include_trash:** `typing.Optional[IncludeTrash]` 
    
</dd>
</dl>

<dl>
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

Moves the thread to trash by adding a trash label to all messages. If the thread is already in trash, it will be permanently deleted. Use `permanent=true` to force permanent deletion.

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

**permanent:** `typing.Optional[bool]` — If true, permanently delete the thread instead of moving to trash.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

