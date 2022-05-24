'''

    this function use for drow the rectangle,
    the use of this function we find minimun and maxmum value of hand(x, y) cordenet...

'''
def min_x_for_hand_rectangle(tempList):
    appendList = []

    for i in range(len(tempList)):
        appendList.append(tempList[i][0])

    return min(appendList)
    # find the min value of templist[i][j] in j...


def min_y_for_hand_rectangle(tempList):
    appendList = []

    for i in range(len(tempList)):
        appendList.append(tempList[i][1])

    return min(appendList)
    # find the min value of templist[i][j] in i...


def max_x_for_hand_rectangle(tempList):
    appendList = []

    for i in range(len(tempList)):
        appendList.append(tempList[i][0])

    return max(appendList)
    # find the max value of templist[i][j] in j...


def max_y_for_hand_rectangle(tempList):
    appendList = []

    for i in range(len(tempList)):
        appendList.append(tempList[i][1])

    return max(appendList)
    # find the max value of templist[i][j] in i...



# this function written by vineet krishna gupta...