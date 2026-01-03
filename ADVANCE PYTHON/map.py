num= [1,2,3,4,4,5,6,6,6,777,8,88,8]

def is_even(n):
    return n %2==0
    
evens = list(filter(is_even,num))
print(evens)

def update(n):
    return n *2
doubles =list(map(update,evens))
print (doubles)

doubles1 =list(map(lambda n:n*2,evens))
print(doubles1)