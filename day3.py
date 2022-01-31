filepath = "input3.txt"

def powerconsumption_import(filepath):

    with open(filepath, "r") as fp:
            data = fp.read()
        
    data_list = []
    for x in data.split():
        data_list.append(x)
    return data_list


#could make function way more condensed, not going to in interest of time and getting more problems done

def lifesupplyrating(data_list):

    O2List = data_list
    stayinloop = True

    #FOR THE 02 SENSOR
    for x in range(0,12):
        count0, count1 = 0,0
        for y in range(0,len(O2List)):
            if len(O2List) == 1:
                stayinloop = False
                break
            if (O2List[y])[x] == "0":
                count0 += 1
            else:
                count1 += 1
        if stayinloop:
            if count0>count1:
                O2List = remove1(O2List,x)
                # for y in range(0,len(O2List)):
                #     if (O2List[y])[x] == "1":
                #         O2List.remove((O2List[y])[x])
            else:
                O2List = remove0(O2List,x)
                # for y in range(0,len(O2List)):
                #     if (O2List[y])[x] == "0":
                #         O2List.remove((O2List[y])[x]))
        else:
            break


    CO2List = data_list
    stayinloop = True
#FOR THE C02 SENSOR
    for x in range(0,12):
        count0, count1 = 0,0
        for y in range(0,len(CO2List)):
            if len(CO2List) == 1:
                stayinloop = False
                break
            if (CO2List[y])[x] == "0":
                count0 += 1
            else:
                count1 += 1
        if stayinloop:
            if count0<=count1:
                CO2List = remove1(CO2List,x)
            else:
                CO2List = remove0(CO2List,x)
        else:
            break




    
    rating = int(O2List[0],2) * int(CO2List[0],2)
    return rating




def remove1(shorteneddata, originalX):
    newList = []
    for y in range(0,len(shorteneddata)):
        if (shorteneddata[y])[originalX] == "0":
            newList.append((shorteneddata[y]))
    return newList
    # return [x for x in shorteneddata if (shorteneddata[x])[originalX] == "1"]

def remove0(shorteneddata, originalX):
    newList = []
    for y in range(0,len(shorteneddata)):
        if (shorteneddata[y])[originalX] == "1":
            newList.append((shorteneddata[y]))
    return newList
    #return [x for x in shorteneddata if (shorteneddata[x])[originalX] == "0"]

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

