import os
import tempfile


class File:
    def __init__(self, path_to_file):
        self.idx = -1
        self.path_to_file = path_to_file
        if not os.path.exists(path_to_file):
            with open(path_to_file, 'w') as f:
                pass

    def __add__(self , obj):
        new_obj = File(os.path.join(tempfile.gettempdir(), hex(id(self) + id(obj))))
        new_obj.write(self.read() + obj.read())
        return new_obj

    def __str__(self):
        return self.path_to_file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path_to_file, 'r') as f:
            iter_list = f.readlines()
            if self.idx == len(iter_list) - 1:
                self.idx = -1
                raise StopIteration
            self.idx += 1
            return iter_list[self.idx]

    def read(self):
        with open(self.path_to_file, 'r') as f:
            result = f.read()
            return result 

    def write(self, text):
        with open(self.path_to_file, 'w') as f:
            f.write(text)
        return len(text)
