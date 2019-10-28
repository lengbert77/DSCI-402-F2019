Assignment 1
#Solution to problem 1, Luke Engbert
temp=[1,[2,3,4],5,6,[7,8,9,10],11,12]
def flat(list_name):
    #base case where an empty list is flattened to an empty list
    if list_name==[]:
        return list_name
#this line tells us that if the first list element is a list, then we want
#to return the elements of 0 plus the rest of the list elements as a flattened list
    if isinstance(list_name[0],list):
        return flat(list_name[0]+list_name[1:])
#Next we can return all elements except the first one which we just flattened, 
#and add them to the new flattened element.The process is repeated recursively
    return list_name[:1]+flat(list_name[1:])
print(flat(temp))

temp1=[1,2,3,4]

#Solution to problem 2, Luke Engbert
#The base case would be where list_name = 0, powerset(list_name is also 0)
def powerset(list_name):
 #We need to iterate 2^nth times, because our powerset has n elements in it 
    n = len(list_name)
    #We can express this using binary terminology in list comprehension
    return [[list_name[x] for x in range(n) if i&1<<x] for i in range(2**n)]
print(powerset([1,2,3]))



#Solution to problem 3, Luke Engbert
def perm(lists): 
   #Base case tells us if the length is 1 or 0 the only results will be the same as the original list
    if len(lists) == 1:
     return [lists]

    permutated = [] # resulting list
    for a in lists:
       #Below we can go through the remaining elements and permutate them 
      remaining_elements = [x for x in lists if x != a]
      z = perm(remaining_elements) # permutations of sublist
      #next we can tack our first element of the list back on

      for i in z:
       permutated.append([a] + i)

    return permutated
print(perm([1,2,3]))