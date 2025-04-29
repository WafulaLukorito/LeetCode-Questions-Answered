from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    char_count = Counter(t)  # Frequency of chars in t
    required = len(char_count)  # Unique characters in t
    left = 0
    min_len = float("inf")
    min_start = 0
    formed = 0
    window_counts = {}

    for right, char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in char_count and window_counts[char] == char_count[char]:
            formed += 1

        while formed == required:
            # Update minimum window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left

            # Try shrinking from left
            window_counts[s[left]] -= 1
            if s[left] in char_count and window_counts[s[left]] < char_count[s[left]]:
                formed -= 1
            left += 1

    return s[min_start:min_start + min_len] if min_len != float("inf") else ""

# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))  # Output: "BANC"