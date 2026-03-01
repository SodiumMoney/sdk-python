def normalize_username(raw: str) -> str:
    return raw.strip().lstrip("@").lower()
