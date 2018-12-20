# prepare for file to take in arguments
from sys import argv
# check if file exists
from os.path import exists
# disperse arguments into variables
script, from_file, to_file = argv
# print what is going to happen
print(f"Copying from {from_file} to {to_file}")
# open file in in read mode then run the read function and store it indata
# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()
# Inform user of the contents size
print(f"The input file is {len(indata)} bytes long")
# print if file exists or not
print(f"Does the output file exist? {exists(to_file)}")
# prompt user what to do next
print("Ready, hit RETURN  to continue, CTRL-C to abort.")
# wait for users input
input()
# open file that was created into write mode
out_file = open(to_file, 'w')
# write contents of the first file to this new file
out_file.write(indata)
# status notification
print("Alright, all done.")
# close both files
out_file.close()
in_file.close()