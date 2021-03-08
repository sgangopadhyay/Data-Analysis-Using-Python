x = [160,160,161,162,163,163,163,164,164,170,"suman"]

def check_number_in_list(data):
    number_count = 0
    not_number_count = 0
    total_elements = int(len(data))
    for data in data:
        if (isinstance(data, int)==True or isinstance(data, float)==True):
            number_count = number_count + 1
        elif(isinstance(data, int)==False or isinstance(data, float)==False):
            not_number_count = not_number_count + 1
    if (total_elements == number_count):
        return True
    else:
        return False


def check(data):
    pass

print(check_number_in_list(x))