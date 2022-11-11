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



# start time
st = time.time()

stcpu = time.process_time()

# MonogDB connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["powertest"]
mycol = mydb["logdata"]

# random string size
N = 7

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
