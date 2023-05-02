import random
import string


def generate_pid(prefix: str, string_len: int) -> str:
    """Generates a unqiue randoum pid

    Args:
        prefix (str): starting prefix
        string_len (int): len of pid to be generated

    Returns:
        str: pid in the format "pid_ad28asdnkadasd"
    """
    choices = string.ascii_letters + string.digits
    return prefix + "_" + "".join(random.choices(choices, k=string_len))
