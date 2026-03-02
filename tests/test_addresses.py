from sodium_sdk.addresses import (
    get_config_address,
    get_payment_address,
    get_identity_address,
)

def test_config_address():
    assert str(get_config_address("mainnet")) == "3WYJaf1ocPSbQAMjFhka5t8iusdH11Atw6FcxeuVYsTw"

def test_payment_blknoiz06():
    assert str(get_payment_address("twitter", "@blknoiz06")) == "HPT9k5YWkKNQcZGewGmABjRu8A5Bnem6VsBmNrNsSgyd"

def test_payment_alias():
    a = str(get_payment_address("twitter", "@blknoiz06"))
    b = str(get_payment_address("twitter", "@BLKNOIZ06"))
    assert a == b

def test_payment_unicode():
    assert str(get_payment_address("twitter", "Ansem 🐂🀄️")) == "k7JEBhVHHWLrNdhJ87cPbpgJr98kDVQuqUb5HsVKW7S"

def test_identity_blknoiz06():
    assert str(get_identity_address("twitter", "@blknoiz06")) == "T4gKVCxkB3c6pERaS67fLBgMyg1FpGmjeNcrGvbuLY1"

def test_identity_unicode():
    assert str(get_identity_address("twitter", "Ansem 🐂🀄️")) == "83McthMovBoPHgXPVGsif61zkCZNEE7tmypdNkxh1cv5"
