
def Remove(tuples):
	tuples = [t for t in tuples if t]
	return tuples

tuples = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),)]
print(Remove(tuples))
