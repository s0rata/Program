def Num2Words(num):
	units = ['','one','two','three','four','five','six','seven','eight','nine']
	teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
	thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']
	word =[]

	numStr = ('%.2f'%num).split('.')
	dollar, cent = numStr[0], numStr[1]
	dLen= len(dollar)
	dGroup= (dLen+2)/3
	dollar = dollar.zfill(dGroup*3)
	ct, cu = int(cent[0]), int(cent[1])

	if num == 0 or 0 < num < 1:
		word.append("zero")
	else:
		for i in range(0,dGroup*3,3):
			dh,dt,du = int(dollar[i]), int(dollar[i+1]), int(dollar[i+2])
			
			if dh>=1:
				word.append(units[dh])
				word.append("hundred")

			if dt>1:
				word.append(tens[dt]+"-")
				if du>=1:
					word.append("\b"+units[du])
			elif dt==1:
				if du>=1: word.append(teens[du])
				else: word.append(tens[du]) 
			else:
				word.append(units[du])

			if ((dGroup-1>=1) and (dh+dt+du)>0):
				word.append(thousands[dGroup-1] + ",")
				dGroup -= 1
	
	word.append("dollar and")
	if cent == "00":
		word.append('zero')
	elif ct>1:
		word.append(tens[ct])
		if cu>=1:
			word.append(units[ct])
	elif ct==1:
		if cu>=1: word.append(teens[cu])
		else: word.append(tens[cu])
	else:
		word.append(units[cu])
	word.append('cent')

	return " ".join(word)
	

print "Convert number to words:"
while True:
	try:
		x = float(input("$"))
		print Num2Words(x)
		break
	except Exception:
		print ("INVALID NUMBER")
