#Repayment of principal and interest is based on different bank policy. 

#P is Principal
#R is annual interest rate
#r is annual interest rate in decimal
#t is periods of loaning
#T is monthly
#I is total interest
#p is monthly payment
#f is frequency of payment: "Monthly, Bimonthly, Quarterly, Semi-Annually, Annually"

def loanCal(P, r, t, f):
	p = P / (t / f)
	I = 0.0
	for i in range(0, t, f):
		I = I + (P * (r * f) / 12)
		P = P - p 
	return I
#end loanCal() 

PaymentFrequency = {1 : "Monthly(12/yr)", 2 : 'Bimonthly(6/yr)', 3 : 'Quarterly(4/yr)', 4 : 'Semi-Annually(2/yr)', 5 : 'Annually(1/yr)'}
print 'Loan Calculator'
print '==============='
while True:

	print "Payment frequency:"
	print "------------------"
	for i, j in PaymentFrequency.items():
		print '%d: %s' %(i, j)
	print "-------------------"
	try:
		T = int(input("Payment frequency:\n> "))
		P = float(input("Principal($):\n> "))
		R = float(input("Annual Interest Rate(%):\n> "))
		t = int(input("Loan term in months:\n> "))
		r = R / 100

		if T == 1: f = 12
		elif T == 2: f = 6
		elif T == 3: f = 4
		elif T == 4: f = 2
		elif T == 5: f = 1
		else: 
			print "Invalid choice"
		print "Your %s payment is: $" %PaymentFrequency[T], loanCal(P, r, t, f)
		# print loanCal(P, r, t, f)
	except Exception:
		print "Value Error"
	print "\n"