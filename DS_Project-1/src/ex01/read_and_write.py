def read_and_write(input_file, output_file):
    with open(input_file, 'r') as in_file:
        with open(output_file, 'w') as out_file:
            out_file.write(in_file.read().replace('",', '"\t').replace(
                'false,', 'false\t').replace('true,', 'true\t'))


if __name__ == "__main__":
    input_file = 'ds.csv'
    output_file = 'ds.tsv'
    read_and_write(input_file, output_file)
