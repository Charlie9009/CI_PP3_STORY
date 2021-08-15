

def validate_user_input():
    while True:
        try:
            pathChoice = int(input("1\n"))
            if pathChoice != 1:
                raise ValueError("You can only put the number 1 here.")
        except ValueError as e:
            print(f"Invalid input: {e}, please try again")
            continue
        return True

