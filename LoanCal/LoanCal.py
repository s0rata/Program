#Repayment of principal and interest is based on different bank policy. 

#P is Principal
#R is annual interest rate
#r is annual interest rate in decimal
#t is periods of loaning
#T is monthly
#I is total interest
#p is monthly payment
#f is frequency of payment: "Monthly, Bimonthly, Quarterly, Semi-Annually, Annually"

def loanCal(P,r,t,f):
	p = P / (t/f)
	I=0.0
	for i in range(0,t,f):
		I= I+(P*(r*f)/12)
		P= P- p 
	return I
#end loanCal() 

print 'Loan Calculator'
print '==============='

P = float(input("Principal($): "))
R = float(input("Annual Interest Rate(%): "))
t = int(input("Loan term in months: "))
print "Payment frequency:"
print "------------------"
print "1. Monthly (12/yr)"
print "2. Bimonthly (6/yr)"
print "3. Quarterly (4/yr)"
print "4. Semi-Annually (2/yr)"
print "5. Annually (1/yr)"
print "-------------------"
T = int(input("Payment frequency: "))
	
r = R/100
if T == 1: f = 12
elif T == 2: f = 6
elif T == 3: f = 4
elif T == 4: f = 2
elif T == 5: f = 1
else: 
	print "Invalid choice"

print loanCal(P,r,t,f)