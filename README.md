# Sololearn Code Coach Challenges
Collection of my solutions in Python to the 'Code Coach' challenges on Sololearn (https://www.sololearn.com/)

## Easy

### [Halloween Candy](https://github.com/martin-kerr/sololearn-code-coach-challenges/blob/main/easy/halloween-candy.py)

You go trick or treating with a friend and all but three of the houses that you visit are giving out candy. One house that you visit is giving out toothbrushes and two houses are giving out dollar bills. 

Task:
Given the input of the total number of houses that you visited, what is the percentage chance that one random item pulled from your bag is a dollar bill? 

Input Format: 
An integer (>=3) representing the total number of houses that you visited. 

Output Format:
A percentage value rounded up to the nearest whole number.

Sample Input:
4

Sample Output: 
50

## Medium

### [Pig Latin](https://github.com/martin-kerr/sololearn-code-coach-challenges/blob/main/medium/pig-latin.py)
You have two friends who are speaking Pig Latin to each other! Pig Latin is the same words in the same order except that you take the first letter of each word and put it on the end, then you add 'ay' to the end of that. ("road" = "oadray") 

Task:
Your task is to take a sentence in English and turn it into the same sentence in Pig Latin! 

Input Format:
A string of the sentence in English that you need to translate into Pig Latin. (no punctuation or capitalization)

Output Format:
A string of the same sentence in Pig Latin.

Sample Input:
"nevermind youve got them"

Sample Output:
"evermindnay ouveyay otgay hemtay"

## Hard
### [New Driver's License](https://github.com/martin-kerr/sololearn-code-coach-challenges/blob/main/hard/new-drivers-license.py) 
You have to get a new driver's license and you show up at the office at the same time as 4 other people. The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now, and they can each see one customer at a time. How long will it take for you to walk out of the office with your new license?

Task: 
Given everyone's name that showed up at the same time, determine how long it will take to get your new license.

Input Format: 
Your input will be a string of your name, then an integer of the number of available agents, and lastly a string of the other four names separated by spaces.

Output Format: 
You will output an integer of the number of minutes that it will take to get your license.

Sample Input:
'Eric'
2
'Adam Caroline Rebecca Frank'

Sample Output: 
40

### [Password Validation](https://github.com/martin-kerr/sololearn-code-coach-challenges/tree/main/hard/password-validation.py)

You're interviewing to join a security team. They want to see you build a password evaluator for your technical interview to validate the input.

Task: 
Write a program that takes in a string as input and evaluates it as a valid password. The password is valid if it has at a minimum 2 numbers, 2 of the following special characters ('!', '@', '#', '$', '%', '&', '*'), and a length of at least 7 characters.
If the password passes the check, output 'Strong', else output 'Weak'.

Input Format:
A string representing the password to evaluate.

Output Format:
A string that says 'Strong' if the input meets the requirements, or 'Weak', if not.

Sample Input: 
Hello@$World19

Sample Output: 
Strong
