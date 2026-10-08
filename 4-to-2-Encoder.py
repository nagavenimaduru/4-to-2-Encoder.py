def encoder_4_to_2(inputs):
    if inputs == [1, 0, 0, 0]:
        return [0, 0]
    elif inputs == [0, 1, 0, 0]:
        return [0, 1]
    elif inputs == [0, 0, 1, 0]:
        return [1, 0]
    elif inputs == [0, 0, 0, 1]:
        return [1, 1]
    else:
        return None


print("4-to-2 Encoder")
print("----------------")

inputs = []

for i in range(4):
    value = int(input(f"Enter D{i} (0 or 1): "))

    if value not in [0, 1]:
        print("Invalid input! Please enter only 0 or 1.")
        exit()

    inputs.append(value)

output = encoder_4_to_2(inputs)

if output is not None:
    print("\nInputs:")
    for i, value in enumerate(inputs):
        print(f"D{i} = {value}")

    print(f"\nEncoded Output:")
    print(f"A = {output[0]}")
    print(f"B = {output[1]}")
else:
    print("\nInvalid input!")
    print("Exactly one input must be HIGH (1).")
