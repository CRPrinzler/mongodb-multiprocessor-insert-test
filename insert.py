import random
import pymongo
import string
import time
import multiprocessing
from multiprocessing import Pool

# f function for imap() iteration
def f(x):
  return x

# Get values
print('How many inserts?: ')
numstr=input()
num = int(numstr)

# random string size
print('Set the random string size (integer): ')
strsize = input()
N = int(strsize)

# mongo host?
print('Set the host for mongodb (ip):')
mongohost = input()

# start time
st = time.time()

stcpu = time.process_time()

# MonogDB connection
myclient = pymongo.MongoClient("mongodb://"+str(mongohost)+":27017/")
mydb = myclient["powertest"]
mycol = mydb["logdata"]



with Pool(processes=12) as pool:
  	for i in pool.imap_unordered(f, range(num)):
				name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
				mydict = { "name": ""+ str(name), "address": "test" }
				i = mycol.insert_one(mydict)


# End time
et = time.time()
etcpu = time.process_time()

# Calculate the measured time
elapsed_time = et - st
res = etcpu -stcpu

# Output results

if res < 61 :
		print(num,' inserts have been processed')
		print('Execution time:',elapsed_time, 'seconds')
		print('CPU Execution time:', res, 'seconds')
else:
		elapsed_timem = elapsed_time/60
		resmin = res/60
		print(num,' inserts have been processed')
		print('Execution time:',elapsed_timem, 'minutes')
		print('CPU Execution time:', resmin, 'minutes')
