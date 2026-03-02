from .normalize import normalize_username
from .networks import NETWORKS, DEFAULT_NETWORK, get_program_id, set_mainnet_program_id
from .addresses import (
    get_config_address,
    get_payment_address,
    get_identity_address,
    get_used_proof_address,
    get_link_request_address,
    get_telegram_link_request_address,
)
from .evm import get_evm_salt
from .types import Platform, Network, SUPPORTED_PLATFORMS

__all__ = [
    "normalize_username",
    "NETWORKS",
    "DEFAULT_NETWORK",
    "get_program_id",
    "set_mainnet_program_id",
    "get_config_address",
    "get_payment_address",
    "get_identity_address",
    "get_used_proof_address",
    "get_link_request_address",
    "get_telegram_link_request_address",
    "get_evm_salt",
    "Platform",
    "Network",
    "SUPPORTED_PLATFORMS",
]
