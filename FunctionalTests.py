import random
import time

directory = "/home/work/SGTest/PythonTest/"
samples_filename = "teststrings_100.txt"

file_prefix = "testfile"


# number of files to create
number_of_files = 3

# number of changes
number_of_changes = 10

# set file for sample data depending on the needed number of changes
if number_of_changes > 100:
    samples_filename = "teststrings_1000.txt"
elif number_of_changes > 1000:
    samples_filename = "teststrings_100000.txt"

sleeptime = 1  # type: float

if __name__ == '__main__':
    print("Using Testdata from " + str(samples_filename))
    print("Sleep interval: " + str(sleeptime) + "s\n\n")

    with open(samples_filename) as file:

        sample_lines = file.readlines()

        filelist = []
        for i in range(number_of_files):
            fn = directory + file_prefix + str(i) + ".txt"
            filelist.append(fn)


        # make file changes
        fileindex = 0
        for i in range(number_of_changes):
            print(str(i) + "...")
            file = open(filelist[fileindex], "w")
            file.write(sample_lines[i])
            file.close()
            fileindex = (fileindex + 1) % number_of_files
            time.sleep(sleeptime)



