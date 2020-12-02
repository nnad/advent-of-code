# your code goes here
# your code goes here
# your code goes here
import sys

def main():
	dict = {}
	num1 = ''
	num2 = ''
	res = []
	letter = []
	flag = False
	alfa = False
	range_num = []
	
	for line in sys.stdin:
		
	    for el in line:
	    	print(el)
	    	if el.isdigit() :
	    		num1 += el
	    		continue
	    	if el == '-':
	    		num2 = num1
	    		num1 = ''
	    		continue
	    	if el == ' ' and flag == False and alpha != True:
	    		flag = True
	    		range_num.append([int(num1), int(num2)])
	    		continue
	    	
	    	if el.isalpha() and flag and alpha != True:
	    		alpha = True
	    		letter.append(el)
	    		continue
	    		
	    	if flag and alpha and dict[el]:
	    		dict[el] += 1
	    	else: dcit[el] = 0
	    	
	    alpha = False
	    flag = False
	    num1 = ''
	    num2 = '' 
	    
	for i in range (0, len(letter)):
		if dict.get(letter[i]) >=  range_num[i][0] or dict.get(letter[i]) <=  range_num[i][1]:
			res.append(True)
		else: res.append(False)
		
	return res
		
main()
