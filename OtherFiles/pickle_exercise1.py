# Import pickle package
import pickle
from util import save_obj

dict1 = {'Mar': '84.4', 'June': '69.4', 'Aug': '85', 'Airline': '8'}
save_obj(dict1, './OtherFiles/data')


# Open pickle file and load data: d
with open('./OtherFiles/data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))