#given input data

data = ((45, 'foot'), (21, 'basket'), (10, 'hand'), (24, 'foot'), (21,
'hand'))

def unique_data_items(data):
    ''' input data is made of ((int, string), (int, string), ...)'''
    unique_nums = ()
    #initialising the tuple
    unique_words = ()
    for i in data:
        for y in i:
            if isinstance(y, str) and y not in unique_words:
                unique_words = unique_words + (y,)
            elif isinstance(y, int) and y not in unique_nums:
                unique_nums = unique_nums + (y,)
            else:
                print(y,)
    return unique_nums, unique_words
unique_data_items(data)
