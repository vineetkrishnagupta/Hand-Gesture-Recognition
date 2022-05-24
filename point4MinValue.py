'''
    if point 4 value is minimum(y axis) in full list than this function return True, else False.
'''

def min_value_for_Point_4(tempList):
    appendList = []

    for i in range(len(tempList)):
        appendList.append(tempList[i][1])
    
    if min(appendList) == appendList[4]:
        return True
    
    else:
        False



# this function written by vineet krishna gupta...