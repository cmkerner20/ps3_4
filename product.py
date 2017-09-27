import sys
import os
import math

"""
CS121 HW3 2017





"""


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Helpers functions from HW2.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''
These make properly formated strings given triples of variables.
'''
def make_AND_statement(output,input1,input2):
    return  "{} := {} AND {}".format(output, input1, input2)

def make_OR_statement(output,input1,input2):
    return  "{} := {} OR {}".format(output, input1, input2)

def make_XOR_statement(output,input1,input2):
    return  "{} := {} XOR {}".format(output, input1, input2)

def make_NAND_statement(output,input1,input2):
    return  "{} := {} NAND {}".format(output, input1, input2)


'''
Takes a file object f and a NAND line,
and writes a NAND line to the file with a newline character
'''
def write_NAND_line(f,line):
    f.write("%s\n" % line)

'''
Function that takes a number
and adds a special prefix to it
'''
def get_var_name(counter):
    return "u_" + str(counter)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# multiply two bits together
# CURRENTLY IN PYTHON, NEED TO CONVERT TO OUTPUTTING NAND
def two_bits_mult(bit1, bit2):
    #return "(" + make_AND_statement("test", bit1, bit2) + ") "
    return int(bit1) * int(bit2)


# fill a storing array with sub-arrays of each of the smaller multiplications
# CURRENTLY IN PYTHON, NEED TO CONVERT TO OUTPUTTING NAND
def fill_array(num1, num2):
    # get length of each string of bits
    len1 = len(num1)
    len2 = len(num2)

    # store each string of bits in arrays of single bits
    arr1 = list(num1)
    arr2 = list(num2)

    # create an empty storing array of size 512 that will store 512 sub-arrays
    # of each of the 512 multiplications
    storing_arr = [[]] * 4

    # fill the current array with the result of the multiplication and the
    # right number of 0 for the power shift
    for i2 in range(0, len2):
        # initialize a new array for new multiplication with 0s
        cur_arr = [0] * 512

        # shift by the right numbers of 0 to account for current power
        for counting in range(0, i2):
            cur_arr[counting] = 0

        # multiply the bits 2 by 2 and put them in the current array
        for i1 in range(0, len1):
            cur_arr[i1 + i2] = two_bits_mult(arr1[len1 - 1 - i1], arr2[len2 - 1 - i2])

        # reverse the current array and store it in our storing array
        storing_arr[i2] = list(reversed(cur_arr))

    return storing_arr





def carry(sum_arr):

    reversed_arr = list(reversed(sum_arr))
    len_arr = len(reversed_arr)

    for i in range(0, len_arr - 1):
        carry = math.floor(reversed_arr[i] / 2)
        reversed_arr[i] = reversed_arr[i] % 2
        reversed_arr[i + 1] = reversed_arr[i + 1] + carry

    return list(reversed(reversed_arr))




# adds all of the sub-arrays together, NEED TO IMPLEMENT CARRY
# CURRENTLY IN PYTHON, NEED TO CONVERT TO OUTPUTTING NAND
def add(storing_arr):
    # get length of the storing array
    storing_len = len(storing_arr)

    # create a new array of the sum of each of the sub-arrays of our
    # storing array
    for i in range(0, storing_len - 1):
        sum_arr = [x + y for x,y in zip(storing_arr[i], storing_arr[i + 1])]


    print(sum_arr)


    final_arr = carry(sum_arr)


#    print(final_arr)


    return final_arr





"""
usage: python product.py "num1" "num2"
writes "NANDproduct.nand"
"""
def main():


    add(fill_array("101111", "1111"))

#    inname = sys.argv[1]
#    name,ext = os.path.splitext(inname)
#    with open(inname,'r') as infile:
#    	prog = infile.readlines()
#    outfile = open(name+'_converted.nand','w')
#    NANDify(outfile,prog)
#    outfile.close()




# call program
if __name__ == "__main__":
    main()
