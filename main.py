def calc(input_value):
    decimal_value = input_value
    count = 0

    while decimal_value >= 1:
        decimal_value /= 10
        count += 1

    rounded_value = round(decimal_value, 1)

    for i in range(count):
        rounded_value *= 10

    print(int(rounded_value))

print('To end the program, type "quit"')
while True:
    input_value = input("Enter a whole number to be rounded: ")

    if input_value.lower() == "quit":
        break

    while True:
        try:
            int(input_value)
        except ValueError:
            print("Please enter a whole number")
        else:
            calc(int(input_value))
            break


