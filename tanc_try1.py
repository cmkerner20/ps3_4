import sys
import os
#These make properly formated strings given triples of variables.

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


def get_output_var_name(counter_y):
    # TODO
    return "y_" + str(counter_y)
    #SCOPE OF PYTHON VARIABLES??

def multiply1(f,a,b,counter):
  #initialize array that stores a list of list that contains all the numbers that need to be added
  storing_array  = []
  print("storing_array")
  print(str(storing_array))
  shift_counter = 0

  #iterate through the numbers
  for x in b:
    #local_list
    curr_array = []
    print("curr_array")
    print(str(curr_array))

    #add 0 to shift function
    for z in range(shift_counter):
          curr_array.append("z_0") # this should be an unassigned variable of value = 0
    shift_counter += 1

    for y in a:
        print("COUNTER")
        print(counter)
        print("before")
        print(str(curr_array))
        y_var = get_var_name(counter)
        counter = write_AND_triple_as_NAND(f,y_var,y,x,counter)
        #appending numbers in reverse order
        curr_array.append(y_var)
        print("after")
        print(str(curr_array))



    #reverse list

    curr_array.reverse()
    print("REVERESE")
    print(curr_array)
    #calculate zeroes to add to the front of number to make sure all lists are of same length.
    number_of_zeroes_needed = 8 - len(curr_array)
    zero_array = ["z_0"] * number_of_zeroes_needed
    curr_array = zero_array + curr_array
    print("STORING ARRAY BEFORE APPENDING")
    print(storing_array)
    storing_array.append(curr_array)
    print("STORING ARRAY AFTER APPENDING")
    print(storing_array)
    print("__________________________NEW OUTER LOOP _________________________")

  return storing_array


def add(f,list_a, list_b,counter):
  #there will probbaly be a big with the counters
  index_counter = 0
  carry_variable  = 0
  list_a.reverse()
  list_b.reverse()
  temp_list = []
  for a,b in zip(list_a, list_b):
    vars1 = get_var_name(counter)
    vars2 = get_var_name(counter)
    vars3 = get_var_name(counter)

    write_XOR_as_NAND(f, (str(vars1) + " = " + str(a) + " xor " + str(b)), counter)
    write_XOR_as_NAND(f, (str(vars2) + " = " + str(vars1) + " xor " + str(carry_variable)), counter)

    write_MAJ_as_NAND(f, (str(vars3) + " = maj(" + str(carry_variable) + "," + str(a)+ "," + str(b) + ")"), counter)
    carry_variable = vars3
    temp_list.append(vars2)
  return temp_list[::-1]


def collapse(f,l, counter):
  for x in range(0, len(l)-1):
    temp = add(f,l[x], l[x+1], counter)
    l[x+1] = temp
    if (len(l) == (len(l) - 2)):
      return
    else:
      continue
  return l[len(l)-1]

'''
def collapse(l, counter):
  for x in range(l):
    l[x+1] = add(l[x], l[x+1], counter)
    if (l == (range(l) - 1)):
      break
    else:
      continue
  return l[range(l)]
  '''


def finalmente(f,a,b,counter):
  counter_y = 0
  to_add_array = multiply1(f,a,b,counter)
  binary_list_solution = collapse(f,to_add_array, counter)
  for i in binary_list_solution:
    a = get_var_name(counter)
    counter += 1
    y = get_output_var_name(counter_y)
    counter_y += 1
    write_NAND_triple(f,a,i,i)
    write_NAND_triple(f,y,a,a)

"""
usage: python NANDp2NAND.py "filename.nandp" writes "filename_converted.nand"
"""

def main():
  outfile = open('converted.nand','w')
  finalmente(outfile,["x_0","x_1","x_2","x_3",],["x_4","x_5","x_6","x_7",],0)
  outfile.close()

if __name__ == "__main__":
    main()

