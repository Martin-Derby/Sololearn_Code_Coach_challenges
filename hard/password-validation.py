
#testing case
#word="@@!@h33"

word=input()
special = "!@#$%&*"

#define strength score and inc by 1 for every passed test. password acceptable if score total comes to 3

score = 0

#set criteria 1: 7 characters or more
if len(word) >= 7:
    score +=1

#criteria_2: count of special chars to be 2 or more
special_count=0
for char in word:
    if char in special:
        special_count +=1
    
if special_count >=2:
     score +=1
     
#criteria 3: count of numeric chars to be 2 or more
number_count=0
for char in word:
    if char.isnumeric()==True:
        number_count +=1   
           
if number_count  >=2:
     score +=1
     
#additional criteria to ensure password can never be scored acceptable if space in word
if" "in word:
   score-=1 
        
if score ==3:
    print ("Strong")
else:
    print ("Weak")
