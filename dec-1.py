def getPassword():
    ans = 0
    currentDial = 50
    file = open('inputs/dec-1')
    for line in file:
        direction = 1 if line[0] == 'R' else -1
        steps = int(line[1:])
        tempCD = currentDial if direction == 1 else ((100 - currentDial) if currentDial != 0 else 0)
        numRotationsPast0 = ((tempCD + steps) // 100)
        ans += numRotationsPast0
        newDial = (currentDial + (direction * steps)) % 100
        if numRotationsPast0 > 0:
            print(f'Rotated past 0 between {currentDial} and {newDial} {numRotationsPast0} times when going {steps} steps in the {direction} direction!')
        currentDial = newDial
    return ans

print(getPassword())

# The edge case I didn't see was when we had landed on a 0 in a previous turn to not make the 100 - currentDial equal to just 100. That makes it count double.
