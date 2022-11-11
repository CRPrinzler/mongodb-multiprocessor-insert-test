import os
import random
import pymongo
import string
import time
import multiprocessing
from multiprocessing import Pool
from halo import Halo

# By Rinzler.dk

os.system('clear')

print('You have ' + str(multiprocessing.cpu_count()) +' logical CPUs in your system.')
cpu = multiprocessing.cpu_count()
print('Lets use each of them...')
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

# mongo port?
print('Set the host for mongodb (default: 27017):')
mongoport = input()
#ask for port database and collection
# mongo DB?
print('Database name:')
dbname = input()

# mongo collection?
print('Collection name:')
mongocol = input()
os.system('clear')


# start time
st = time.time()

stcpu = time.process_time()

# MonogDB connection
myclient = pymongo.MongoClient("mongodb://"+str(mongohost)+":"+str(mongoport)+"/")
mydb = myclient[""+str(dbname)+""]
mycol = mydb[""+str(mongocol)+""]

spinner = Halo(text='Inserting random data into monogDB', spinner='dots')
spinner.start()

with Pool(processes=cpu) as pool:
  	for i in pool.imap_unordered(f, range(num)):
				name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
				mydict = { "name": ""+ str(name), "address": "XX"+ str(name)}
				i = mycol.insert_one(mydict)

spinner.stop()

# End time
et = time.time()
etcpu = time.process_time()

# Calculate the measured time
elapsed_time = et - st
res = etcpu -stcpu

# Output results
os.system('clear')

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
