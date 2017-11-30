import time, getpass

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

username = getpass.getuser()
print (username)
#Jack wrote this code
