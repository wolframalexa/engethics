# takes a text file and returns some simple data about the frequency of each word in the file

import re

frequency = {}

textfile = open('descriptions.txt', 'r')
output = open('wordfreqs.txt', 'w')
text = textfile.read().lower()

# find all word frequencies
pattern = re.findall(r'\b[a-z]{2,15}\b', text)

for word in pattern:
	count = frequency.get(word,0)
	frequency[word] = count + 1

# sort by frequency
sorted_freq = {}
frequency_list = sorted(frequency, key=frequency.get)

for word in frequency_list:
	sorted_freq[word] = frequency[word]


# remove common English words
to_remove = ["the", "and", "or", "this", "for", "is", "in", "to", "of", "will", "from", "by", "can", "about", \
		"that", "not", "many", "these", "yet", "much", "out", "between", "they", "also", \
		"you", "both", "us", "at", "as", "on", "it", "with", "are", "an"]

for word in to_remove:
	sorted_freq.pop(word)

print(sorted_freq)
for key in sorted_freq:
	result = key + " " +  str(sorted_freq[key]) + "\n"
	output.write(result)

textfile.close()
output.close()
