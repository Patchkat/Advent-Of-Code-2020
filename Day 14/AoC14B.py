# A function to apply the bitmask to the memory address
def apply_mask(num, mask):
    mask = [c for c in mask]
    # Add 0s to make the number the same length as the mask
    num = ''.join(['0' for x in range(36 - len(num))]) + num
    num = [c for c in num]
    # Apply the mask
    for pos, value in enumerate(mask):
        if value == "X" or value == '1':
            num[pos] = mask[pos]
    # Remove all trailing 0s
    num_x_positions = []
    for x in range(len(num)):
        if num[x] == 'X' or num[x] == '1':
            num = num[x:]
            break
    # Store the position of all floating bits in the mask
    for x in range(len(num)):
        if num[x] == 'X':
            num_x_positions.append(x)

    nums = []
    nums = create_numbers(num, num_x_positions, 0, nums)
    
    return [x for x in nums if x != None]

# A recursive function for creating all possible memory locations 
# based on the floating bits in the mask
def create_numbers(numbers, positions, pos, nums):
    # Check if the end of the mask has been reached
    if pos == len(positions):
        return ''.join([c for c in numbers])
    # Try both 0 and 1 in the given position
    for x in range(2):
        numbers[positions[pos]] = str(x)
        nums.append(create_numbers(numbers, positions, pos+1, nums))
    # Break out of the function once all possibilities have been created
    if pos == 0:
        return nums

# The actual code runner
if __name__ == "__main__":
    # Input all of the lines from the file
    f = [x.rstrip('\n').split(' ') for x in open('masks.txt').readlines()]
    bits = {}
    mask = ''
    # Split the information apart
    for x in f:
        # Find the mask
        if x[0] == 'mask':
            mask = x[2]
        # Apply the mask to each line
        else:
            # Get the memory address and convert it into binary
            memory_address = int(int(x[0].split('[')[1][:-1]))
            binary_value = bin(memory_address).replace("0b","")
            masks = apply_mask(binary_value, mask)
            for y in masks:
                bits[int(y, 2)] = int(x[2])
    # Add up all of the values and print it out
    total = 0
    for x in bits.values():
        if x != 0:
            total += x
    print(total)