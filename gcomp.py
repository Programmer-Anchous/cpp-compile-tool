import os
from sys import platform

from random import randrange


if "linux" not in platform.lower():
    print("Unsopported OS")


def generate_str_num():
    result = ""
    for _ in range(20):
        result += str(randrange(10))
    return result


def comparator(filename):
    extensions = (".cpp", ".hpp", ".h")
    for extension in extensions:
        if filename.endswith(extension):
            return True
    return False


directories = tuple(os.walk("."))[0][-1]
directories = list(filter(comparator, directories))

object_file_name = f"object_file_{generate_str_num()}"

command = f"clear; g++ {' '.join(directories)} -o {object_file_name}; ./{object_file_name}; rm {object_file_name}"

os.system(command)
