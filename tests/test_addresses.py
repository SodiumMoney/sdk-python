from sodium_sdk.addresses import get_config_address

def test_config_address():
    assert str(get_config_address("mainnet")) == "3WYJaf1ocPSbQAMjFhka5t8iusdH11Atw6FcxeuVYsTw"
