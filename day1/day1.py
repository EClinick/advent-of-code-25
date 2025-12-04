# Safe dial logic
# If the dial is pointing at 0, and the rotation is left, the dial should point at 99.
# If the dial is pointing at 99, and the rotation is right, the dial should point at 0.
# The number of times the dial is left pointing at 0 after any rotation in the sequence is the password.
ans=0
# The dial starts at 50.
cur=50
def log(message):
    if LOGS:
        print(message)
# read the input file
with open('day1-input.txt', 'r') as file:
    for line in file:
        # split the line into direction and position
        direction = line[0]
        position = int(line[1:])
        if position > 100: 
            LOGS=True
        else:
            LOGS=False
        log(f"Direction: {direction} Position: {position}")
        if direction == 'L':
            temp=(cur-position)%100
            log(f"Dial is pointing at {cur} before rotation {line} temp is {temp}")
            if temp == 0:
                ans+=1
            cur=temp
        else:
            temp=(cur+position)%100
            log(f"Dial is pointing at {cur} before rotation {line} temp is {temp}")
            if temp == 0:
                ans+=1
            cur=temp
        log(f"Dial is pointing at {cur} after rotation {line}")
print(ans)

