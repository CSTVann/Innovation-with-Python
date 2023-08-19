from collections import Counter

# Given tuple
data = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)

# Count the occurrences of each element
counter = Counter(data)

# Find the most frequent element(s)
most_common = counter.most_common()

# Find the highest tied element (when there are multiple elements with the same maximum frequency)
max_frequency = most_common[0][1]
highest_tied_element = max(elem for elem, freq in most_common if freq == max_frequency)

print("The most frequent element:", highest_tied_element)
