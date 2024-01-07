#!/usr/bin/python3

def text_indentation(text):
    """
    print a text

    Parameters:
    - text (int): string to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while (i < len(text)):
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print()
            i += 2
        else:
            print(text[i], end="")
            i += 1
