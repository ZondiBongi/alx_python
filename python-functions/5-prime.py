user_input = input("Please enter a number",())
def is_prime(number):
    if number ==1:
        return False
    elif number ==2:
        return True
    else:
        for x in range(2,number):
            if(number % x ==0):
                return False
        return True    
    
