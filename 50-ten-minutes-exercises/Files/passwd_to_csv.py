#!/usr/bin/env python
import os
import csv


def passwd_to_csv(input_file: str, output_file: str):
    """
    @param input_file: First file that contains password-style to read from
    @param output_file: Second file to write output into
    @return: writes to a csv file in a format: 
        USERNAME \t ID 
    """
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        reader = csv.reader(input_file, delimiter=':')
        output = csv.writer(output_file, delimiter='\t')

        for rec in reader:
            if len(rec) > 1:
                output.writerow((rec[0], rec[2]))

        input_file.close()
        output_file.close()

    return


def main():
    input_file = os.path.join('sources', 'passwd.txt')
    output_file = os.path.join('sources', 'passwd.csv')

    passwd_to_csv(input_file, output_file)


if __name__ == '__main__':
    main()
