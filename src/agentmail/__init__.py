# This file was auto-generated by Fern from our API Definition.

# isort: skip_file

from .types import (
    Ascending,
    Count,
    ErrorName,
    ErrorResponse,
    Labels,
    Limit,
    OrganizationId,
    PageToken,
    ValidationErrorResponse,
)
from .errors import IsTakenError, NotFoundError, ValidationError
from . import contexts, drafts, inboxes, messages, threads, webhooks
from .client import AgentMail, AsyncAgentMail
from .contexts import (
    Context,
    ContextData,
    ContextId,
    ContextIsEvent,
    ContextMetadata,
    ContextType,
    CreateContextRequest,
    ListContextsResponse,
)
from .drafts import (
    CreateDraftRequest,
    Draft,
    DraftAttachments,
    DraftBcc,
    DraftCc,
    DraftCreatedAt,
    DraftEventId,
    DraftHtml,
    DraftId,
    DraftInReplyTo,
    DraftItem,
    DraftLabels,
    DraftPreview,
    DraftReferences,
    DraftSubject,
    DraftText,
    DraftTo,
    DraftUpdatedAt,
    ListDraftsResponse,
)
from .environment import AgentMailEnvironment
from .messages import (
    Addresses,
    Attachment,
    AttachmentContent,
    AttachmentContentType,
    AttachmentFilename,
    AttachmentId,
    AttachmentInline,
    AttachmentSize,
    ListMessagesResponse,
    Message,
    MessageAttachments,
    MessageBcc,
    MessageCc,
    MessageEventId,
    MessageFrom,
    MessageHtml,
    MessageId,
    MessageInReplyTo,
    MessageItem,
    MessageLabels,
    MessagePreview,
    MessageReferences,
    MessageRejectedError,
    MessageSubject,
    MessageText,
    MessageTimestamp,
    MessageTo,
    ReplyToMessageRequest,
    SendAttachment,
    SendMessageAttachments,
    SendMessageBcc,
    SendMessageCc,
    SendMessageRequest,
    SendMessageResponse,
    SendMessageTo,
    UpdateMessageRequest,
)
from .threads import (
    ListThreadsResponse,
    Thread,
    ThreadAttachment,
    ThreadAttachments,
    ThreadEventId,
    ThreadId,
    ThreadItem,
    ThreadLabels,
    ThreadMessageCount,
    ThreadPreview,
    ThreadRecipients,
    ThreadSenders,
    ThreadSubject,
    ThreadTimestamp,
)
from .version import __version__
from .webhooks import (
    CreateWebhookRequest,
    EventId,
    EventType,
    EventTypes,
    InboxIds,
    ListWebhooksResponse,
    MessageReceivedPayload,
    SvixId,
    SvixSignature,
    SvixTimestamp,
    Url,
    Webhook,
    WebhookId,
)

__all__ = [
    "Addresses",
    "AgentMail",
    "AgentMailEnvironment",
    "Ascending",
    "AsyncAgentMail",
    "Attachment",
    "AttachmentContent",
    "AttachmentContentType",
    "AttachmentFilename",
    "AttachmentId",
    "AttachmentInline",
    "AttachmentSize",
    "Context",
    "ContextData",
    "ContextId",
    "ContextIsEvent",
    "ContextMetadata",
    "ContextType",
    "Count",
    "CreateContextRequest",
    "CreateDraftRequest",
    "CreateWebhookRequest",
    "Draft",
    "DraftAttachments",
    "DraftBcc",
    "DraftCc",
    "DraftCreatedAt",
    "DraftEventId",
    "DraftHtml",
    "DraftId",
    "DraftInReplyTo",
    "DraftItem",
    "DraftLabels",
    "DraftPreview",
    "DraftReferences",
    "DraftSubject",
    "DraftText",
    "DraftTo",
    "DraftUpdatedAt",
    "ErrorName",
    "ErrorResponse",
    "EventId",
    "EventType",
    "EventTypes",
    "InboxIds",
    "IsTakenError",
    "Labels",
    "Limit",
    "ListContextsResponse",
    "ListDraftsResponse",
    "ListMessagesResponse",
    "ListThreadsResponse",
    "ListWebhooksResponse",
    "Message",
    "MessageAttachments",
    "MessageBcc",
    "MessageCc",
    "MessageEventId",
    "MessageFrom",
    "MessageHtml",
    "MessageId",
    "MessageInReplyTo",
    "MessageItem",
    "MessageLabels",
    "MessagePreview",
    "MessageReceivedPayload",
    "MessageReferences",
    "MessageRejectedError",
    "MessageSubject",
    "MessageText",
    "MessageTimestamp",
    "MessageTo",
    "NotFoundError",
    "OrganizationId",
    "PageToken",
    "ReplyToMessageRequest",
    "SendAttachment",
    "SendMessageAttachments",
    "SendMessageBcc",
    "SendMessageCc",
    "SendMessageRequest",
    "SendMessageResponse",
    "SendMessageTo",
    "SvixId",
    "SvixSignature",
    "SvixTimestamp",
    "Thread",
    "ThreadAttachment",
    "ThreadAttachments",
    "ThreadEventId",
    "ThreadId",
    "ThreadItem",
    "ThreadLabels",
    "ThreadMessageCount",
    "ThreadPreview",
    "ThreadRecipients",
    "ThreadSenders",
    "ThreadSubject",
    "ThreadTimestamp",
    "UpdateMessageRequest",
    "Url",
    "ValidationError",
    "ValidationErrorResponse",
    "Webhook",
    "WebhookId",
    "__version__",
    "contexts",
    "drafts",
    "inboxes",
    "messages",
    "threads",
    "webhooks",
]
