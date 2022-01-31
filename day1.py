
filepath = "input1.txt"
def depth_import(filepath):
    with open(filepath, "r") as fp:
        data = fp.read()

        data_int = []
        for x in data.split():
            data_int.append(int(x))

        #data_int = [int(x) for x in data.split()]
        fp.close()
        return data_int


# def increaseCounter(data):
#     counter = 0
#     for x in range(len(data)-1):
#         if data[x]<data[x+1]:
#             counter += 1
#     return counter

def increaseWindowCounter(data):
    counter = 0
    for x in range(len(data)-3):
        if (data[x]+data[x+1]+data[x+2])<(data[x+1]+data[x+2]+data[x+3]):
            counter += 1
    return counter

#print(depth_import(filepath))

data = depth_import(filepath)
# print(increaseCounter(data))
print(increaseWindowCounter(data))
    
