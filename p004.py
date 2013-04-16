# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(integer):
	list = [];
	while(integer != 0):
		list.append(integer % 10)
		integer = int(integer/10)
	size = len(list)
	for x in range(0, int(size/2)):
		if(list[x] != list[-(x+1)]):
			return False
	return True

digits = 3
print("Finding largest palindrome made from products of " + str(digits) + " digit numbers")
print("...")
largestPalindrome = 0
for x in range(10**(digits-1),10**digits):
	for y in range(x,10**digits):
		if(isPalindrome(x*y) and x*y > largestPalindrome):
			largestPalindrome = x*y
print("Largest palindrome for products of " + str(digits) + " digit numbers: " + str(largestPalindrome))