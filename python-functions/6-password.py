def validate_paasword(password):
    password = input("Please enter password")
    print("")

    if len(password) == 8 and  (password.isdigit()) and (password.islower()) ==True and (password.isspace()) == True and (password.isupper()) == True:
        print(True)
    else:
        print(False)

    