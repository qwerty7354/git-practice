def has_unique_chars(s: str) -> bool:
    return len(set(s)) == len(s)


print(has_unique_chars("abcdef"))
print(has_unique_chars("hello"))