# Get the number of elements from the user
num_elements = int(input("Введите количество элементов: "))

# Initialize an empty list to store the elements
elements = []

# Loop to get each element from the user
for i in range(num_elements):
    element = int(input(f"Введите {i + 1} элемент: "))
    elements.append(element)

# Sort the list in ascending order
elements.sort()

# Print the sorted list
print("Вывод:", elements)