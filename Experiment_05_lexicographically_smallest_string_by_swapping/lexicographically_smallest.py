import string

def lexicographically_smallest(s: str) -> str:
    """Swap all occurrences of two characters (at most once) to get the smallest string."""
    best = s
    chars = sorted(set(s))
    for a in chars:
        for b in chars:
            if a == b:
                continue
            # swap all occurrences of a and b
            swapped = s.translate(str.maketrans(a + b, b + a))
            if swapped < best:
                best = swapped
    return best

if __name__ == "__main__":
    text = input("Enter a lowercase string: ")
    print("Lexicographically smallest:", lexicographically_smallest(text))
