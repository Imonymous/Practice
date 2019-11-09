#!/usr/bin/env python3

# Mock 8

def check_for_all_stars(pattern, pattern_idx):
    i = pattern_idx
    while i < len(pattern):
        if pattern[i] != "*":
            return False
        i += 1
    return True

def doesMatch(string, pattern):
    return doesMatchRecursive(string, 0, pattern, 0)

def doesMatchRecursive(string, string_idx, pattern, pattern_idx):
    if string_idx == len(string) and pattern_idx == len(pattern):
        return True
    if pattern_idx == len(pattern):
        return False
    if string_idx == len(string):
        return check_for_all_stars(pattern, pattern_idx)
    if pattern[pattern_idx] == "." or string[string_idx] == pattern[pattern_idx]:
        return doesMatchRecursive(string, string_idx+1, pattern, pattern_idx+1)
    if pattern[pattern_idx] == "*":
        return doesMatchRecursive(string, string_idx+1, pattern, pattern_idx) or doesMatchRecursive(string, string_idx+1, pattern, pattern_idx+1)

    return False

print(doesMatch("abcd", ".*cd"))
print(doesMatch("abcdpodfor", "a*."))
print(doesMatch("abcddefgab", ".b*."))
