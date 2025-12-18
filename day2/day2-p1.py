# Product ID ranges
# The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).
# 11-22 has two invalid IDs, 11 and 22.
# 95-115 has one invalid ID, 99.
# 998-1012 has one invalid ID, 1010.
# 1188511880-1188511890 has one invalid ID, 1188511885.
# 222220-222224 has one invalid ID, 222222.
# 1698522-1698528 contains no invalid IDs.
# 446443-446449 has one invalid ID, 446446.
# 38593856-38593862 has one invalid ID, 38593859.
# The rest of the ranges contain no invalid IDs.

def split_string_in_half(s: str):
    mid= len(s)//2
    return s[:mid], s[mid:]

sum=0

# Read the input file to get ranges limits
with open('day2-input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        ranges = line.split(',')
        
# Now since we have an array of ranges, we need to check if any ID in ranges[i] appears twice!
for i in range(len(ranges)):
    # Before iterating through the range, we need to clean up each ranges[i] to split the - into two numbers
    # range_start = str
    # range_end = str
    range_start, range_end = ranges[i].split('-')
    # iterate thru each individual range
    for j in range(int(range_start), int(range_end)):
        # Splitting each number into two halves
        # Stringifying the number to split it into two halves
        half1, half2 = split_string_in_half(str(j))
        # If both halves are the same, then the number is invalid
        if half1 == half2:
            print(f"Invalid number: {j}")
            sum += int(j)

print(sum)
