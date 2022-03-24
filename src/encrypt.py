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
    # For decription
    keyD = {'z' : 'a',
            'a' : 'b',
            'b' : 'c',
            'c' : 'd',
            'd' : 'e',
            'e' : 'f',
            'f' : 'g',
            'g' : 'h',
            'h' : 'i',
            'i' : 'j',
            'j' : 'k',
            'k' : 'l',
            'l' : 'm',
            'm' : 'n',
            'n' : 'o',
            'o' : 'p',
            'p' : 'q',
            'q' : 'r',
            'r' : 's',
            's' : 't',
            't' : 'u',
            'u' : 'v',
            'v' : 'w',
            'w' : 'x',
            'x' : 'y',
            'y' : 'z'}
    encryptD= {
            'a' : 'z',
            'b' : 'a',
            'c' : 'b',
            'd' : 'c',
            'e' : 'd',
            'f' : 'e',
            'g' : 'f',
            'h' : 'g',
            'i' : 'h',
            'j' : 'i',
            'k' : 'j',
            'l' : 'k',
            'm' : 'l',
            'n' : 'm',
            'o' : 'n',
            'p' : 'o',
            'q' : 'p',
            'r' : 'q',
            's' : 'r',
            't' : 's',
            'u' : 't',
            'v' : 'u',
            'w' : 'v',
            'x' : 'w',
            'y' : 'x',
            'z' : 'y'}
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

