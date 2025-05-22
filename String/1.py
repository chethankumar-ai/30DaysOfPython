def get(*args):
    out=()
    for i in args:
        if type(i) ==str:
            if i[0] in 'aeiou':
                out+=(i,)
    print(out)

put=get
put(1,2,'hello','aeiou')

