# Given tuple
data = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)

# Count the occurrences of each element using a dictionary
element_count = {}
for element in data:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

# Find the most frequent element(s)
most_common = []
max_frequency = 0
for element, frequency in element_count.items():
    if frequency > max_frequency:
        most_common = [element]
        max_frequency = frequency
    elif frequency == max_frequency:
        most_common.append(element)

# Find the highest tied element (when there are multiple elements with the same maximum frequency)
highest_tied_element = max(most_common)

print("The most frequent element:", highest_tied_element)
