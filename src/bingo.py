# Author : Ali Snedden
# Date   : 3/23/22
# License: MIT
# Notes  : 
#   Caesar Cipher : https://en.wikipedia.org/wiki/Caesar_cipher   
#   https://dadoverflow.com/2019/05/31/python-bingo/
# Background : 
#       
# Purpose :
#   Generates encrypted words
#   
#  
#
# How to Run :
import sys
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
#import matplotlib.style as style
import numpy as np
import random
 
from error import exit_with_error
from error import warning
#%matplotlib inline
#style.use('seaborn-poster')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20})


def main(Verbose=True):
    """
    ARGS:
        None.
    DESCRIPTION:
    RETURN:
    DEBUG:
    FUTURE:
    """
    wordL = ["cat", "hat", "pop", "mom", "dad", "hog", "girl", "boy", "dirt", "red", "rat",
              "blue", "tree", "code", "run", "leaf", "tent", "camp", "help", "trust", "friend",
              "strong", "respect", "rain", "fun", "sun", "swim", "team", "program", "doctor"]

    random.shuffle(wordL)
    rowlen= 4  # make any size card you'd like
     
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(np.arange(0, rowlen + 1))
    ax.set_yticks(np.arange(0, rowlen + 1))
    plt.grid()
     
    for i, word in enumerate(wordL[:rowlen**2]):
        x = (i % rowlen) + 0.4
        y = int(i / rowlen) + 0.5
        ax.annotate(word, xy=(x, y), xytext=(x, y))
         
    plt.show()


if __name__ == "__main__":
    main()


