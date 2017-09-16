import pickle

food_name = "celery"
data = pickle.load(open("Data(5.81ms)/"+food_name+".pkl","r"))

print(len(data[0]))
#print(data)