#print 'Loan Calculator'
#print '==============='
#P = float(input("Principal($): "))
#R = int(input('Annual Interest Rate(%): '))
#t = int(input('Term(months): '))
#T = int(input('Monthly: '))
#print '==============='


# Fuction to find interest in a day
def dayLoanCal(P,R):
	return ((P*(R/100))/360)

print dayLoanCal(12000,36)
	
