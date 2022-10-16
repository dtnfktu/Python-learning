import datetime

def addlog(filename:str, msg:str) :
    with open(filename,'a') as f :
        f.write(str(datetime.datetime.now()) + ' - ' + msg + '\n')