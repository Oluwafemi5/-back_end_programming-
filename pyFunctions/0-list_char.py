value = []
myList =[2,1,'This',4,'10',(3,2), 'fun']
value = [x for x in myList
  if isinstance(x,int)]
value.sort()
print(value)
        
