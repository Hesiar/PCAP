
''' Esta funcion usa return indistintamente'''
def fun_bad(n):
    for i in range(n):
        return i
    
''' Esta funcion usa yield'''
def fun_good(n):
    for i in range(n):
        yield i
        
''' for c in fun_bad(5):
        print(c)
'''
for c in fun_good(5):
    print(c)

