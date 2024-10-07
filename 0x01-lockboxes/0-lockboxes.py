def canUnlockAll(boxes):
    unlocked = [False] * len(boxes)  # Track if a box is unlocked
    unlocked[0] = True  # Box 0 is always unlocked
    keys = [0]  # Start with the key to box 0

    while keys:
        current_key = keys.pop()  # Take the current key
        for key in boxes[current_key]:  # Go through the keys in this box
            if key < len(boxes) and not unlocked[key]:  # Check if the box can be unlocked[key]:
                unlocked[key] = True
                keys.append(key)  # Add the key to unlock the next box

    return all(unlocked)  # Return True if all boxes are unlocked
