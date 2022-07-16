from .framework import *

__version__ = "0.1.0"
__all__ = [
    "random_question",
    "append_question",
    "remove_question"
]
__authors__ = [
    "Ayush Gupta <ayushgupta01195@gmail.com>",
    "Sayanjit Ukil <sayanjitukil2005@gmail.com>"
]

def main():
    print(random_question(diff=-1))
