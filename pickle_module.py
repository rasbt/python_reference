# sr 10/29/13
# The pickle module converts Python objects into byte streams
# to save them as a file on your drive for re-use.
#
# module documentation http://docs.python.org/2/library/pickle.html

import pickle

#### Generate some object
my_dict = dict()
for i in range(1,1000):
    my_dict[i] = "some text"

#### Save object to file
pickle_out = open('my_file.pkl', 'wb')
pickle.dump(my_dict, pickle_out)
pickle_out.close()

#### Load object from file
my_object_file = open('my_file.pkl', 'rb')
my_dict = pickle.load(my_object_file)
my_object_file.close()

