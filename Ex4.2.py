var = input("Enter some data:")

try:
	if int(var) > 5:
		print('Yes')
	else:
		print('No')
except:
	try:
		if float(var) > 5.0:
			print('Yes')
		else:
			print('No')
	except:
		try:
			str(var)
			print('String')
		except:
			print('Other')
