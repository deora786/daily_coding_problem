import time
'''
Auther: Sachin Nath Deroa


This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


Bonus: Can you do this in one pass?



The problem statment:
Given a list of numbers 'lst' and a number 'k'
finding id the list contains any such pairs which sume to 'k'

Following solution is an O(n) solution using Hash set

'''

#print("-----------STARTING---------")

start_time = time.time()
# list of numers
num_list = [2,23,4,13,34,5,22,9,1]
# given number to check whetner list contains any two which sum to it
k = 25
# creating a compliment set for lookup
compl_set = set()

# function to check if such pair exist
def does_add(num_list, num_k):
	for i in num_list:
		# the compliment of number i
		compl_num = num_k-i
		if compl_num in compl_set:
			# if list has the compliment, Hurrey!!! we found the pair
			return True
		else:
			# add the number in set
			compl_set.add(i)
	return False

print (does_add(num_list, k))


#print("----------FINISHED----------")
print("--- %s seconds ---" % (time.time() - start_time))
