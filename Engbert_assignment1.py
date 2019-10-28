Engbert_assignment1
#Solution to problem 1, Luke Engbert
def flat(list_name):
    #base case where an empty list is flattened to an empty list
    if list_name==[]:
        return list_name
#this next line tells us that if the first list element is a list, then we want
#to return the sub-elements of that first element (index 0) plus the rest of the list elements as a flattened list
    if isinstance(list_name[0],list):
        return flat(list_name[0]+list_name[1:])
#Next we can return all elements except the first one which we just flattened, 
#and add them to the new flattened element.The process is repeated recursively
    return list_name[:1]+flat(list_name[1:])



#Solution to problem 2, Luke Engbert
#The base case would be where list_name = 0, then subsequently the powerset(list_name is also 0)
def powerset(list_name):
 #We need to iterate 2^nth times, because our powerset has n elements in it 
    n = len(list_name)
    #We convert our index to binary representation with a bitwise operation and loop through
    #The & will compare the indexes and if it yields a result other than 0, that can go in the final resultit
    return [[list_name[x] for x in range(n) if i & 1<<x] for i in range(2**n)]




#Solution to problem 3, Luke Engbert
def perm(lists): 
   #Base case tells us if the length is 1 or 0 the only results will be the same as the original list
    if len(lists) == 1:
     return [lists]

    permutated = [] # resulting list
    for i in lists:
       #Below we can go through the remaining elements and permutate them 
      temp = [x for x in lists if x != i]
      temp2 = perm(temp) # permutations of sublist
      #next we can tack our first element of the list back on

      for j in temp2:
       permutated.append([i] + j)

    return permutated



import numpy as np

#problem 4:
    
def spiral (n, ending_corner):
    curr_num=n**2 -1
    matrix=np.negative(np.ones(n,n))
    starting_corner={1:(0,0),2:(0,n-1),3:(n-1,0),4:(n-1,n-1)}
    curr_pos=starting_corner(ending_corner)
    direction_steps=[(1,0),(0,1),(-1,0),(0,-1)]
    starting_directions={1:0,2:4,3:2,4:3}
    curr_direction=starting_directions(starting_corner)
    
    if curr_num >=0:
        row,col==curr-pos
        matrix[row,col]==curr_num
        
    if curr_pos not in matrix:
    #This is where I couldn't figure out anymore
