from solders.pubkey import Pubkey
from .networks import DEFAULT_NETWORK, get_program_id
from .types import Network

def get_config_address(network: Network = DEFAULT_NETWORK) -> Pubkey:
    program_id = get_program_id(network)
    pda, _ = Pubkey.find_program_address([b"config"], program_id)
    return pda
