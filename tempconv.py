#Temperature Converter
#Input: Temperature
#Output: Temperature in another unit
#Use: Converts temperatures and makes you feel bad about it
#Andre Martins, 10-2018

def celcius(temp_c) :
	try:
		temp_c = float(temp_c);
	except ValueError:
		print('\n\nNot a number, idiot...\n\n')
		return;
	in_k = temp_c + 273.15;
	if (in_k < 0) :
		print('\n\nNice try, fag...\n\n')
		return;
	in_f = temp_c*(9/5)+32;
	print('\n_______________________\n')
	print("In Kelvin:      ", in_k)
	print("In Fahrenheit:  ", in_f)
	print('_______________________\n')
	return;

def kelvin(temp_k) :
	try:
		temp_k = float(temp_k);
	except ValueError:
		print('\n\nNot a number, jackass...\n\n')
		return;
	if (temp_k < 0) :
		print('\n\nNice try, fag...\n\n')
		return;
	in_c = temp_k - 273.15;
	in_f = temp_k*(9/5)-459.67;
	print('\n_______________________\n')
	print("In Celcius:     ", in_c)
	print("In Fahrenheit:  ", in_f)
	print('_______________________\n')
	return;

def frankenstein(temp_f) :
	try:
		temp_f = float(temp_f);
	except ValueError:
		print('\n\nNot a number, asshole\n\n')
		return;
	in_c = (temp_f - 32)*(5/9);
	in_k = (temp_f + 459.67) * (5/9);
	if (in_k < 0) :
		print('\n\nNice try, fag...\n\n')
		return;
	print('\n_______________________\n')
	print("In Celcius:  ", in_c) 
	print("In Kelvin:   ", in_k)
	print('_______________________\n')


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
		print('Goodbye')
		repeater = 0;
		break
	else :
		print('\nYou must be dumb...\n')
