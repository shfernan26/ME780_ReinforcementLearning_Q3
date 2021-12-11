import numpy as np
import matplotlib.pyplot as plt
import random
import visualizeMap as vm

maxRewardStates = [[2, 6]]
maxReward = 1
maxPenaltyStates = [[4,5], [4, 6]]
maxPenalty = -1
transitions = [[-1, 0], [0, 1], [1, 0], [0, -1]]   # up, right, down, left

regReward = 0

trials = 2  # 20
gamma = 1
lr = 0.5
maxAttempts = 100

maxXSize = 4
maxYSize = 6

startPoint1 = [1, 1] # [y,x, action number to next state)
startPoint2 = [4, 4]
start = 2  # Change depending on which start point you have

if start == 1:
    startPoint = startPoint1
elif start == 2:
    startPoint = startPoint2

def initializeActionRewards(q_grid):
    for actionState in q_grid:
        if actionState[0] == maxRewardStates[0][0] and actionState[1] == maxRewardStates[0][1]:
            actionState[2] = maxReward
        elif (actionState[0] == maxPenaltyStates[0][0] and actionState[1] == maxPenaltyStates[0][1]) or (actionState[0] == maxPenaltyStates[1][0] and actionState[1] == maxPenaltyStates[1][1]):
            actionState[2] = maxPenalty
        else:
            actionState[2] = regReward

    return q_grid

def updateGrid(qGrid, state):
    for acState in qGrid:
        if acState[0] == state[0] and acState[1] == state[1]:
            return qGrid.index(acState)


def getAction():
    return random.choice(transitions)

def getNextState(currState, qGrid):

    action = getAction()
    next_state = np.array(currState) + np.array(action)
    # Don't make action if out of bounds
    while 0 in next_state or next_state[0] >= maxYSize or next_state[1] >= maxXSize:
        action = getAction()
        next_state = np.array(currState) + np.array(action)

    return next_state

def getProbability(transitions):
    return 1 / len(transitions)

def getUtility(prob, reward, gamma, utilityGrid, posY, posX):
    return prob*(reward+(gamma*utilityGrid[posY, posX]))


def plotUtilityGrid(utilityGrid, trial):
    print("Trial # ", trial)
    print(utilityGrid)
    return None


def main():
    qGrid = [[i, j, acReward] for i in range(1, maxYSize+1) for j in range(1, maxXSize+1) for acReward in range(1, len(transitions)+1)]

    states = [[i, j] for i in range(1, maxYSize+1) for j in range(1, maxXSize+1)]

    qGrid = initializeActionRewards(qGrid)
    print('mygrid', qGrid)

    for trial in range(trials):


        path = []
        path.append((startPoint))

        # print('a', path)
        currAttempt = 0

        while currAttempt < maxAttempts:
            currAttempt += 1
            currState = path[-1]
            if (currState in maxRewardStates):
                print('Arrived')
                for acState in qGrid:
                    if acState[0] == currState[0] and acState[1] == currState[1]:
                        acState[2] = maxReward

                for state in reversed(path):
                    for acState in qGrid:
                        if acState[0] == state[0] and acState[1] == state[1]:
                            currQVal = acState[2]
                            reward = currQVal + lr*(gamma*maxReward-currQVal)
                            qGrid = updateGrid(qGrid, state)


            elif (currState in maxPenaltyStates):
                for acState in qGrid:
                    if acState[0] == currState[0] and acState[1] == currState[1]:
                        acState[2] = maxPenalty

                for state in reversed(path):
                    for acState in qGrid:
                        if acState[0] == state[0] and acState[1] == state[1]:
                            currQVal = acState[2]
                            reward = currQVal + lr * (gamma * maxPenalty - currQVal)
                            qGrid = updateGrid(qGrid, state)

            else:
                # print('z')
                nextState = getNextState(currState, qGrid)
                # print(nextState)
                path.append(list(nextState))

        print(len(path))
        print('path', path[0], path[10], path[-1])



    # vm.visualizeMap(states, utilityGrid, maxXSize, maxYSize, maxRewardStates, maxPenaltyStates, transitions, startPoint)



if __name__ == "__main__":
    main()