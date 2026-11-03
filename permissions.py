"""Role-based permissions for editing reusable Discord support replies."""
from __future__ import annotations

from collections.abc import Iterable

# Discord role IDs authorised to create and edit quick replies.
# Plugin Developer and Contributor respectively.
REPLY_EDITOR_ROLE_IDS = frozenset({
    1563858250456236032,
    1563864910285373502,
})


def has_reply_editor_role(role_ids: Iterable[int]) -> bool:
    """Only members holding one of the explicitly permitted roles can edit replies."""
    return not REPLY_EDITOR_ROLE_IDS.isdisjoint(role_ids)
