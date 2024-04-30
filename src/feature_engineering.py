import baseline as bl
import numpy as np
from PyBioMed import Pyprotein
from PyBioMed.PyProtein import CTD

train = bl.load_train_data("data/train.csv", val_split=False)
test = bl.load_test_data("data/test.csv")

train_seq, test_seq = train.sequence, test.sequence     #extract the sequences
print("test sequence total",len(train_seq))
print("train sequence total",len(test_seq))

'''I am attempting here to see if I can extract features I think are important from different softwares and see if
   I can maybe run another software ontop of these that then extracts the most important features. I then will feed
   this into my existing models (by copying and pasting in this file) to see if it makes a differnece.'''
