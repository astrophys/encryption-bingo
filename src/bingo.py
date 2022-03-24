# Author : Ali Snedden
# Date   : 3/23/22
# License: MIT
# Notes  : 
#   Caesar Cipher   : https://en.wikipedia.org/wiki/Caesar_cipher   
#   For inspiration : https://dadoverflow.com/2019/05/31/python-bingo/
#
# Background : 
#       
# Purpose :
#   Generates encrypted words
#   
#
# How to Run :
#       python3 src/bingo.py wordlist.txt
import sys
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import random
 
from error import exit_with_error
from error import warning
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20})


def print_help(Arg):
    """
    ARGS:
        Arg     : int, exit value
    DESCRIPTION:
        Print Help. Exit with value arg
    RETURN:
        N/A
    DEBUG:
        1. Tested, it worked
    FUTURE:
    """
    sys.stdout.write(
        "\nUSAGE : python src/bingo.py wordlist.txt \n\n"
        "   wordlist.txt : (file) List of words (one entry per line) to make bingo out of\n"
        "                         \n")
    sys.exit(Arg)



def main(Verbose=True):
    """
    ARGS:
        None.
    DESCRIPTION:
    RETURN:
    DEBUG:
    FUTURE:
    """
    path = sys.argv[1]
    fin  = open(path, "r")
    wordL=[]
    for line in fin:
        wordL.append(line)
    
    random.shuffle(wordL)
    nRow= 4                     # make any size card you'd like
     
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(np.arange(0, nRow + 1))
    ax.set_yticks(np.arange(0, nRow + 1))
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    plt.grid()
     
    # Create bingo plot - Grab only enough elements to fill it
    for i, word in enumerate(wordL[:nRow**2]):
        x = (i % nRow) + 0.25
        y = int(i / nRow) + 0.25
        ax.annotate(word, xy=(x, y), xytext=(x, y))
    plt.savefig("bingo-card.png")


if __name__ == "__main__":
    main()


