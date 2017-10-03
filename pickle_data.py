import numpy as np
import csv
import pickle
import os
import itertools

# generate a time-force data file

fork_property = "steel"
food_name = "cantelope"
trial = "4"
data_range_i = 926
data_range_f = 1005
directory = "Data(test)/data_raw/"+fork_property+"/"+food_name
directory_f = "Data(test)/data_filtered/"+fork_property+"/"+food_name
input_filename = "Data(5.81ms)/"+food_name+"_"+fork_property+" fork.txt"
input_filename_f = "data_filtered/"+food_name+"_"+fork_property+" fork_filtered.txt"

output_file = open("Data(5.81ms)/"+food_name+"_steel fork.csv",'w')
# output_file_f = open("data_filtered/"+food_name+"_"+fork_property+" fork_filtered.csv",'w')

force_data = []
with open(input_filename) as f:
	for line in f:
		force_data.append([(int(n)-1390)*0.594*0.0098 for n in line.split()][0])

time = np.arange(0,0.00581*len(force_data),0.00581,dtype=np.float32)

print(len(time))
print(len(force_data))

writer = csv.writer(output_file,delimiter=',')
writer.writerows(zip(time,force_data))
output_file.close()

# generate a directory
if not os.path.exists(directory):
	os.makedirs(directory)

if not os.path.exists(directory_f):
	os.makedirs(directory_f)
# generate a pickle file
pickle_file = open(directory+"/"+trial+".pkl","w")
pickle_file_f = open(directory_f+"/"+trial+".pkl","w")
output_file = open("Data(5.81ms)/"+food_name+"_steel fork.csv","r")

tf_data = csv.reader(output_file)

time_list = []
force_list = []
force_list_f = []

with open(input_filename_f) as ff:
	for d in itertools.islice(ff,data_range_i,data_range_f):
		force_list_f.append(float(d))

print(len(force_list_f))


# force_list = tf_data.iloc[1,283:354]
# time_list = tf_data.iloc[0,0:len(force_list)-1]

# for row in tf_data:
# 	for a in itertools.islice(row[1],283,354):
#  		force_list.append(a)
#  	for b in itertools.islice(row[0],0,len(force_list)-1):
#  		time_list.append(b)
 	# time_list.append(row[0][0:len(force_list)-1])
 	
for row in itertools.islice(tf_data,data_range_i,data_range_f):
	force_list.append(float(row[1]))

time_list = time[0:len(force_list)]

print(len(force_list))
print(len(time_list))
# print(force_list)
# print(time_list)

pickle.dump([time_list,force_list],pickle_file)
pickle.dump([time_list,force_list_f],pickle_file_f)
pickle_file.close()
pickle_file_f.close()
output_file.close()