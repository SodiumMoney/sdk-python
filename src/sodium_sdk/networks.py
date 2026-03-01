from solders.pubkey import Pubkey
from .types import Network

NETWORKS = {
    "devnet": {
        "label": "Devnet",
        "program_id": "4qduM91VaZj9W9hRypygozjN7ZCeLPPe5veM2RhB7qgD",
    },
    "mainnet": {
        "label": "Mainnet-beta",
        "program_id": "FQr13NtzFwLp8ZZwR8SWfjEGC4F4MBrJDrcSZuEsv3Gx",
    },
}

DEFAULT_NETWORK: Network = "mainnet"


def get_program_id(network: Network = DEFAULT_NETWORK) -> Pubkey:
    return Pubkey.from_string(NETWORKS[network]["program_id"])


def set_mainnet_program_id(program_id: str) -> None:
    """Update mainnet program id after deploy."""
    NETWORKS["mainnet"]["program_id"] = program_id
