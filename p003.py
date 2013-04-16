# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def isPrime(integer):
	for x in range(2,integer):
		if integer % x == 0:
			return False
	return True

target = 600851475143
newTarget = target
largestPrimeFactor = 1
i = 2

print("Finding largest prime factor of target: " + str(target))
while i <= newTarget:
	if(isPrime(i) and newTarget % i == 0):
		newTarget /= i
		largestPrimeFactor = i
		print(str(i) + " is a prime factor of target, new target: " + str(newTarget))
	i += 1
		
print("Largest prime factor of " + str(target) + ": " + str(largestPrimeFactor))