import random
eng = open('eng.txt')
und = open('underground.txt')
und = list(und)
for sentence in eng:
	list_of_sentences = sentence.split('.' or '!' or '?')
	for sen in list_of_sentences:
		sen = sen + random.choice(und)
		print(sen)
