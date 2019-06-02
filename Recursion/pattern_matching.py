def doesMatch(string, pattern):

def doesMatchRecursive(string, string_idx, pattern, pattern_idx):
	if string_idx == len(string):
		return True
	if pattern_idx == len(pattern):
		return False

	if pattern[pattern_idx] == "." && string[string_idx] == 


doesMatch("abcd", ".*cd")
doesMatch("abcdpodfor", "a*.")
doesMatch("abcddefgab", ".b*.")