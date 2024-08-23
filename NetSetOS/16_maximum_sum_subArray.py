# Maximum Sum SubArray (Kadane's algorithm)

arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]

max_sum = 0
cur_sum = 0
for i in arr:
    cur_sum += i
    if cur_sum < 0:
        cur_sum = 0

    if cur_sum > max_sum:
        max_sum = cur_sum

print(f'Max sum: {max_sum}')



# From YouTube
def max_sum_subarray(arr):
    size=len(arr)
    curr_sum=0
    max_so_far=arr[0]
    st=0;end=0;poi=0
    for i in range(0,size):
        curr_sum=curr_sum+arr[i]

        if(max_so_far<curr_sum):
            max_so_far=curr_sum
            st=poi
            en=i
        if(curr_sum<0):
            curr_sum = 0
            poi=i+1

    print("Maximum sum Subarray is",max_so_far)
    print("Start Index of window is",st)
    print("End Index of window is",en)

max_sum_subarray(arr)