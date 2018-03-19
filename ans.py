'''
We can solve this by using modified version of binary search.

Time complexity of binary search in worst case is O(LogN) if size of list is N

How this algorithm is working?

Important Point: Since array is sorted and rotated so there will be one element which will
be smaller than its neighbours.

Using this technique , see the steps for modified version of binary search to solve your problem

list = [3, 4, 5, 1, 2]
We want to search element 1
left=0, right=4
--First handle base cases
--if (left == right)
----return left
--Run loop
--while(left<=right):
-----(1) if (right==right) => when you have reached termination condition
-----------return left
----(1) find the middle of the indexes:
--------mid=(left+right)//2
----(2)if (mid < right and l[mid] > l[mid + 1]): => This can be happen at one place only for rotation
            return mid + 1
----(3)elif(left < mid and l[mid] < l[mid-1]): => Same as above step(2)
        return mid
-----(4)  elif(l[mid] < l[right]): => search in left half
            right = mid -1
-----(5) search in right half
            left = mid + 1

To understand this clear please first learn binary search and after than learn
how to search minimum in rotated array.

Take pan and papper and analyse indexes and  algorithm

Sample Input:
[3, 2, 1, 0, -1, 1, 2]
[3, 2, 0, 2, 4]
[0]
[1,2,3]
[7,5,1]

Sample Output:
4
2
0
0
2
'''

#Your program start from below line

#function to search in minimum in rotated array
def find_min_in_valley(l):
    left=0
    right=len(l)-1
    if(left == right):
        return left
    while(left <= right):
        #final termination condition
        if (left == right):
            return left

        mid = (left + right) // 2
        #Below two condition is searching if middle is minimum of it's neighour
        if (mid < right and l[mid] > l[mid + 1]):
            return mid + 1
        elif(left < mid and l[mid] < l[mid-1]):
            return mid
        elif(l[mid] < l[right]):
            #Search in left half
            right = mid -1
        else:
            #Search in righ half
            left = mid + 1


#Calling above function and displaying response
print(find_min_in_valley([3, 2, 1, 0, -1, 1, 2]))
print(find_min_in_valley([3, 2, 0, 2, 4]))
print(find_min_in_valley([0]))
print(find_min_in_valley([1,2,3]))
print(find_min_in_valley([7,5,1]))
