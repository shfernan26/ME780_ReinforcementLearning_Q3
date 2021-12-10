import numpy as np
import matplotlib.pyplot as plt

import visualizeMap as vm

maxRewardStates = [[2, 6]]
maxReward = 1
maxPenaltyStates = [[4,5], [4, 6]]
maxPenalty = -1
transitions = [[-1, 0], [0, 1], [1, 0], [0, -1]]   # up, right, down, left

regReward = 0

# startPoint1 = [1, 1]
# startPoint2 = [3, 2]
trials = 20
gamma = 1

maxXSize = 6
maxYSize = 4


def getNextState(currState, action):
    if currState in maxRewardStates:
        return currState, maxReward

    if currState in maxPenaltyStates:
        return currState, maxPenalty

    nextState = np.array(currState) + np.array(action)
    if 0 in nextState or nextState[0] > maxYSize or nextState[1] > maxXSize:
        nextState = currState

    return nextState, regReward


def main():
    valueMap = np.zeros((maxYSize, maxXSize))
    states = [[i, j] for i in range(1, maxYSize+1) for j in range(1, maxXSize+1)]

    # values of the value function at step 0
    print("Init value map: ")
    print(states)

    deltas = []
    for it in range(trials):
        copyValueMap = valueMap
        deltaState = []
        for state in states:
            utility = 0
            for action in transitions:
                nextPosition, reward = getNextState(state, action)
                # print(nextPosition)
                utility += (1/len(transitions))*(reward+(gamma*valueMap[nextPosition[0]-1, nextPosition[1]-1]))
            deltaState.append(np.abs(copyValueMap[state[0]-1, state[1]-1]-utility))
            copyValueMap[state[0]-1, state[1]-1] = utility
        deltas.append(deltaState)
        valueMap = copyValueMap
        if it in [0,1,2,trials-2, trials-1]:
            print("Iteration {}".format(it+1))
            print(valueMap)
            print("")

    plt.figure(figsize=(20, 10))
    plt.plot(deltas)
    plt.show()

    vm.visualizeMap(states, valueMap, maxXSize, maxYSize, maxRewardStates, maxPenaltyStates, transitions)


if __name__ == "__main__":
    main()