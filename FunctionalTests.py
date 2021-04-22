import random
import time
import datetime as dt

changes_directory = "/home/work/sauvegarde_test/functional/"

small_data_file = "small_data.txt"
big_data_file = "big_data.txt"


filename_A = "Datei_A.txt"
filepath_A = changes_directory + filename_A

filename_B = "Datei_B.txt"
filepath_B = changes_directory + filename_B

sleeptime = 10  # type: float

def wait_until_time_reached(start_time = None):
    # interval to check for reached time
    check_interval = 0.5

    # set time to next full minute if not set
    if start_time is None:
        now = dt.datetime.now().time()
        if now.minute == 59:
            if now.hour == 23:
                start_time = dt.time(0,0)
            else:
                start_time = dt.time(now.hour + 1, 0)
        else:
            start_time = dt.time(now.hour, now.minute + 1)

    print('Starting at: ' + str(start_time))
    while dt.datetime.now().time() < start_time:
        print '.',
        time.sleep(check_interval)
    print('\n')


if __name__ == '__main__':


    # read data to insert
    small_data = None
    big_data = None

    with open(small_data_file) as sd_file:
        small_data = sd_file.read()
        sd_file.close()

    with open(big_data_file) as bd_file:
        big_data = bd_file.read()
        bd_file.close()

    # start at specific time
    #wait_until_time_reached()

    # create empty file A
    file_A = open(filepath_A, 'w')
    file_A.close()
    print(str(dt.datetime.now().time())+"\tFile A created, empty.")
    time.sleep(sleeptime)

    # add small data (X) to file A
    file_A = open(filepath_A, 'w')
    file_A.write(small_data)
    file_A.close()
    print(str(dt.datetime.now().time()) + "\tSmall data (X) written to File A.")
    time.sleep(sleeptime)

    # after 10 sec: overwrite A with big data (Y)
    file_A = open(filepath_A, 'w')
    file_A.write(big_data)
    file_A.close()
    print(str(dt.datetime.now().time()) + "\tBig data (X) written to File A.")
    time.sleep(sleeptime)

    # create new file B, containing small data (X)
    file_B = open(filepath_B, 'w')
    file_B.write(small_data)
    file_B.close()
    print(str(dt.datetime.now().time()) + "\tFile B created with small data (X).")

    print('Test done.')


