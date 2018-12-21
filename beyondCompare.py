import sys
import os

def beyondCompare(fname1, fname2):

    # Open file for reading in text mode (default mode)
    with open(fname1, 'r') as f1, open(fname2, 'r') as f2:

        print("-----------------------------------")
        print("Compare files", "F> " + fname1, "<S " + fname2)
        print("-----------------------------------")

        # Read the first line from the files
        f1_line = f1.readline()
        f2_line = f2.readline()

        # line number
        line_num = 1

        # Loop if either file1 or file2 has not reached EOF
        while f1_line != '' or f2_line != '':

            # Strip the leading whitespaces
            f1_line = f1_line.rstrip()
            f2_line = f2_line.rstrip()

            # Compare the lines from both file
            if f1_line != f2_line:

                # If a line does not exist on file2 then mark the output with + sign
                if f2_line == '' and f1_line != '':
                    print("F>+","%d"% line_num,f1_line)
                #
                elif f1_line != '':
                    print("F>","%d"% line_num,f1_line)

                # If a line does not exist on file1 then mark the output with + sign
                if f1_line == '' and f2_line != '':
                    print("<S+","%d"% line_num,f2_line)
                #
                elif f2_line != '':
                    print("<S","%d"% line_num,f2_line)

            # Read the next line from the file
            f1_line = f1.readline()
            f2_line = f2.readline()

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