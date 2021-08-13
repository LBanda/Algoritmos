def cadenap(cadena):
    pila = []
    parentesis = {'{': '}', '(': ')', '[': ']'}

    for c in cadena:
        if c in parentesis:
            pila.append(c)
        elif len(pila) == 0 or c != parentesis[pila.pop()]:
            return False
    
    return len(pila) == 0


print(cadenap('()'))
print(cadenap('()()()()()()()()()'))
print(cadenap('([])[]()'))
print(cadenap(')'))
print(cadenap('()['))
print(cadenap('(([))]'))
print(cadenap('((((((((((((((((((((((((((((((((('))