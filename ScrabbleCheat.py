import operator

scrabble = open('/Users/michaelchan/Desktop/words.txt','r')
word_list = []

for line in scrabble:
	scrabble = line.strip()
	word_list.append(scrabble)

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10, "_": 0} # set blank tile '_'

rack = raw_input("What letters do you have? >>> ")
if rack.isalpha == True: 
	rack = rack.lower() # convert to lower case

else:
	print 'please enter letters only'

# A function to take letters from the rack and see if they appear in word_list
valid_words = []

for word in word_list:
	
	possible_letter = True
	rack_letters= list(rack) # splits chars on rack into list
	for letter in word:
		if letter not in rack_letters:
			possible_letter = False
			break # stops checking letters in rack
		
		else: 
			rack_letters.remove(letter) # removes letter after being checked
		
	if possible_letter == True: # get the score for each word
		total = 0 
		for letter in word:
			total = total + scores[letter]
		valid_words.append([word, total])
		
valid_words.sort(reverse = True, key=operator.itemgetter(1))

for highscore in valid_words:
	print highscore
	
print scores["_"]	

	



