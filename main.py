import random
import time

testpath = "/home/work/SGTest/PythonTest/"
filename = "teststrings_100.txt"

testfiles_prefix = "testfile"


# number of files to create
numoffiles = 3

# number of changes
numofchanges = 50
if numofchanges > 100:
    filename = "teststrings_1000.txt"
elif numofchanges > 1000:
    filename = "teststrings_100000.txt"

if __name__ == '__main__':
    print(str(numofchanges) + " Changes -> " + "Using Data from " + str(filename))

    with open(filename) as f:

        content = f.readlines()

        filelist = []
        for i in range(numoffiles):
            fn = testpath + testfiles_prefix + str(i) + ".txt"
            filelist.append(fn)


        # make file changes
        fileindex = 0
        for i in range(numofchanges):
            print(str(i) + "...")
            f = open(filelist[fileindex], "w")
            f.write(content[i])
            f.close()
            fileindex = (fileindex + 1) % numoffiles
            time.sleep(0.5)



