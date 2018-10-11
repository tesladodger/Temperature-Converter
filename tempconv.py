#Temperature Converter
#Input: Temperature
#Output: Temperature in other units
#Use: Converts temperatures and makes you feel bad about it
#André Martins, 2018

from tempformulas import celcius, kelvin, frankenstein

print(' _____________________________________')
print('|                                     |')
print('| Temperature Converter (on steroids) |')
print('|_____________________________________|')
repeater = 1
while (repeater==True) :
	print('Convert from:')
	print('C - Celcius')
	print('K - Kelvin')
	print('F - Fahrenheit')
	print('T - Terminate')
	from_var = str(input('8===D  '))
	from_var = from_var.upper();
	print(from_var)	
	if (from_var=='C') :
		temp_c = str(input('\nTemperature in Celcius: '))
		celcius(temp_c)
	elif (from_var=='K') :
		temp_k = str(input('\nTemperature in Kelvin: '))
		kelvin(temp_k)
	elif (from_var=='F') :
		temp_f = str(input('\nTemperature in Fahrenheit: '))
		frankenstein(temp_f)
	elif (from_var=='T') :
		print('\n\nGoodbye')
		repeater = 0;
		break
	else :
		print('\nYou must be dumb...\n')
