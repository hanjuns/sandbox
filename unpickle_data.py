from __future__ import print_function
import pickle

food_name = "carrot"
fork_property = "steel"
directory = "Data(test)/data_raw/"+fork_property+"/"+food_name

data = pickle.load(open(directory+"/1.pkl","r"))

print(data)
# print(len(data[0]))
# print(data[0])
# print(len(data[1]))
# print(data[1])