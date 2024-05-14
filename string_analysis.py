def count_char(user_input):
    str_input = user_input.replace(" ", "")
    str_count = len(str_input)
    print("the total number of characters in a String without whitespace:", str_count)
    return str_count
    
def count_vowels_and_consonants(user_input):
    user_input_lower = user_input.lower()
    type_casting = list(user_input_lower)
    count_v = 0
    count_c = 0
    
    for i in type_casting:
        try:
            if i in ['a', 'e', 'i', 'o', 'u']:
                count_v += 1
            else:
                if i.isalpha(): 
                    count_c += 1
        except:
            print("enter a valid input")
            return -1
    
    print("the number of vowels:", count_v)
    print("the number of consonants:", count_c)

def is_palindrome(user_input):
    user_input_lower = user_input.lower().replace(" ", "")
    return user_input_lower == user_input_lower[::-1]

def contains_alphanumeric(user_input):
    for i in user_input:
        return i.isalnum()

def get_case(user_input):
    return user_input.upper(), user_input.lower()

def check_input(user_input):
    count_char(user_input)
    count_vowels_and_consonants(user_input)

    if is_palindrome(user_input):
        print("The input is a palindrome.")
    else:
        print("The input is not a palindrome.")

    if contains_alphanumeric(user_input):
        print("The input contains alphanumeric characters.")
    else:
        print("The input does not contain alphanumeric characters.")

    upper_case, lower_case = get_case(user_input)
    print("Upper case:", upper_case)
    print("Lower case:", lower_case)

print("Welcome to string analysis program! \n")
user_input = input("Enter a string: ")
check_input(user_input)
