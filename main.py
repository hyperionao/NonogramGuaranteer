length = input("Give the row/column length you are dealing with!\n")
runs = input("Give the runs as shown above/aside the row/column! Format should be as a continuous string: 4 5\n")

length = int(length)
runs_list = runs.split()
runs_list = [int(run) for run in runs_list]

gap_array = ['X']

#base case: runs with gaps already add up to length of row
if sum(runs_list) + 1*(len(runs_list)-1) == length:
    print("Already a perfect guarantee!\n")
    
#base case: runs will never have a guarantee slot
if sum(runs_list) + 1*(len(runs_list)-1) <= length/2:
    print("No guarantees!")

#calculating blanks 
blanks = length - (sum(runs_list) + 1*(len(runs_list)-1))

#all other cases
array_list = []
for run in runs_list:
    array_list.append(gap_array)
    array_list.append([1]*run)
array_list.pop(0)

array_list.append(['_']*blanks)

for i, run in enumerate(array_list):
    if i%2 == 0:
        if len(run) < blanks:
            blank_ge_run = [0]*len(run)
            array_list[i] = blank_ge_run
        else:
            blank_run = [0]*blanks
            run[:blanks] = blank_run
        
print(array_list)

full_list = []
for run in array_list:
    full_list = full_list + run
    
    
guarantee_count = 0
for i, num in enumerate(full_list):
    if num != 1:
        full_list[i] = '?'
    else: 
        guarantee_count+=1
        
print(f'''{guarantee_count} guaranteed slots found: \n''')
print(full_list)