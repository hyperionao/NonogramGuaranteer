def calculate_blanks(length, runs_list):
    return length - (sum(runs_list) + (len(runs_list) - 1))

def process_input():
    try:
        length = int(input("Give the row/column length you are dealing with!\n"))
        runs = input("Give the runs as shown above/aside the row/column! Format should be as a continuous string: 4 5\n")
        runs_list = [int(run) for run in runs.split()]
        return length, runs_list
    except ValueError:
        print("Invalid input. Please try again.")
        exit()

length, runs_list = process_input()
blanks = calculate_blanks(length, runs_list)

if blanks < 0:
    print("The row is overconstrained. Exiting.")
    exit()
elif blanks == 0:
    print("Already a perfect guarantee!\n")
elif sum(runs_list) + 1 * (len(runs_list) - 1) <= length / 2: #gaps+runs only reach half or is less than half, no guarantees possible! 
    print("No guarantees!")

#logic for gaps + 'runs'
array_list = []
for run in runs_list:
    array_list.append(['X'])
    array_list.append([1] * run)
array_list.pop(0)  # removes initial gap
array_list.append(['_'] * blanks)

for i, run in enumerate(array_list):
    if i % 2 == 0: #strictly handles runs in the array_list
        if len(run) < blanks:
            array_list[i] = [0] * len(run)
        else:
            run[:blanks] = [0] * blanks

full_list = []
guarantee_count = 0
for run in array_list:
    for num in run:
        if num == 1:
            full_list.append(1)
            guarantee_count += 1
        else:
            full_list.append('?')

print(f"{guarantee_count} guaranteed slots found: \n")
print(full_list)
