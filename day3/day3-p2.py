def find_joltage(numbers: list, pick: int = 12) -> int:
    """
    Build the largest possible joltage by turning on exactly `pick` batteries.
    Greedy stack approach (remove k digits to maximize the remaining number).
    """
    n = len(numbers)
    k = n - pick  # how many digits we are allowed to remove

    stack = []  # digits we plan to keep (this replaces line_sum)

    for i in range(n):
        curr = int(numbers[i])

        # Pop while we still can delete and curr improves the number earlier
        # stack[-1] is how we track the previous number
        while k > 0 and len(stack) > 0 and stack[-1] < curr:
            removed = stack.pop()
            k -= 1
            # print(
            #     "i=", i,
            #     " curr=", curr,
            #     " -> popping ", removed,
            #     " remaining k=", k,
            #     " stack=", stack
            # )

        stack.append(curr)
        # print("i=", i, " pushed ", curr, " k=", k, " stack=", stack)

    # If deletions remain, trim from the end
    if k > 0:
        # print("Trimming from end, k=", k)
        stack = stack[:-k]

    # Take exactly `pick` digits
    result_digits = stack[:pick]
    result_str = ""
    for d in result_digits:
        result_str += str(d)

    # print("final stack=", stack)
    # print("result_digits=", result_digits, " result_str=", result_str)

    return int(result_str)


# test= ['2', '3', '4', '2', '3', '4', '2', '3', '4', '2', '3', '4', '2', '7', '8']
# print(find_joltage(test))

total_sum=0

# read the input file
with open('day3-input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        # Split the line into a list of numbers
        numbers = list(line)
        total_sum += find_joltage(numbers)
print(total_sum)