# your code goes here# your code goes her
import sys

def main():
	elements = []
	num = 2020
	res = set()
	
	for line in sys.stdin:
	    #new_list = [int(elem) for elem in line.split()]
	    elements.append(int(line))
	    
	elements.sort()
	
	for i in range(0, len(elements)):
		for j in range (0, len(elements) - i - 1):
			for k in range (0, len(elements) - i - 1):
				if elements[len(elements) - i - 1] + elements[j] > num or elements[len(elements) - i - 1] + elements[j]  + elements[k] > num or elements[len(elements) - i - 1] + elements[k] > num:
					break
				if elements[len(elements) - i - 1] + elements[j] + elements[k] == num:
					res.add(elements[len(elements) - i - 1] * elements[j] * elements[k])
			
	for el in res:
		print(el)
		
main()
