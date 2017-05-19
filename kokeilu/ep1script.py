#!/usr/bin/env python3

import csv
import glob
import sys
import os
from glob import glob

def last_6chars(x):
    return x[-6:]

def main(argv):
    if (len(argv) != 2):
        print("Enter .csv folder name as a command line parameter")
        exit()
    path2 = sys.argv[1] + 'subjects/' + '*'
    folders = glob(path2)
    folders = sorted(folders, key = last_6chars)

    for folder in folders:
        path = folder + '/*.csv'
        filenames = glob(path)
        filenames = sorted(filenames, key = last_6chars)

        #   if len(filenames) != 0:
        #       print("Invalid folder name")
        #       exit()

        with open("ep1out.csv","a") as fout:
                if len(filenames) == 60:
                    k = os.path.basename(os.path.normpath(folder))
                    for filename in filenames:
                        f = open(filename, 'r')
                        for row in f:
                            fout.write(row)
                            #fout.write("\n")
                        f.close()
                    fout.write(k)
                    fout.write("\n")


if __name__ == "__main__":
    main(sys.argv)