#map function
# map function is used to perform the same operation on collection for each and every value in side the given collection
# var = map(fname,collection)
# var = map(fname,collection)
def sqr(num):
    return num*num
var =map(sqr,range(1,10))
print(list(var))
