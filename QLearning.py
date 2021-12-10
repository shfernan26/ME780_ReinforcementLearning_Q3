import numpy as np
import matplotlib.pyplot as plt

import visualizeMap as vm

maxRewardStates = [[2, 6]]
maxReward = 1
maxPenaltyStates = [[4,5], [4, 6]]
maxPenalty = -1
transitions = [[-1, 0], [0, 1], [1, 0], [0, -1]]   # up, right, down, left

regReward = 0

trials = 20
gamma = 1

maxXSize = 6
maxYSize = 4

startPoint1 = [1, 1]
startPoint2 = [3, 2]
start = 2 # Change depending on which start point you have

if start == 1:
    startPoint = startPoint1
elif start == 2:
    startPoint = startPoint2



def getNextState(currState, action):
    if currState in maxRewardStates:
        return currState, maxReward

    if currState in maxPenaltyStates:
        return currState, maxPenalty

    nextState = np.array(currState) + np.array(action)
    if 0 in nextState or nextState[0] > maxYSize or nextState[1] > maxXSize:
        nextState = currState

    return nextState, regReward

def getProbability(transitions):
    return 1 / len(transitions)

def plotUtilityGrid(utilityGrid, trial):
    print("Trial # ", trial)
    print(utilityGrid)
    return None


def main():
    utilityGrid = np.zeros((maxYSize, maxXSize))
    states = [[i, j] for i in range(1, maxYSize+1) for j in range(1, maxXSize+1)]

    allTrialStateChange = []
    for trial in range(trials):

        singleTrialStateChange = []
        for state in states:
            utility = 0

            for action in transitions:
                nextPosition, reward = getNextState(state, action)
                utility = utility + getProbability(transitions)*(reward+(gamma*utilityGrid[nextPosition[0]-1, nextPosition[1]-1]))

            singleTrialStateChange.append(np.abs(utilityGrid[state[0]-1, state[1]-1]-utility)) # Checking difference in new/old utility
            utilityGrid[state[0]-1, state[1]-1] = utility # New utility map

        allTrialStateChange.append(singleTrialStateChange)

        if trial in [0,1,2,trials-2, trials-1]:
            plotUtilityGrid(utilityGrid, trial)

    plt.figure(figsize=(20, 10))
    plt.plot(allTrialStateChange)
    plt.show()
    vm.visualizeMap(states, utilityGrid, maxXSize, maxYSize, maxRewardStates, maxPenaltyStates, transitions, startPoint)



if __name__ == "__main__":
    main()