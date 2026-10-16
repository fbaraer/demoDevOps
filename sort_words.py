"""Sort the words of a string alphabetically."""

import sys


def sort_words(text: str, ignore_case: bool = True) -> str:
    """Return the words of `text` sorted alphabetically, joined by spaces.

    With ignore_case (the default), upper- and lowercase words sort
    together, e.g. "banana Apple cherry" -> "Apple banana cherry".
    """
    key = str.lower if ignore_case else None
    return " ".join(sorted(text.split(), key=key))


def main() -> None:
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter a string: ")
    print(sort_words(text))


if __name__ == "__main__":
    main()
