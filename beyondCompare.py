import sys
import os

def beyondCompare(fname1, fname2):

    # Open file for reading in text mode (default mode)
    with open(fname1, 'r') as file1, open(fname2, 'r') as file2:

        print("-----------------------------------")
        print("Compare files", "F> " + fname1, "<S " + fname2)
        print("-----------------------------------")

        # Read the first line from the files
        file1_line = file1.readline()
        file2_line = file2.readline()

        # line number
        line_num = 1

        # Loop if either file1 or file2 has not reached EOF
        while file1_line != '' or file2_line != '':

            # Strip the leading whitespaces
            file1_line = file1_line.rstrip()
            file2_line = file2_line.rstrip()

            # Compare the lines from both file
            if file1_line != file2_line:

                # If a line does not exist on file2 then mark the output with + sign
                if file2_line == '' and file1_line != '':
                    print("F>+","%d"% line_num,file1_line)
                #
                elif file1_line != '':
                    print("F>","%d"% line_num,file1_line)

                # If a line does not exist on file1 then mark the output with + sign
                if file1_line == '' and file2_line != '':
                    print("<S+","%d"% line_num,file2_line)
                #
                elif file2_line != '':
                    print("<S","%d"% line_num,file2_line)

            # Read the next line from the file
            file1_line = file1.readline()
            file2_line = file2.readline()

            # Increment line number
            line_num += 1
    return

def main():

    fname1 = sys.argv[1:][0]
    fname2 = sys.argv[2:][0]

    print("fname1 =" , fname1)
    print("fname2 =", fname2)

    beyondCompare(fname1, fname2)

    return

if __name__ == "__main__":
    main()