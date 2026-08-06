import secrets
import string


def generate_random_code(length: int) -> str:
    generated_code = "".join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(length)
    )
    return generated_code.upper()
