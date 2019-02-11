import pickle
from util import save_obj

dict_fruit = { 'peaches': 13, 'apples': 4, 'oranges': 11}

save_obj(dict_fruit, './OtherFiles/pickle_fuit')

with open('./OtherFiles/pickle_fuit.pkl', 'rb') as file:
    data = pickle.load(file)

print(data)

