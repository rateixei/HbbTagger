import numpy as np
from numpy.lib.recfunctions import stack_arrays
from root_numpy import root2array, root2rec
import glob
import pandas as pd

import argparse
parser =  argparse.ArgumentParser(description='Tree to pandas in h5')
parser.add_argument("-i", "--input", dest="i", type=str, required=True)
parser.add_argument("-t", "--treeName", dest="t", type=str, required=True)
parser.add_argument("-o", "--output", dest="o", type=str, required=True)
opt = parser.parse_args()

arraytree = root2array(opt.i, opt.t)
df = pd.DataFrame(arraytree)
df.info()
df.to_hdf(opt.o, 'branches')

