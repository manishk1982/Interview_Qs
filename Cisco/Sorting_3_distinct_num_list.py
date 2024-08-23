# Enter your code here. Read input from STDIN. Print output to STDOUT
cnt = input()
num_arr = input()

num_list = num_arr.split(" ")
# Check if count matches with the numbers present in the array
if int(cnt) != len(num_list):
    print(" ")
    exit()

# Get distinct numbers from array and sort
distinct_set = set(num_list)
sorted_distinct_set = sorted(distinct_set)

# Get occurance count for each distinct number
count_dict = {}
for num in distinct_set:
    count_dict[num] = num_list.count(num)
    
# Prepare the sorted array, based on occcurance count
sorted_list = []
for num in sorted_distinct_set:
    sorted_list.extend([num] * count_dict[num])

print(" ".join(sorted_list))