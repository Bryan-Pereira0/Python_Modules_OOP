import text_utils
choice_upper = input("Enter whether you want to A reverse your string or B capitalize your string!: ")
choice = choice_upper.lower()

if choice == "a":
    s = input("What set of string would you like to reverse?: ")
    text_utils.reverse_string(s)
elif choice == "b":
    s = input("What set of string would you like to capitalize?: ")
    text_utils.capitalize_string(s)