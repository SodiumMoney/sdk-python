from solders.pubkey import Pubkey
from .networks import DEFAULT_NETWORK, get_program_id
from .normalize import normalize_username
from .types import Network, Platform

def _slot_bytes(slot: int) -> bytes:
    return int(slot).to_bytes(8, "little")

def get_config_address(network: Network = DEFAULT_NETWORK) -> Pubkey:
    program_id = get_program_id(network)
    pda, _ = Pubkey.find_program_address([b"config"], program_id)
    return pda

def get_payment_address(
    platform: Platform,
    username: str,
    network: Network = DEFAULT_NETWORK,
) -> Pubkey:
    norm = normalize_username(username)
    program_id = get_program_id(network)
    seeds = [b"escrow", platform.lower().encode(), norm.encode()]
    pda, _ = Pubkey.find_program_address(seeds, program_id)
    return pda

def get_identity_address(
    platform: Platform,
    username: str,
    network: Network = DEFAULT_NETWORK,
) -> Pubkey:
    norm = normalize_username(username)
    program_id = get_program_id(network)
    seeds = [b"identity", platform.lower().encode(), norm.encode()]
    pda, _ = Pubkey.find_program_address(seeds, program_id)
    return pda

def get_used_proof_address(proof_hash: bytes, network: Network = DEFAULT_NETWORK) -> Pubkey:
    program_id = get_program_id(network)
    pda, _ = Pubkey.find_program_address([b"used_proof", proof_hash], program_id)
    return pda

def get_link_request_address(
    username_hash: bytes,
    wallet: Pubkey,
    slot: int,
    network: Network = DEFAULT_NETWORK,
) -> Pubkey:
    program_id = get_program_id(network)
    seeds = [b"link_req", username_hash, bytes(wallet), _slot_bytes(slot)]
    pda, _ = Pubkey.find_program_address(seeds, program_id)
    return pda

def get_telegram_link_request_address(
    username_hash: bytes,
    wallet: Pubkey,
    slot: int,
    network: Network = DEFAULT_NETWORK,
) -> Pubkey:
    program_id = get_program_id(network)
    seeds = [b"tg_link_req", username_hash, bytes(wallet), _slot_bytes(slot)]
    pda, _ = Pubkey.find_program_address(seeds, program_id)
    return pda
