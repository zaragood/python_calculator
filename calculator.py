from calculator_art import logo
print(logo)

import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Addition function
def addition(num1, num2):
    """takes in two parametere a, b."""
    sum = num1 + num2
    return(sum)

#substraction function
def subtraction(num1, num2):
    """takes in two parametere a, b."""
    differences = num1 - num2
    return(differences)

#division function
def division(num1, num2):
    """takes in two parametere a, b."""
    exponent = num1 / num2
    return(exponent)

#multiplication function
def multiplication(num1, num2):
    """takes in two parametere a, b."""
    product = num1 * num2
    return(product)


#dictionary containing our operation as key and our function as value
function = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

#Recursive function to make our program run again from the top if the user wants to start a new calculation
def recursive_call():
    continue_calculation = True
    
    #while our condition is true we want to prompt the user for inputs 
    while continue_calculation:
        first_number = float(input("what is the first number? "))
        
        #Displays the available symbol to the user to choose from
        for symbol in function:
            print(symbol)
        
        operation = input("Pick an operation: ")
        
        #checking if the user entered the valide operation that is in our dictionary
        if operation not in function:
            print("Invalide operation :( Try again!")
            #starting afresh by calling our recursive function so the user can enster a valide operation
            recursive_call()
            
        #for valide operation prompt the user for next number
        second_number = float(input("What is the next number? "))

        #get the key for that operation and use to call the corresponding function
        calculation_function = function[operation]
        first_result = calculation_function(first_number, second_number)

        #prints the full calculation
        print(f"{first_number} {operation} {second_number} = {first_result}")
    
        #set flag to determine if the loop runs again or not
        continue_again = True
        
        while continue_again: 
            #Ask the user if they would like to continue calculation with previoUs result or start a new calculation
            user_choice = input(f"Type 'y' to continue calculating with {first_result}, or type 'n' to restart: ")        
            if user_choice == "y":
                operation = input("Pick another operation: ")
                third_number = float(input("What is the next number? "))
                calculation_function = function[operation]
                second_result = calculation_function(first_result, third_number)
                first_result = second_result
                
                print(f"{first_result} {operation} {third_number} = {second_result}")
            
            #if users choice is n then clear the termimal and run the vode again using recursive call
            elif user_choice == "n":
                continue_again = False
                clear_terminal()
                print("Restarting calculator")
                recursive_call()
            else:
                print("Invalide response :( Try again!")
                continue_again = True
recursive_call()
                