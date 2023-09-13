myList = [2, 1, "this", 4, "10", (3, 2), "fun", "python"]

def new_list(value):
    result = []
    if value == "Number":
       result = [x for x in myList
                if isinstance(x,int)]
    elif  value == "String":
          result = [x for  x in myList
                if isinstance(x,str)] 
    elif value == "Alphabets":
           result =[x for x in myList
             if isinstance(x,str) and len(x) >=3 ]  
    else:
        result =print ("Invalid Option")
    return  result
   
print(new_list("Number"))
print (new_list("String"))
print(new_list("Alphabets"))
print (new_list("Sango"))
