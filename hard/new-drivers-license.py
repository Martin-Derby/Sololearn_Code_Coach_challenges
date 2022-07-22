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
