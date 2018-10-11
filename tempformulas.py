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