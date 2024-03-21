# PROBLEM: 
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given  scores. 
# Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains n. The second line contains an array A[] of n integers each separated by a space.

#SOLUTION:
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    

    arr = list(set(arr))
    arr.sort(reverse=False)
    print(arr[-2] if len(arr) > 1 else arr[0])
