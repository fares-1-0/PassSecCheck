import hashlib
import requests


def check_pwned_password(password):
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    # split the hash
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        return None, "⚠️  Can't reach the internet right now, try again later"

    if response.status_code != 200:
        return None, "⚠️  There was a problem contacting the API"

    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count), None

    return 0, None
