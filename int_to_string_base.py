# Converts given integer to string representation with the given "BASE"

def to_string(number, base):
	toCharacterString = "0123456789ABCDEF"

	if number < base:
		return toCharacterString[number]
	else:
		return to_string(number // base, base) + toCharacterString[number % base]

print to_string(1515, 16)