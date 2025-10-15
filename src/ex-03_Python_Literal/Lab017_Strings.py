name='This is a Big line'
print(type(name))
#name=name+1 this throws "can only concatenate str (not "int") to str"
name=name+str(1)
print(type(name))

#Concatenation within the strings is allowed.
fname='chandra'
lname='deepthi'
full_name=fname+lname#this prints chandradeepthi
full_name=fname+ " " + lname#this prints chandra deepthi
print(full_name)