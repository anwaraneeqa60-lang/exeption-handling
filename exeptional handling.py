def check_age_and_parity():
    while True:
        try:
            age_input = input("Enter your age: ")
            age = int(age_input)
            if age < 0 or age > 120:
                print("Error: Please enter a realistic age between 0 and 120.")
                continue
            else:
                print(f"Valid age entered: {age}")
                if age % 2 == 0:
                    print(f"{age} is an even number.")
                else:
                    print(f"{age} is an odd number.")
                break
        except ValueError:
            print("Error: Invalid input. Please enter numeric digits.")
check_age_and_parity()