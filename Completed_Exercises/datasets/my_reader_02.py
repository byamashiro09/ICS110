#import modules
import re

# open and read the file
fin = open('113809of.fic').readlines()

# compile a pattern
pattern = re.compile(r'^([^aeiou][aeiou])+', re.DOTALL)
counter = 0

# iterate over the words
for line in fin:
	word = line.strip()
	#print(word)
	if len(word) % 2 == 0:
		#print(word)
		matchobj = pattern.search(word)
		counter += 1
print(counter)


# compare the word to pattern

#increment my counter

# present result