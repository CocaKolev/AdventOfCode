filepath = "input2.txt"

def movement_import(filepath):


    with open(filepath, "r") as fp:
            data = fp.read()

    data_list = []
    for x in data.split():
        data_list.append(x)
    return data_list

def aim(data_list):
    aim = 0
    xmove = 0
    ymove = 0
    for x in range(0,len(data_list)-1,2):
        if data_list[x] == "forward":
            xmove = xmove + int(data_list[x+1])
            ymove = ymove + aim * int(data_list[x+1])
            # x += 1
        elif data_list[x] == "up":
            aim = aim - int(data_list[x+1])

            # x += 1
        else:
            aim = aim + int(data_list[x+1])
            # x += 1

    multiple = ymove * xmove 
    return multiple




# def movement(data_list): 
#     xmove = 0
#     ymove = 0
#     for x in range(0,len(data_list)-1,2):
#         if data_list[x] == "forward":
#             xmove = xmove + int(data_list[x+1])
#             # x += 1
#         elif data_list[x] == "up":
#             ymove = ymove - int(data_list[x+1])
#             # x += 1
#         else:
#             ymove = ymove + int(data_list[x+1])
#             # x += 1

#     multiple = xmove * ymove
#     return multiple

data_list = movement_import(filepath)
# print(movement(data_list))
print(aim(data_list))
