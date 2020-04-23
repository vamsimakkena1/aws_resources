import time

def starttime():

    current_time = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
    return current_time