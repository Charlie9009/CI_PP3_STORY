

def validate_warrior_path0():
    while True:
        try:
            pathChoice = int(input("1\n"))
            if pathChoice != 1:
                raise ValueError("You can only use the number 1 here")
        except ValueError as e:
            print(f"Invalid input: {e}, please try again")
            continue
        return True


def validate_user_input():
    while True:
        try:
            pathChoice = int(input("1, 2\n"))
            if pathChoice < 1 or pathChoice > 2:
                raise ValueError("You can only use numbers 1 and 2 here")
        except ValueError as e:
            print(f"Invalid input: {e}, please try again")
            continue
        return True
