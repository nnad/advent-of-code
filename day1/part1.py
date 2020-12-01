# your code goes here# your code goes her
import sys

def main():
	elements = []
	num = 2020
	res = []
	
	for line in sys.stdin:
	    elements.append(int(line))
	    
	elements.sort()
	
	for i in range(0, len(elements)):
		for j in range (0, len(elements) - i - 1):
			if elements[len(elements) - i - 1] + elements[j] == num:
				res.append(elements[len(elements) - i - 1] * elements[j])
				
			if elements[len(elements) - i - 1] + elements[j] > num:
				break
			
	for el in res:
		print(el)
		
main()
