def imprimir_funcion(args, fun):
    for x in args:
        print('f(',x,')=', fun(x), sep='')
        
#La funcion lambda nos ahorra definir una funcion que solo se usa 1 vez.
def funcion_cuadrado(x):
    return x**2

# f(x) = x^2

imprimir_funcion([x for x in range(-2, 3)], funcion_cuadrado)

#codigo mas simple
imprimir_funcion([x for x in range(-2, 3)], lambda x: x**2)