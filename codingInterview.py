# i have a street, containing several blocks , each block will have n number of buildings and , assuming that each block has a apartment available for sale. I have to 
# choose an apartment which will have least distance to all of my priority buildings.
# the street will be given as a list, the priority will be given as a array.

street = [
    {
        "gym":False,
        "school": False,
        "store":True,
        "office" : True
    },
    {
        "gym":False,
        "school": True,
        "store":False,
        "office" : False
    },
    {
        "gym":False,
        "school": True,
        "store":False,
        "office" : False
    },
    {
        "gym":False,
        "school": True,
        "store":True,
        "office" : False
    },
    {
        "gym":True,
        "school": False,
        "store":True,
        "office" : False
    }
]

#priorityList = ["gym","school","store"] # expected output will be index 3 apartment.
priorityList = ["store","gym","office"] 


_less = 0
_extreme = len(street) - 1
#function to check the existence of a builiding in a given index

def haveBuilding(loc, building):
    for i in street[loc]:
        if street[loc][building]:
            return 1


priorityDistanceforward = {
         "gym" : -1,
         "school": -1,
         "store": -1,
         "office": -1
}
priorityDistancebackward = {
         "gym" : -1,
         "school": -1,
         "store": -1,
         "office": -1
}

priorityDistanceoptimal = {
         "gym" : -1,
         "school": -1,
         "store": -1,
         "office": -1 
} 

class Apartment:
    def __init__(self):
        self.optimalityRank = 0
        self.priorityDistanceoptimal = {
         "gym" : -1,
         "school": -1,
         "store": -1,
         "office": -1    
        }
        self.routeSum = 0
    
    def sumOfRoute(self):
        for i in self.priorityDistanceoptimal:
            self.routeSum += self.priorityDistanceoptimal[i]


def _RESET():
    for i in priorityDistanceforward:
        priorityDistanceforward[i] = -1
    for i in priorityDistancebackward:
        priorityDistancebackward[i] = -1

def finish(priorityDistance):
    flag = len(priorityDistance)
    count = 0
    for m in priorityDistance:
        if priorityDistance[m] >= 0:
            count += 1
    if flag == count:
        return True
    else:
        return False

def set(building,priorityDistance):
    if priorityDistance[building] >= 0:
        return True
    else:
        return False


def reset(loc,priorityDistance,direction):
    if direction == "forward":
        for m in priorityDistance:
            if priorityDistance[m] >= 0:
                 priorityDistance[m] -= loc
    if direction == "backward":
        for m in priorityDistance:
            if priorityDistance[m] >= 0:
                priorityDistance[m] = -1 * (priorityDistance[m] - loc)

                
def forwardbuildingDist(source, destination):
    """ the source or destination should not be end of list, add exceptions later """
    start = source
    end = destination
    while(start <= end):
        for i in street[start]:
            if i in priorityList:
                if not(set(i,priorityDistanceforward)):
                    """ add some measure here to avoid the call to finish """
                    if street[start][i]:
                        priorityDistanceforward[i] = start
        if finish(priorityDistanceforward):
            break
        start +=1        
    reset(source,priorityDistanceforward,"forward")  


def backwardbuildingDist(source, destination):
    start = source
    end = destination
    while(start >= end):
        for i in street[start]:
            if i in priorityList:
                if not(set(i,priorityDistancebackward)):
                    if street[start][i]:
                        priorityDistancebackward[i] = start
        if finish(priorityDistancebackward):
           break
        start -= 1
    reset(source,priorityDistancebackward,"backward")

#function to compare the forward and backward postition of priority buildings and select the best one.

def priorityDistanceOptimal(forward, backward, priorityDistanceoptimal):
    for i in priorityList:
        if forward[i] >= 0 and backward[i] < 0:
            priorityDistanceoptimal[i] = forward[i]
        if forward[i] < 0 and backward[i] >= 0:
            priorityDistanceoptimal[i] = backward[i]
        if forward[i] >= 0 and backward[i] >= 0:
            if forward[i] <= backward[i]:
                priorityDistanceoptimal[i] = forward[i]
            else:
                priorityDistanceoptimal[i] = backward[i]

def optimalityTieBreaker(apartmentObject1,apartmentObject2):
    maxValue1 = max(apartmentObject1.priorityDistanceoptimal.values())
    maxValue2 = max(apartmentObject2.priorityDistanceoptimal.values())
    if maxValue1 >= maxValue2:
        return { 'object1' : False, 'object2' : True}
    else:
        return { 'object1' : True, 'object2' : False}
    
def appartmentOptimalityRank(apartmentObject1, apartmentObject2):
    if apartmentObject1.routeSum < apartmentObject2.routeSum:
        apartmentObject1.optimalityRank = apartmentObject1.optimalityRank + apartmentObject2.optimalityRank + 1
    elif apartmentObject1.routeSum <= apartmentObject2.routeSum:
        resultDictionary = optimalityTieBreaker(apartmentObject1,apartmentObject2)
        if resultDictionary['object1']:
            apartmentObject1.optimalityRank = apartmentObject1.optimalityRank + apartmentObject2.optimalityRank + 1
        else:
            apartmentObject2.optimalityRank = apartmentObject2.optimalityRank + apartmentObject1.optimalityRank + 1
    else:
        apartmentObject2.optimalityRank = apartmentObject2.optimalityRank + apartmentObject1.optimalityRank + 1        

def highestOptimalRank(apartmentObject, limit):
    highest = 0
    for i in range(limit+1):
        if apartmentObject[i].optimalityRank > apartmentObject[highest].optimalityRank:
            highest = i
    return highest

ApartmentList = []
for i in range(_extreme + 1):
    ApartmentList.insert(i,Apartment())
    forwardbuildingDist(i,_extreme)
    backwardbuildingDist(i,_less)
    priorityDistanceOptimal(priorityDistanceforward,priorityDistancebackward,ApartmentList[i].priorityDistanceoptimal)
    ApartmentList[i].sumOfRoute()
    if i > 0:
        highest = highestOptimalRank(ApartmentList,i-1)
        appartmentOptimalityRank(ApartmentList[i],ApartmentList[highest])
    _RESET()

optimalApartmentChoice = highestOptimalRank(ApartmentList,_extreme)
print("Apartment at block ",optimalApartmentChoice," will be suitable for your needs !")



#forwardbuildingDist(1,4)
#backwardbuildingDist(1,0)
#priorityDistanceOptimal(priorityDistanceforward,priorityDistancebackward,priorityDistanceoptimal)
#print("Forward : ",priorityDistanceforward)
#print("Backward : ",priorityDistancebackward)
#print("Optimal : ",priorityDistanceoptimal) 



