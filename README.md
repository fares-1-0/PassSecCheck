# PassSecCheck

A command-line password auditing tool written in Python. It evaluates a password
in three stages: **strength**, **common-password check**, and **data-breach lookup**.

## Features

- Strength scoring from 0 to 5 with actionable recommendations
- Detection of commonly used weak passwords
- Breach lookup through the Have I Been Pwned (HIBP) API using k-anonymity,
  so the password itself never leaves your machine

## Project Structure

```
PassSecCheck/
├── main.py              # Entry point, runs all checks
├── strength_check.py    # Password strength scoring
├── display_result.py    # Formats and prints the result
├── check_common.py      # Common-passwords check
├── hash_pass.py         # HIBP breach check (k-anonymity)
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8+ (developed on Python 3.13)
- `requests`

```bash
python --version
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

## How It Works

### 1. Strength check (`strength_check.py`)

`check_password_length(password)` returns a tuple `(strength, recomm)`:

- `strength`: an integer score starting at 0
- `recomm`: a list of recommendations shown to the user

The score gains one point for each of the following:

| Criterion | Points |
|---|---|
| Length of at least 8 characters | +1 |
| Length of at least 12 characters (bonus) | +1 |
| Contains an uppercase letter | +1 |
| Contains a lowercase letter | +1 |
| Contains a digit | +1 |
| Contains a special character | +1 |

The score is capped at 5. Each criterion is tested with `re.search()` from the
built-in `re` (regular expression) module. When a criterion is not met, a matching
recommendation is appended to `recomm`.

### 2. Result display (`display_result.py`)

`display_result(strength, recomm)` maps the score to a level and an emoji, prints
them, then lists every recommendation.

| Score | Level |
|---|---|
| 0 | Very Weak 😱 |
| 1 | Narrow 🔴 |
| 2 | Weak 🟠 |
| 3 | Medium 🟡 |
| 4 | Strong 🟢 |
| 5 | Solid 💪 (Very Solid ⛓ when there are no recommendations) |

### 3. Common passwords (`check_common.py`)

A set of about 50 frequently used passwords, taken from well-known lists such as
`rockyou.txt` and `fasttrack.txt`. `check_common(password)` lowercases the input
before the lookup, because `Password` is just as dangerous as `password`.

### 4. Breach lookup (`hash_pass.py`)

HIBP is queried with **k-anonymity** so the full password or hash is never sent:

1. Hash the password with SHA-1 (the password is first encoded to bytes, since
   `hashlib` works on bytes).
2. Split the uppercase hex digest into a 5-character **prefix** and the remaining
   **suffix**.
3. Send only the prefix to `https://api.pwnedpasswords.com/range/<prefix>`.
4. The API returns every known hash suffix that shares that prefix, one per line,
   in the form `SUFFIX:COUNT`.
5. Read the response with `response.text.splitlines()`, then split each line on
   `:` into `hash_suffix` and `count`.
6. If `hash_suffix` equals our own suffix, the password was found in a breach
   `count` times.

**Illustrative example** (not a real digest): if the SHA-1 of a password is
`CBFDAC6008F9CAB4083784CBD1874F76618D2A97`, the prefix is `CBFDA` and the suffix
is the remaining 35 characters. Only `CBFDA` is sent to the API.

## Example Output

```
==================================================
Checking password..... wait.. 😪
==================================================

🟢 Strength: Strong  (4/5)
*** Tips you should follow to enhance your password ***
  - for more strong password add special cases 🔣

⚠️ Warning: this is one of the most common weak passwords!

🌐 Checking against the breach database...
🔴 Serious warning: this password appeared 1,234,567 times in real data breaches!
==================================================
```

## Security Notes

- The password is never sent over the network. Only the first 5 characters of its
  SHA-1 hash are transmitted.
- SHA-1 is used here only because the HIBP API requires it. It is not suitable for
  storing passwords.
- Avoid running the tool on a shared screen, since the password is typed in clear text.

## Development Log

1. Checked the Python version with `python --version` (Python 3.13).
2. Created the `PassSecCheck` directory and the first file, `strength_check.py`.
3. Imported the required libraries: `re`, `hashlib`, `requests`.
4. Built `check_password_length(password)` to score strength and collect recommendations.
5. Built `display_result(strength, recomm)` to print the level, emoji, and tips.
6. Built `check_common(password)` for the common-passwords check.
7. Built `check_pwned_password(password)` for the HIBP breach lookup.
8. Wired everything together in `main.py`.
