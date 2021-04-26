# pickling
import pickle
d1 = {1: 'a', 2: 'b'}
pickle_file = open("picklefile.txt", "wb")
pickle.dump(d1, pickle_file)

pickle_file = open("picklefile.txt", "rb")
newdict = pickle.load(pickle_file)
print(newdict)
