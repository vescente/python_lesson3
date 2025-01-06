# Function to convert input string to list of integers
def input_to_list(prompt):
    return list(map(int, input(prompt).split(',')))

# Get the first list from the user
list1 = input_to_list("Введите элементы 1-го списка: ")

# Get the second list from the user
list2 = input_to_list("Введите элементы 2-го списка: ")

# Remove elements from list1 that are present in list2
result_list = [item for item in list1 if item not in list2]

# Print the result
print("Результат:", result_list)