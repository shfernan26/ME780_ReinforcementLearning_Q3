import numpy as np
import matplotlib.pyplot as plt

import visualizeMap as vm

maxRewardStates = [[2,6]]
maxReward = 1
maxPenaltyStates = [[4,5], [4,6]]
maxPenalty = -1
initialStates = [[1,1], [3,2]]

actions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

trials = 20
gamma = 1

maxXSize = 6
maxYSize = 4


def main():
    # Initializing things
    stateGrid = [[i, j] for i in range(maxXSize) for j in range(maxYSize)]
    valueGrid = np.zeros((maxYSize, maxXSize))
    deltas = []
    utilityVal = 0


    for trial in range(trials):
        for state in stateGrid:
            print(state)
            # for action in actions:





    # deltas = []
    # for it in range(numIterations):
    #     copyValueMap = np.copy(valueMap)
    #     deltaState = []
    #     for state in states:
    #         weightedRewards = 0
    #         for action in actions:
    #             finalPosition, reward = actionRewardFunction(state, action)
    #             weightedRewards += (1/len(actions))*(reward+(gamma*valueMap[finalPosition[0], finalPosition[1]]))
    #         deltaState.append(np.abs(copyValueMap[state[0], state[1]]-weightedRewards))
    #         copyValueMap[state[0], state[1]] = weightedRewards
    #     deltas.append(deltaState)
    #     valueMap = copyValueMap
    #     if it in [0,1,2,9, 99, numIterations-1]:
    #         print("Iteration {}".format(it+1))
    #         print(valueMap)
    #         print("")
    #
    # plt.figure(figsize=(20, 10))
    # plt.plot(deltas)
    # plt.show()
    #
    # vm.visualizeMap(states, valueMap, gridSize, terminationStates, actions)


if __name__ == "__main__":
    main()
