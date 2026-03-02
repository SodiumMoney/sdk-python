from .normalize import normalize_username
from .types import Platform

def get_evm_salt(platform: Platform, username: str) -> str:
    norm = normalize_username(username)
    return f"{platform.lower()}:{norm}"
