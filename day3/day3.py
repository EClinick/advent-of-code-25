def find_largest_number(numbers: list) -> int:
    '''
    This function finds the largest number in the list of numbers, and returns the index and the number.
    '''
    max_number = 0
    max_index = 0
    for i in range(len(numbers)):
        if int(numbers[i]) > max_number:
            max_number = int(numbers[i])
            max_index = i
    return max_index, max_number

total_sum=0
#Read the input file
with open('day3-input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # Split the line into a list of numbers
        numbers = list(line)
        # Find the largest number in the list
        idx, largest_number = find_largest_number(numbers)
        # Call largest_number function again but only starting from the idx + 1
        # If the idx is the last index, call find_largest_number w/o the largest number idx
        if idx == len(numbers) - 1:
            idx, largest_number_2 = find_largest_number(numbers[:idx])
            temp_sum=str(largest_number_2)+str(largest_number)
        else:
            idx, largest_number_2 = find_largest_number(numbers[idx + 1:])
            temp_sum= str(largest_number) + str(largest_number_2)
       
        total_sum += int(temp_sum)
print(total_sum)