import random

def arbitarily_pattern(whole_index: int):
    list_index = []
    for i in range(0,whole_index - 1):
        random_bool = random.choice([True, False])
        list_index.append(random_bool)
    return list_index 


