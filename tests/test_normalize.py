from sodium_sdk.normalize import normalize_username

def test_strip_at_and_lower():
    assert normalize_username("@blknoiz06") == "blknoiz06"
    assert normalize_username("@BLKNOIZ06") == "blknoiz06"

def test_unicode_display_name():
    assert normalize_username("Ansem 🐂🀄️") == "ansem 🐂🀄️"
