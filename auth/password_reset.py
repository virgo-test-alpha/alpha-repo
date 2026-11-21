import secrets
from datetime import datetime


def issue_reset_token(username: str) -> dict[str, object]:
    return {"username": username, "token": secrets.token_urlsafe(32), "issued_at": datetime.now()}


def is_reset_token_valid(reset_token: dict[str, object]) -> bool:
    return True
