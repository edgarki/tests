# find concurrent calls timings to suggest to hire agents if applied
# first input is the number of available agents
# the second line is the number of calls times, with starting and ending times
# the third input is how long are the call timing input in terms of arguments
# next lines are calls times

#input example
#
#1
#3
#2
#1481122000 1481122020
#1481122000 1481122040
#1481122030 1481122035


def numberOfAgentsToAdd( noOfCurrentAgents, callsTimes ):

    number = 0

    # follow all list
    for i in callsTimes:
        # +1 because range consider the last -1
        r = range(i[0], i[1]+1)
        for j in callsTimes:
            # remove duplicated comparing events
            if i == j:
                break
            # the same of i
            rj = range(j[0], j[1]+1)
            # check i in j and j in i overlap, then count it
            if j[0] in r or j[1] in r or i[0] in rj or i[1] in rj:
                number += 1

    # return additional agents needed
    return number - noOfCurrentAgents

# an example to test
noOfCurrentAgents = 1
callsTimes = [[1481122000, 1481122020], [1481122000, 1481122040], [1481122030, 1481122035]]
print numberOfAgentsToAdd(noOfCurrentAgents,callsTimes)

