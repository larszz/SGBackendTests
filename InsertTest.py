import random
import time
import datetime as dt

directory = "/home/work/sauvegarde_test/performance/"
samples_filename = "insertstrings_new.txt"

file_prefix = "testfile_insert"

# sleep time between file changes
sleeptime = 2  # type: float

# number of files to create
number_of_files = 100

# number of changes
number_of_changes = 10

# max changes
max_changes = 100000



if __name__ == '__main__':
    print("Using Testdata from " + str(samples_filename))
    print("Sleep interval: " + str(sleeptime) + "s\n\n")

    wait = 3
    print('Start in: ' + str(wait) + 'sekonds')
    time.sleep(wait)

    with open(samples_filename) as file:

        sample_lines = file.readlines()

        filelist = []
        for i in range(number_of_files):
            fn = directory + file_prefix + str(i) + ".txt"
            filelist.append(fn)

        start_time = dt.datetime.now().time()
        print ('Starting: ' + str(start_time))
        # make file changes
        fileindex = 0
        for i in range(number_of_changes):
            print(str(i) + '/' + str(number_of_changes) + "...")
            file = open(filelist[fileindex], "w")
            file.write(sample_lines[i % len(sample_lines)])
            file.close()
            fileindex = (fileindex + 1) % number_of_files
            time.sleep(sleeptime)

        print('Started:\t' + str(start_time))
        print ('Finished:\t' + str(dt.datetime.now().time()))

