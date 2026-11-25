def length_of_string(s: str) -> int:
    """Return the number of characters in the input string."""
    count = 0
    for ch in s:
        count += 1
    return count

if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Length of the string:", length_of_string(text))
