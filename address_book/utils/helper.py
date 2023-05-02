import random
import string


def generate_pid(prefix: str, string_len: int) -> str:
    choices = string.ascii_letters + string.digits
    return prefix + "_" + "".join(random.choices(choices, k=string_len))
