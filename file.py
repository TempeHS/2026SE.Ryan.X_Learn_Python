def main():
	num1 = int(input('What is num 1? '))
	num2 = int(input('What is num 2? '))
	operator = input('What is the operator?')
	if operator == '+':
		UIoutput = num1 + num2
	elif operator == '-':
		UIoutput = num1 - num2
	elif operator == '*':
		UIoutput = num1 * num2
	elif operator == '/':
		UIoutput = num1 / num2
	else:
		print('Operator not known')
	
	print(UIoutput)


main()




