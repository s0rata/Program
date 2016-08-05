def Num2Words(num):
	units = ['','one','two','three','four','five','six','seven','eight','nine']
	teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
	thousands = ['','thousand','million','billion','trillion','thousand trillion', 'million trillion', 'billion trillion', 'trillion trillion']
	word =[]

	numStr = str(num)
	numLen = len(numStr)
	group = (numLen+2)/3 
	numStr = numStr.zfill(group*3)

	if num == 0:
		return "zero"
	if numLen > 27:
		return "Error"
	else:
		for i in range(0,group*3,3):
			h,t,u = int(numStr[i]), int(numStr[i+1]), int(numStr[i+2])
			
			'''check on hundred digit'''
			if h>=1:
				word.append(units[h])
				word.append("hundred")

			'''check on ten digit'''
			if t>1:
				word.append(tens[t])
				if u>=1:
					word.append(units[u])
			elif t==1:
				if u>=1: word.append(teens[u])
				else: word.append(tens[u]) 
			else:
				word.append(units[u])

			'''check on thousand digit'''	
			if (group-1>=1) and ((h+t+u)>0):
				word.append(thousands[group-1] + ",")
				group -= 1

	return " ".join(word) + " dollar"


print "Convert number to words:"
x = int(input("$"))
print Num2Words(x)

