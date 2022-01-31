filepath = "input3.txt"

def powerconsumption_import(filepath):

    with open(filepath, "r") as fp:
            data = fp.read()
        
    data_list = []
    for x in data.split():
        data_list.append(x)
    return data_list

def lifesupplyrating(data_list):

    count0, count1 = 0,0
    o2= 0 
    O2List = data_list

    for x in range(0,12):
        for y in range(0,len(O2List)):
            if (O2List[y])[x] == "0":
                count0 += 1
            else:
                count1 += 1
        if count0>count1:
            remove1(O2List,x)
            # for y in range(0,len(O2List)):
            #     if (O2List[y])[x] == "1":
            #         O2List.remove((O2List[y])[x])
        else:
            remove0(O2List,x)
            # for y in range(0,len(O2List)):
            #     if (O2List[y])[x] == "0":
            #         O2List.remove()



    rating = co2 * o2 
    return rating

def remove1(shorteneddata, originalX):
    return [x for x in shorteneddata if (shorteneddata[x])[originalX] == "1"]

def remove0(shorteneddata, originalX):
    return [x for x in shorteneddata if (shorteneddata[x])[originalX] == "0"]

def powerconsumption(data_list):
    gamma, epsilon = "", ""
    
    for x in range(0,12):
        count0,count1 = 0,0
        for y in range(len(data_list)):
            if (data_list[y])[x] == "0":
                count0 += 1
            else:
                count1 += 1
        if count0 < count1:
            gamma += "1"
        else:
            gamma += "0"

#    print(gamma)
    inv_dict = {'0' : '1', '1' : '0'}
    for i in gamma:
        epsilon += inv_dict[i]

    gamma = int(gamma, 2)
 #   print(gamma)
  #  print(epsilon)

    epsilon = int(epsilon,2)
   # print(epsilon)
    totalpower = gamma * epsilon
    return totalpower

data = powerconsumption_import(filepath)
print(powerconsumption(data))
print(lifesupplyrating(data))

