# Agentmail Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fagentmail-to%2Fagentmail-python)
[![pypi](https://img.shields.io/pypi/v/agentmail)](https://pypi.python.org/pypi/agentmail)

The Agentmail Python library provides convenient access to the Agentmail APIs from Python.

## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)
- [Pagination](#pagination)
- [Websockets](#websockets)

## Installation

```sh
pip install agentmail
```

## Reference

A full reference for this library is available [here](https://github.com/agentmail-to/agentmail-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
client.inboxes.create()
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from agentmail import AsyncAgentMail

client = AsyncAgentMail(
    api_key="YOUR_API_KEY",
)


async def main() -> None:
    await client.inboxes.create()


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from agentmail.core.api_error import ApiError

try:
    client.inboxes.create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from agentmail import AgentMail

client = AgentMail(
    ...,
)
response = client.inboxes.with_raw_response.create(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

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
client.inboxes.create(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from agentmail import AgentMail

client = AgentMail(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.inboxes.create(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from agentmail import AgentMail

client = AgentMail(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
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
## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from agentmail import AgentMail

client = AgentMail(
    api_key="YOUR_API_KEY",
)
response = client.inboxes.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page
```

## Websockets

The SDK supports both sync and async websocket connections for real-time, low-latency communication. Sockets can be created using the `connect` method, which returns a context manager. 
You can either iterate through the returned `SocketClient` to process messages as they arrive, or attach handlers to respond to specific events.

```python

# Connect to the websocket (Sync)
import threading

from agentmail import AgentMail

client = AgentMail(...)

with client.websockets.connect(...) as socket:
    # Iterate over the messages as they arrive
    for message in socket
        print(message)

    # Or, attach handlers to specific events
    socket.on(EventType.OPEN, lambda _: print("open"))
    socket.on(EventType.MESSAGE, lambda message: print("received message", message))
    socket.on(EventType.CLOSE, lambda _: print("close"))
    socket.on(EventType.ERROR, lambda error: print("error", error))


    # Start the listening loop in a background thread
    listener_thread = threading.Thread(target=socket.start_listening, daemon=True)
    listener_thread.start()
```

```python

# Connect to the websocket (Async)
import asyncio

from agentmail import AsyncAgentMail

client = AsyncAgentMail(...)

async with client.websockets.connect(...) as socket:
    # Iterate over the messages as they arrive
    async for message in socket
        print(message)

    # Or, attach handlers to specific events
    socket.on(EventType.OPEN, lambda _: print("open"))
    socket.on(EventType.MESSAGE, lambda message: print("received message", message))
    socket.on(EventType.CLOSE, lambda _: print("close"))
    socket.on(EventType.ERROR, lambda error: print("error", error))


    # Start listening for events in an asyncio task
    listen_task = asyncio.create_task(socket.start_listening())
```

