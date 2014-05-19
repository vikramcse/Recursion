# converts given string as a parameter and returns a new string that is the reverse of the old string

def reverse(s):
	length = len(s) - 1
	if length == 0:
		return s[0]
	else:
		return (s[length] + reverse(s[:-1]))

print(reverse("Hello"))