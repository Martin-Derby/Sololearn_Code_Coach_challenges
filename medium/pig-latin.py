'''
Input Format :A string of the sentence in English that you need to translate into Pig Latin. (no punctuation or capitalization) 

take the first letter of each word and put it on the end, then you add 'ay' to the end of that. ("road" = "oadray") 
'''

#take input string of english
eng =str(input())

#set pig latin translation as empty string to add output words to
pig =""

#make list of words in input phrase
englist=eng.split()

##loop through words in input phrase
for word in englist:
 #make list of letters in word(s)
 word = list(word) 
 
 #copy first letter of each word to end
 word.append(word[0])
 
 #remove first letter of each word
 word.remove(word[0])
 
 #add 'ay' to  word
 word.extend(['a','y'])
 
 #join letters to make new word a string
 word ="".join(word)
 
 #add new word plus a space to output string 
 pig +=(word + " ")
 ##end of loop

#remove space from end of output string then print it 
pig =pig[:-1]
print(pig)
