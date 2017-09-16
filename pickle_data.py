import numpy as np
import csv
import pickle

# generate a time-force data file
food_name = "celery"
input_filename = "Data(5.81ms)/"+food_name+"_steel fork.txt"
output_file = open("Data(5.81ms)/"+food_name+".csv",'w')

force_data = []
with open(input_filename) as f:
	for line in f:
		force_data.append([int(n) for n in line.split()][0])

time = np.arange(0,5.81*len(force_data),5.81,dtype=np.float32)

print(len(time))
# print(len(force_data))

writer = csv.writer(output_file,delimiter=',')
writer.writerows(zip(time,force_data))
output_file.close()

# generate a pickle file
pickle_file = open("Data(5.81ms)/"+food_name+".pkl","w")
output_file = open("Data(5.81ms)/"+food_name+".csv","r")

tf_data = csv.reader(output_file)

time_list = []
force_list = []

for row in tf_data:
 	time_list.append(row[0])
 	force_list.append(row[1])

pickle.dump([time_list,force_list],pickle_file)
pickle_file.close()
output_file.close()