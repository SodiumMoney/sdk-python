from solders.pubkey import Pubkey
from .networks import DEFAULT_NETWORK, get_program_id
from .normalize import normalize_username
from .types import Network, Platform

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
