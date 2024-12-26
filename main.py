def calculate_blanks(length, runs_list):
    return length - (sum(runs_list) + (len(runs_list) - 1))

def process_input(length, runs):
    try:
        length = int(length)
        runs_list = [int(run) for run in runs.split()]
        return length, runs_list
    except ValueError:
        return None, None

def nonogram_logic(length, runs_list):
    blanks = calculate_blanks(length, runs_list)

    if blanks < 0:
        return "The row is overconstrained. Exiting."
    elif blanks == 0:
        return "Already a perfect guarantee!"
    elif sum(runs_list) + (len(runs_list) - 1) <= length / 2:
        return "No guarantees!"

    array_list = []
    for run in runs_list:
        array_list.append(['X'])
        array_list.append([1] * run)
    array_list.pop(0)  # removes initial gap
    array_list.append(['_'] * blanks)

    for i, run in enumerate(array_list):
        if i % 2 == 0:  # handles runs in the array_list
            if len(run) < blanks:
                array_list[i] = [0] * len(run)
            else:
                run[:blanks] = [0] * blanks

    full_list = []
    guarantee_count = 0
    for run in array_list:
        for num in run:
            if num == 1:
                full_list.append('⬛')
                guarantee_count += 1
            else:
                full_list.append('⬜')

    result = f"{guarantee_count} guaranteed slots found: \n\n{''.join(map(str, full_list))}"
    return result
