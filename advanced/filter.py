# filter is a function which is used to perform the operation on a given list of collection. So where is it is used to overcome the
# Map function The length of the input collection is equal to the length of the collection, whereas in filter collection based on the user requirement, it would be changed
# var =filter(filter_name,collection)
# Write a program to extract the complex values from heterogeneous tuple collection
com_val =lambda x: type(x) == complex 
tuple_collection = (1,3,4,5,3+5j,6+3j)
var = filter(com_val,tuple_collection)
print(list(var))