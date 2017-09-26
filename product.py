import sys
import os

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
Implement a function that takes a number
and adds a special prefix to it
'''
def get_array_name(counter):
    return "col_" + str(counter)



'''
Implement a function that takes a number
and adds a special prefix to it
'''
def get_var_name(counter):
    return "u_" + str(counter)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""







def two_bits_mult(bit1, bit2):


    #print make_AND_statement("test", bit1, bit2)

    #string = "(" + make_AND_statement("test", bit1, bit2) + ") "



    #return string

    return int(bit1) * int(bit2)

    "bit1 AND bit2"
    "outputs a bit as a string"




#def shift(storing_array):

    #for index in storing_array:



    #for index in storing_array:
    #    storing_array[index] = storing_array[index].append[]




def fill_array(num1, num2):

    "num1 is a string of bits (101)"
    "num2 is a string of bits (1)"

    # get length of
    len1 = len(num1)
    len2 = len(num2)

    array1 = list(num1)
    array2 = list(num2)

#    array1 = list(reversed(array1))
#    array2 = list(reversed(array2))

    storing_array = [[]] * 1024

    # col_one = [0] * len1


    for index2 in range(0, len2):

        array = [5] * 2048


        # shift by the right numbers of 0
        for counting in range(0, index2):
            array[counting] = 0



        # prints the numbers

    #    for index1 in range(len1, 0):
    #        r=two_bits_mult(array1[index1],array2[index2])

        for index1 in range(0, len1):
            r=two_bits_mult(array1[len1 - 1 - index1],array2[len2 - 1 - index2])


            # WE want 1 0 1 1 1 1 0 0 0 0 0 0 0 0

        #    col_one
            array[index1 + len2 - 1] = r
            print(r, end="")

        #    print(r + (index1 * "0"

        # shift by the right numbers of 0
    #    for counting in range(0, index2):
    #        array[len1 + 1 + counting] = 0


        #array[len1 + 1: index2]
        storing_array[index2] = array
        print(index2 * "0")
        print(list(reversed(array)))



#def add_column()




#def add()






"""
usage: python product.py "num1" "num2"
writes "NANDproduct.nand"
"""
def main():



    fill_array("101111", "111010101")

#    inname = sys.argv[1]
#    name,ext = os.path.splitext(inname)
#    with open(inname,'r') as infile:
#    	prog = infile.readlines()
#    outfile = open(name+'_converted.nand','w')
#    NANDify(outfile,prog)
#    outfile.close()





if __name__ == "__main__":
    main()
