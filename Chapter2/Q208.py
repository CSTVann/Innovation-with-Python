from collections import Counter

given_tuples = [(), (1), [], 'abc', (), (), (1,), ('a'), ('a', 'b'), ((),)]

filtered_tuples = [item for item in given_tuples if not isinstance(item, str) and not (isinstance(item, list) and len(item) == 0)]

counter = Counter(filtered_tuples)
most_common = counter.most_common()

max_frequency = most_common[0][1]
highest_tied_elements = [elem for elem, freq in most_common if freq == max_frequency]

print("The most frequent elements:", highest_tied_elements)
