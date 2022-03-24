# Encryption Bingo
#### Author : Ali Snedden
#### License: MIT
#### Date   : 3/23/22
## Purpose:
This repo was whipped together quickly to present the concept of encryption to a Girl Scout
Troop. It uses a Caesar Cipher where the letter's have been shifted by one. 

## Dependencies
1. Python-3 (tested with Python-3.7.3)
2. Matplotlib (tested with 3.2.1)

## To Use
1. Generate a list of words, one entry per line in a text file (see `wordlist.txt`) for an
   example
2. Run 
    ```
        python3 src/generate-bingo-card.py wordlist.txt
    ```
   n-times to generate as many bingo cards as you need. The output is name bingo-card.png, so 
   they'll need to be renamed as you go.
3. Pass out the cipher to the kids
4. As you play bingo, run 
    ```
        python3 src/encrypt.py encrypt WORD
    ```
   where `WORD` is an entry drawn from `wordlist.txt`
5. Write the encrypted message on a white board and let the kids decrypt it, marking off 
   entries as they go.





