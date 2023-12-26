def longest_substring(s):
    # Initialize a set to store the unique characters in the current substring
    unique_chars = set()
    # Initialize two pointers: start and end of the current substring
    start = 0
    end = 0
    # Initialize a variable to store the length of the longest substring
    max_len = 0
    # Iterate over the string using the end pointer
    while end < len(s):
        # If the character at the end pointer is not already in the set, add it
        if s[end] not in unique_chars:
            unique_chars.add(s[end])
            # Update the length of the longest substring if necessary
            max_len = max(max_len, end - start + 1)
            end += 1
        else:
            unique_chars.remove(s[start])
            start += 1
    return max_len

print(longest_substring('abcabcbb'))
