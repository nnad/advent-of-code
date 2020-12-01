import sys

def main():
	list_of_lists = []
	num = 2020
	res = []
	
	for line in sys.stdin:
	    #new_list = [int(elem) for elem in line.split()]
	    list_of_lists.append(int(line))
	    
	list_of_lists.sort()
	
	for i in range(0, len(list_of_lists)):
		for j in range (0, i):
			if list_of_lists[i] + list_of_lists[j] == num:
				res.append(list_of_lists[i] * list_of_lists[j])
				print(list_of_lists[i])
				print(list_of_lists[j])
				
			if list_of_lists[i] + list_of_lists[j] > num:
				break
			
	for el in res:
		print(el)
		
main()
