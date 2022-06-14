# Using HeapMap
# Time Complexity: O(n). 
# One traversal of the array is needed, so the time complexity is linear.
# Auxiliary Space: O(n). 
# Since a hashmap requires linear space.

def findMajority(arr, size):
	m = {}
	for i in range(size):
		if arr[i] in m:
			m[arr[i]] += 1
		else:
			m[arr[i]] = 1
	count = 0
	for key in m:
		if m[key] > size / 2:
			count = 1
			print("Majority found :-",key)
			break
	if(count == 0):
		print("No Majority element")

# Driver code
arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]
n = len(arr)

# Function calling
findMajority(arr, n)

# This code is contributed by ankush_953




# Moore voting algorithm
# # Function to find the candidate for Majority
# # Complexity Analysis: 
# # Time Complexity: O(n). 
#     # As two traversal of the array is needed, so the time complexity is linear.
# # Auxiliary Space: O(1). 
#     # As no extra space is required.


# def findCandidate(A):
#     maj_index = 0
#     count = 1
#     for i in range(len(A)):
#         if A[maj_index] == A[i]:
#             count += 1
#         else:
#             count -= 1
#         if count == 0:
#             maj_index = i
#             count = 1
#     return A[maj_index]

# # Function to check if the candidate occurs more than n/2 times


# def isMajority(A, cand):
#     count = 0
#     for i in range(len(A)):
#         if A[i] == cand:
#             count += 1
#     if count > len(A)/2:
#         return True
#     else:
#         return False

# # Function to print Majority Element


# def printMajority(A):
#     # Find the candidate for Majority
#     cand = findCandidate(A)

#     # Print the candidate if it is Majority
#     if isMajority(A, cand) == True:
#         print(cand)
#     else:
#         print("No Majority Element")


# # Driver code
# A = [1, 3, 3, 1, 2]

# # Function call
# printMajority(A)


# -------- Brute Force Approach ------------
# # Python3 program to find Majority
# # element in an array

# # Function to find Majority
# # element in an array


# def findMajority(arr, n):

#     maxCount = 0
#     index = -1  # sentinels
#     for i in range(n):

#         count = 0
#         for j in range(n):

#             if(arr[i] == arr[j]):
#                 count += 1

#         # update maxCount if count of
#         # current element is greater
#         if(count > maxCount):

#             maxCount = count
#             index = i

#     # if maxCount is greater than n/2
#     # return the corresponding element
#     if (maxCount > n//2):
#         print(arr[index])

#     else:
#         print("No Majority Element")


# # Driver code
# if __name__ == "__main__":
#     arr = [1, 1, 2, 1, 3, 5, 1]
#     n = len(arr)

#     # Function calling
#     findMajority(arr, n)

# # This code is contributed
# # by ChitraNayal
