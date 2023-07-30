def fibonacci_sequence(n):
    n= input("Please enter a number")
    if  n in {0,1}:
         return n
    return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)
        