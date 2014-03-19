# Sebastian Raschka, 03/2014
# Read a csv file (with a header) into a dictionary
# where the dictionary structure will be
#   {header_col1: [val1_line1, val1_line2, ...], header_col2: [val2_line1, val2_line2, ...], ...}

def read_csv(csv_path):
    with open(csv_path, 'r') as in_csv:
        header = in_csv.readline().strip().split(',')
        data = {i:[] for i in header}
        for line in in_csv:
            line = line.strip().split(',')
            for i in range(len(line)-1):
                data[header[i]].append(line[i])
    return data
