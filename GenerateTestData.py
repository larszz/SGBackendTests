import random
import time
import datetime as dt

directory = "/home/work/sauvegarde_test/performance/"
samples_filename = "teststrings_100.txt"

file_prefix = "testfile"

# sleep time between file changes
sleeptime = 0.101  # type: float

# number of files to create
number_of_files = 200

# number of changes
number_of_changes = 1000

# max changes
max_changes = 100000

# only metadata important (-> use duplicated data to avoid massive data writing)
only_meta = 0

if only_meta == 1:
    samples_filename = "teststrings_100.txt"

# set file for sample data depending on the needed number of changes
elif number_of_changes <= 100:
    samples_filename = "teststrings_100.txt"
elif (number_of_changes > 100) & (number_of_changes <= 1000):
    samples_filename = "teststrings_1000.txt"
elif number_of_changes > 1000:
    samples_filename = "teststrings_100000.txt"




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

