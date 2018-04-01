A = [36, 5, -12, 9, -21]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88), ('Caven',61)]

def sortStudents(List):
	for x in List:
		return x[0]


L= sorted(L, key = sortStudents)
print(L)