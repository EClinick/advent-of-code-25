# Safe dial logic
# If the dial is pointing at 0, and the rotation is left, the dial should point at 99.
# If the dial is pointing at 99, and the rotation is right, the dial should point at 0.
# The number of times the dial is left pointing at 0 after any rotation in the sequence is the password.

# NOW IN PART TWO, WE NEED TO COUNT THE NUMBER OF TIMES THE DIAL POINTS AT 0 DURING A ROTATION OR AT THE END OF A ROTATION.
ans = 0
# The dial starts at 50.
cur = 50

# Count each time the dial points at 0 while rotating (including the end).
with open('day1-input.txt', 'r') as file:
    for raw in file:
        line = raw.strip()
        direction = line[0]
        position = int(line[1:])

        full_rotations = position // 100
        remaining = position % 100

        if direction == 'R':
            distance_to_zero = (100 - cur) if cur > 0 else 100
            ans += full_rotations
            if remaining >= distance_to_zero:
                ans += 1
            cur = (cur + position) % 100
        else:
            distance_to_zero = cur if cur > 0 else 100
            ans += full_rotations
            if remaining >= distance_to_zero:
                ans += 1
            cur = (cur - position) % 100

print(ans)

