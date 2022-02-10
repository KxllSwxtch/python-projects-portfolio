#!/usr/bin/env python
from time import sleep
from functools import reduce


def print_header():
    """
    Print title/welcome  message
    """
    print("================================================")
    print('Welcome to the Run Timing calculator')
    print("================================================\n")
    return


def get_average_runs(lst: list):
    """
    Get the average of the runs
    """
    return round(float(reduce(lambda a, b: a + b, lst) / len(lst)), 2)


def run_timing():
    """
    Calculates the average time for n run times
    """
    print_header()
    sleep(2)

    app_running = True
    output_list = []
    n_runs = 0

    while app_running:
        try:
            run_time = input('Enter 10 km run time: ')

            if run_time:
                n_runs += 1
                output_list.append(float(run_time))
                continue
            else:
                break
        except Exception as e:
            print("<Error... Please enter the floating point number or an integer>\n")

    avg_runs = get_average_runs(output_list)
    print(f'\nAverage of {avg_runs}, over {n_runs} runs.')
    return


def main():
    run_timing()


if __name__ == '__main__':
    main()
