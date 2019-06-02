# Sonder phone interview 1
def firstNRepeatingWord(line, count):
	words = line.split()

	dictionary = dict()

	for word in words:
		if word in dictionary.keys():
			dictionary[word] += 1
			if dictionary[word] == count:
				return word
		else:
			dictionary[word] = 1

line = "dictionary is the dictionary of the dictionary"
result = firstNRepeatingWord(line, 2)
print(result)