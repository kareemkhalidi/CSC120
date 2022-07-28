from short1_thing import *

def main():
    u = input()
    fooCall = foo(u)
    print(fooCall)
    u2 = input()
    u3 = input()
    barCall = bar(u, u2, u3)
    print(barCall)
    print(baz(fooCall, barCall))

main()