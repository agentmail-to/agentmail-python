# AgentMail Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fagentmail-to%2Fagentmail-python)
[![pypi](https://img.shields.io/pypi/v/agentmail)](https://pypi.python.org/pypi/agentmail)

The AgentMail Python library provides convenient access to the AgentMail API from Python.

## Installation

```sh
pip install agentmail
```

## Reference

A full reference for this library is available [here](./reference.md).

## Usage

Instantiate and use the client with the following:

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

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from agent_mail import AsyncAgentMailApi
from agent_mail.environment import AgentMailApiEnvironment

client = AsyncAgentMailApi(
    api_key="YOUR_API_KEY",
    environment=AgentMailApiEnvironment.PRODUCTION,
)


async def main() -> None:
    await client.inboxes.create_inbox(
        domain="yourdomain.com",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from agent_mail.core.api_error import ApiError

try:
    client.inboxes.create_inbox(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.inboxes.create_inbox(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from agent_mail import AgentMailApi

client = AgentMailApi(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.inboxes.create_inbox(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.
```python
import httpx
from agent_mail import AgentMailApi

client = AgentMailApi(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
