list_of_numbers = [1, 2, 3, 4, 5]
def calculate(numbers):
	if len(numbers) == 1:
		return numbers[0]
	else:
		return numbers[0] + calculate(numbers[1:])

print calculate(list_of_numbers)