from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import numpy as np
import os
import csv


def read_files(file_dir):
    label_txt = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if 'txt' in file:
                label_txt.append(file)
    return label_txt

def write_files(label_txt):
    for txt in label_txt:
        with open(txt, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            data_ = ''
            for i, item in enumerate(data):
                x1,y1,x2,y2,x3,y3,x4,y4,label = (item[i] for i in range(9))
                [x1,y1],[x2,y2],[x3,y3],[x4,y4] = sort_xy(x1,y1,x2,y2,x3,y3,x4,y4)
                if ('b' or 'B') in label[0]: label = 'b'
                elif ('s' or 'S') in label[0]: label = 's'
                elif ('r' or 'R') in label[0]: label = 'r'

                item_ = x1+','+y1+','+x2+','+y2+','+x3+','+y3+','+x4+','+y4+','+label
                item_ += '\n'
                data_ += item_
            with open(txt, 'w') as f_:
                f_.write(data_)

if __name__ == '__main__':
    label_txt = read_files("./")
    write_files(label_txt)
