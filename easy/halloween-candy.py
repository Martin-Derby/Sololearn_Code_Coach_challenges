# function to round up any number to next whole number
def round_up(x):
    '''
    if 'round' rounds down then add 1 to the rounded number
    if 'round' rounds up or number is whole already then return the rounded number
    '''
    if round(x)==int(x) and (x-int(x))!=0: 
        return(round(x)+1)
    else:
        return(round(x)) 

#main code
houses = int(input())
if houses>=3:
         dollar=2
         chance = ((dollar/houses)*100)
         print (round_up(chance))
        
