#!/usr/bin/python3
"""
Contains the definition of 'text_indentation' function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    lines = []
    line = ""
    for c in text:
        line += c
        if c in [".", "?", ":"]:
            lines.append(line)
            line = ""
    lines.append(line)
    for idx in range(len(lines)):
        print(lines[idx].strip(), end="\n\n" if idx != len(lines) - 1 else "")
