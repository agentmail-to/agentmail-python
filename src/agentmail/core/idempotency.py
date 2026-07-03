# This file is a hand-written AgentMail patch (NOT Fern-generated). It is pinned
# in .fernignore so Fern regeneration cannot clobber it.
#
# Purpose: auto-mint an `Idempotency-Key` header for send endpoints so that the
# HttpClient's internal auto-retries (429/5xx/timeouts) all carry the SAME key.
# The AgentMail API makes SENDS idempotent via this header: a retry with the same
# key returns the original message (no duplicate email); reuse with a different
# payload is a 409. Minting once per logical call (before the retry loop) keeps
# every attempt idempotent.

import re
import typing
import uuid

IDEMPOTENCY_KEY_HEADER = "Idempotency-Key"

# The 5 POST send endpoints, matched on the path suffix (after the /v0 prefix and
# ignoring any query string). {segment} is a single non-slash path segment.
#
# Anchored to the END of the path ($) so that ONLY the exact final segments
# /send, /reply, /reply-all, /forward match. This deliberately does NOT match the
# create-draft endpoints (/messages/{seg}/draft-reply, /draft-reply-all,
# /draft-forward), which end in different segments.
_SEND_PATH_REGEX = re.compile(
    r"(?:^|/)(?:"
    r"messages/send"
    r"|messages/[^/]+/reply"
    r"|messages/[^/]+/reply-all"
    r"|messages/[^/]+/forward"
    r"|drafts/[^/]+/send"
    r")$"
)


def _is_send_path(path: typing.Optional[str]) -> bool:
    if not path:
        return False
    # Ignore any query string / fragment; strip a trailing slash before anchoring.
    clean = path.split("?", 1)[0].split("#", 1)[0].rstrip("/")
    return _SEND_PATH_REGEX.search(clean) is not None


def _has_idempotency_key(headers: typing.Optional[typing.Mapping[str, typing.Any]]) -> bool:
    if not headers:
        return False
    return any(k.lower() == IDEMPOTENCY_KEY_HEADER.lower() for k in headers.keys())


def maybe_mint_idempotency_key(
    *,
    method: str,
    path: typing.Optional[str],
    headers: typing.Optional[typing.Dict[str, typing.Any]],
    additional_headers: typing.Optional[typing.Mapping[str, typing.Any]],
) -> typing.Optional[typing.Dict[str, typing.Any]]:
    """Return a headers dict carrying an auto-minted Idempotency-Key, or None.

    Mints (UUID4) only when: the method is POST, the path is one of the send
    endpoints, and no caller-supplied `Idempotency-Key` header is already present
    (case-insensitive) in either `headers` or the request_options
    `additional_headers`. Returns a NEW dict (never mutates the caller's) that the
    request method should thread through its retry recursion so all attempts share
    the same key. Returns None when nothing should change.
    """
    if method.upper() != "POST":
        return None
    if not _is_send_path(path):
        return None
    if _has_idempotency_key(headers) or _has_idempotency_key(additional_headers):
        return None

    minted = dict(headers) if headers else {}
    minted[IDEMPOTENCY_KEY_HEADER] = str(uuid.uuid4())
    return minted
