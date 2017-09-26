import sys
import os


"""
CS121 HW2 2017
THE TODO's are optional, since you can choose which helper functions you want.
However, you must still come up with a way to meet the specification.
The included code helps make properly formated strings, opens and closes files,
and writes to files.
"""

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

"""
Writes NAND triple (not line) to file
"""
def write_NAND_triple(f,output,x1,x2):
    line = make_NAND_statement(output,x1,x2)
    write_NAND_line(f,line)

'''
Writes any kind of line to file
'''
def write_DEBUG_line(f,line):
    f.write("%s\n" % line)


'''
Returns vars from OR line
'''
def parse_OR(line):
    # ASSUMES SPACING!
    vars = line.split()
    output = vars[0]
    input1 = vars[2]
    input2 = vars[4]
    return output, input1, input2


"""
Returns vars from XOR line
"""
def parse_XOR(line):
    # ASSUMES SPACING!
    # SAME FUNCTION AS parse_OR()
    vars = line.split()
    output = vars[0]
    input1 = vars[2]
    input2 = vars[4]
    return output, input1, input2

"""
Returns vars from AND line
"""
def parse_AND(line):
    # ASSUMES SPACING!
    # SAME FUNCTION AS parse_OR()
    vars = line.split()
    output = vars[0]
    input1 = vars[2]
    input2 = vars[4]
    return output, input1, input2



"""
Returns vars from NAND line
"""
def parse_NAND(line):
	# ASSUMES SPACING!
	# SAME FUNCTION AS parse_OR() and parse_XOR()
	vars = line.split()
	output = vars[0]
	input1 = vars[2]
	input2 = vars[4]
	return output, input1, input2

"""
Returns vars from MAJ line
"""
def parse_MAJ(line):
    # ASSUMES SPACING!
    words = line.split()
    output = words[0]
    variables = words[2].split(',')
    index = variables[0].index('(')
    input1 = variables[0][index+1:]
    input2 = variables[1]
    input3 = variables[2][:len(variables[2]) - 1]
    return output, input1, input2, input3

"""
MOTIVATING QUESTION: WHY DO THE BELOW FUNCTIONS ALL TAKE A COUNTER ARGUMENT?
"""

'''
TODO: Implement a function that takes a number
and adds a special prefix to it
'''
def get_var_name(counter):
    # TODO
    return "u_" + str(counter)
    #SCOPE OF PYTHON VARIABLES??

"""
Takes an AND line and writes a series of NAND lines to file
"""
def write_AND_as_NAND(f, line, counter):
    # TODO
    output, x_0, x_1 = parse_AND(line)
    write_AND_triple_as_NAND(f, output,x_0,x_1,counter)
    return counter 

"""
Takes an AND triple and writes a series of NAND lines to file
"""
def write_AND_triple_as_NAND(f, output,input1,input2,counter):
    # TODO
    temp = get_var_name(counter)
    write_NAND_triple(f, temp,input1,input2)
    write_NAND_triple(f, output,temp,temp)
    return counter + 1 

"""
Takes an XOR line and writes a series of NAND lines to file
"""
def write_XOR_as_NAND(f, line, counter):
    # TODO
    output, x_0, x_1 = parse_XOR(line)
    temp1 = get_var_name(counter)
    temp2 = get_var_name(counter+1)
    temp3 = get_var_name(counter+2)
    write_NAND_triple(f,temp1, x_0, x_1)
    write_NAND_triple(f,temp2, x_0, temp1)
    write_NAND_triple(f,temp3, x_1, temp1)
    write_NAND_triple(f,output, temp1, temp3)
    return counter + 3

"""
Takes an OR line and writes a series of NAND lines to file
"""
def write_OR_as_NAND(f, line, counter):
    # TODO	
    output, x_0, x_1 = parse_OR(line)
    write_OR_triple_as_NAND(f,output,x_0,x_1,counter)
    return counter

"""
Takes an OR triple and writes a series of NAND lines to file
"""
def write_OR_triple_as_NAND(f,output,input1,input2,counter):
    # TODO
    notx_0 = get_var_name(counter)
    notx_1 = get_var_name(counter+1)
    write_NAND_triple(f,not1, input1, input1)
    write_NAND_triple(f,not2,input2, input2)
    write_NAND_triple(f,output, not1, not2)
    return counter + 2

"""
Takes a MAJ line and writes a series of NAND lines to file
"""
def write_MAJ_as_NAND(f, line,counter):
	output, input1, input2, input3 = parse_MAJ(line)
	temp0 = get_var_name(counter)
	temp1 = get_var_name(counter+1)
	temp2 = get_var_name(counter+2)
	temp3 = get_var_name(counter+3)
	not3 = get_var_name(counter+4)
	write_NAND_triple(f,temp0, input1, input2)
	write_NAND_triple(f,temp1, input1, input3)
	write_NAND_triple(f,temp2,input2, input3)
	write_NAND_triple(f,temp3, temp2, temp1)
	write_NAND_triple(f,not3, temp3, temp3)
	write_NAND_triple(f,output, not3, temp0)
	return counter + 5
    # TODO	

    


"""
This function should:
    TODO: keep track of counter for new vars
    TODO: write an XOR line as a series of NAND lines
    TODO: write a MAJ line as a series of NAND lines
    TODO: leave NAND lines alone
"""
def NANDify(f,prog):  
    counter = 0
    for line in prog:  
        if "XOR" in line:
            # TODO: HANDLE XOR CASE
            counter = write_XOR_as_NAND(f, line, counter)
        elif "MAJ" in line:
            # TODO: HANDLE MAJ CASE
            counter = write_MAJ_as_NAND(f, line, counter)
        else:
            # TODO: HANDLE NAND CASE
            write_NAND_line(f,line)

"""
usage: python NANDp2NAND.py "filename.nandp" writes "filename_converted.nand"
"""
def main():
	inname = sys.argv[1]
	name,ext = os.path.splitext(inname)
	with open(inname,'r') as infile:
		prog = infile.readlines()
	outfile = open(name+'_converted.nand','w')
	NANDify(outfile,prog)
	outfile.close()

if __name__ == "__main__":
    main()

