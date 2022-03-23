# Author : Ali Snedden
# Date   : 3/23/22
# License: MIT
# Notes  : 
#   Caesar Cipher : https://en.wikipedia.org/wiki/Caesar_cipher   
#
# Background : 
#       
# Purpose :
#   Generates encrypted words
#   
#  
#
# How to Run :
import sys
from error import exit_with_error
from error import warning
    
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
        "\nUSAGE : python src/encrypt.py [encrypt|decrypt] WORD \n\n"
        "   [encrypt|decrypt] : (str) Encrypts or Deciphers WORD \n"
        "   WORD              : (str) to encrypt or decrypt\n"
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
    ######### Get Command Line Options ##########
    if(len(sys.argv) != 2 and len(sys.argv) != 3):
        print_help(1)
    elif(len(sys.argv) == 2 and "-h" in sys.argv[1]):
        print_help(0)
    # Check python version
    if(sys.version_info[0] != 3):
        exit_with_error("ERROR!!! Wrong python version ({}), version 3 "
                        "expected\n".format(sys.version_info[0]))

    option = sys.argv[1].lower()
    word   = sys.argv[2].lower()
    keyD   = dict()
    keyD['z'] = 'a'
    keyD['a'] = 'b'
    keyD['b'] = 'c'
    keyD['c'] = 'd'
    keyD['d'] = 'e'
    keyD['e'] = 'f'
    keyD['f'] = 'g'
    keyD['g'] = 'h'
    keyD['h'] = 'i'
    keyD['i'] = 'j'
    keyD['j'] = 'k'
    keyD['k'] = 'l'
    keyD['l'] = 'm'
    keyD['m'] = 'n'
    keyD['n'] = 'o'
    keyD['o'] = 'p'
    keyD['p'] = 'q'
    keyD['q'] = 'r'
    keyD['r'] = 's'
    keyD['s'] = 't'
    keyD['t'] = 'u'
    keyD['u'] = 'v'
    keyD['v'] = 'w'
    keyD['w'] = 'x'
    keyD['x'] = 'y'
    keyD['y'] = 'z'
    encryptD  = dict()
    encryptD['a'] = 'z'
    encryptD['b'] = 'a'
    encryptD['c'] = 'b'
    encryptD['d'] = 'c'
    encryptD['e'] = 'd'
    encryptD['f'] = 'e'
    encryptD['g'] = 'f'
    encryptD['h'] = 'g'
    encryptD['i'] = 'h'
    encryptD['j'] = 'i'
    encryptD['k'] = 'j'
    encryptD['l'] = 'k'
    encryptD['m'] = 'l'
    encryptD['n'] = 'm'
    encryptD['o'] = 'n'
    encryptD['p'] = 'o'
    encryptD['q'] = 'p'
    encryptD['r'] = 'q'
    encryptD['s'] = 'r'
    encryptD['t'] = 's'
    encryptD['u'] = 't'
    encryptD['v'] = 'u'
    encryptD['w'] = 'v'
    encryptD['x'] = 'w'
    encryptD['y'] = 'x'
    encryptD['z'] = 'y'

    result=[]

    if(option == 'decrypt'):
        for c in word:
            result.append(keyD[c])

    if(option == 'encrypt'):
        for c in word:
            result.append(encryptD[c])
    result = ''.join(result)

    print(result)
    #### Loops
    sys.exit(0)


if __name__ == "__main__":
    main()

