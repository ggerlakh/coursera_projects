import os
import tempfile
import argparse
import json
import sys

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'a') as f:
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', type=str)
    parser.add_argument('--val', type=str)
    arg = parser.parse_args()
    arg.key = str(sys.argv[2])
    if not (arg.key and arg.val):
        if arg.key:
            file = open(storage_path, 'r')
            file_info = file.readlines()
            output_values = list()
            d = dict()
            for line in file_info:
                if arg.key in line: 
                    d = json.loads(line)
                    d_ = json.loads(line)
                    output_values.append(d[arg.key])
            d = d.clear()
            file_info = file_info.clear()
            print(', '.join(output_values))
            output_values = output_values.clear()
            file.close()
    else:
        arg.val = str(sys.argv[4])
        input_info = dict()
        input_info[arg.key] = arg.val
        f.write(json.dumps(input_info) + '\n')
        input_info = input_info.clear()
