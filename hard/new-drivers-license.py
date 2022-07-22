"""
New Driver's License 

You have to get a new driver's license
 and you show up at the office at the
 same time as 4 other people. The office
 says that they will see everyone in
 alphabetical order and it takes 20
 minutes for them to process each new
 license. All of the agents are available
 now, and they can each see one customer
 at a time. How long will it take for you
 to walk out of the office with your new
 license?

Task 
Given everyone's name that showed up at
 the same time, determine how long it
 will take to get your new license.

Input Format 
Your input will be a string of your name,
 then an integer of the number of 
available agents, and lastly a string of 
the other four names separated by spaces.

Output Format 
You will output an integer of the number
 of minutes that it will take to get your
 license.

Sample Input
'Eric'
2
'Adam Caroline Rebecca Frank'

Sample Output 
40

"""

#input
my_name=input()
agents=int(input())
other_names=(input()).split()

#test inputs
#my_name="Martin"
#agents=3
#other_names="F G H I K L N O P Q".split()

#make list of all names inc mine
all_names=list(my_name.split()) + other_names 

# sort names list by alphabet
all_names.sort()

#find my place in queue
queue_place =all_names.index(my_name)+1

#calculate my group number
if queue_place % agents ==0:
    group= int(queue_place/agents)
else:
    group= int(queue_place/agents)+1
    
#calculate wait_time 
wait_time=group*20

print (wait_time)
