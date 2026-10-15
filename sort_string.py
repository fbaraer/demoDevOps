"""Sort the characters of a string alphabetically."""

import sys


def sort_string(text: str, ignore_case: bool = True) -> str:
    """Return the characters of `text` sorted alphabetically.

    With ignore_case (the default), upper- and lowercase letters sort
    together, e.g. "Banana" -> "aaaBnn".
    """
    key = str.lower if ignore_case else None
    return "".join(sorted(text, key=key))


def main() -> None:
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter a string: ")
    print(sort_string(text))


if __name__ == "__main__":
    main()
