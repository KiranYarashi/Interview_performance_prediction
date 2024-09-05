def StringChallenge(str1, str2):
    char_count = {}

    # Count the occurrences of each character in str1
    for c in str1:
        if c.isalpha():
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1

    # Check if str2 can be constructed from str1
    for c in str2:
        if c in char_count and char_count[c] > 0:
            char_count[c] -= 1
        else:
            return "false"

    return "true"

if __name__ == "__main__":
    str1 = "cdore"
    str2 = "coder"

    print(StringChallenge(str1, str2))
