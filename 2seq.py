def get_unique_elements(input_string):
    # Split the input string by the possible delimiters
    if ',' in input_string:
        elements = input_string.split(',')
    elif ';' in input_string:
        elements = input_string.split(';')
    elif '/' in input_string:
        elements = input_string.split('/')
    else:
        print("Invalid delimiter. Please use either ',', ';' or '/'.")
        return []

    # Convert elements to integers
    elements = [int(e) for e in elements]

    # Create a dictionary to count occurrences of each element
    element_count = {}
    for element in elements:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    # Create a list of unique elements
    unique_elements = [element for element, count in element_count.items() if count == 1]

    return unique_elements

# Get input from the user
input_string = input("Введите элементы списка через запятую, точку с запятой или слэш: ")

# Get the unique elements
unique_elements = get_unique_elements(input_string)

# Print the result
print("Результат:", unique_elements)