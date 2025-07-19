while True:
    number_input = int(input("Enter:"))

    if number_input == 0:
        break

    if number_input % 2 == 0:
        print(f"Even {number_input}")
    else: 
        print(f"Odd {number_input}")