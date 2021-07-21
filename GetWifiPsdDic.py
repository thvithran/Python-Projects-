import itertools as its
from typing import TextIO

'''
 Problems encountered do not understand? Python learning exchange group: 821 460 695 meet your needs, data base files have been uploaded, you can download their own!
'''
if __name__ == '__main__':
    words_num = "1234567890"
    words_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    r = its.product(words_num, repeat=8)
         dic: = open ( "password-8 digits .txt", "w")
    for i in r:
        dic.write("".join(i))
        dic.write("".join("\n"))
    dic.close()