# tang_c02e08.py
#       A program to convert Gahrenheit temps to Celsius
# by: Linya Tang
def main():
	Fahrenheit = eval(input("What is the Fahrenheit temperature?"))
	Celsius = (Fahrenheit - 32)*5/9
	print ("The temperature is:", Celsius, "degree Celsius")

main()
