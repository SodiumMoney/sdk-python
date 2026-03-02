from sodium_sdk import get_payment_address, normalize_username

handle = "@blknoiz06"
print("Normalized:", normalize_username(handle))
print("Payment:", get_payment_address("twitter", handle))
