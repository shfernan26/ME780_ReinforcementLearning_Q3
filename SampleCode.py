import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

import visualizeMap as vm

maxRewardStates = [[1, 5]]
maxReward = 1
maxPenaltyStates = [[3,4], [3, 5]]
maxPenalty = -1
transitions = [[-1, 0], [0, 1], [1, 0], [0, -1]]   # up, right, down, left

regReward = 0

# startPoint1 = [1, 1]
# startPoint2 = [3, 2]
trials = 1000
gamma = 1

maxXSize = 6
maxYSize = 4


def actionRewardFunction(initialPosition, action):
    if initialPosition in maxRewardStates:
        return initialPosition, maxReward

    if initialPosition in maxPenaltyStates:
        return initialPosition, maxPenalty

    reward = regReward
    finalPosition = np.array(initialPosition) + np.array(action)
    if -1 in finalPosition or finalPosition[0] >= maxYSize or finalPosition[1] >= maxXSize:
        finalPosition = initialPosition

    return finalPosition, reward


def main():
    valueMap = np.zeros((maxYSize, maxXSize))
    states = [[i, j] for i in range(maxYSize) for j in range(maxXSize)]

    # values of the value function at step 0
    print("Init value map: ")
    print(states)

    deltas = []
    for it in range(trials):
        copyValueMap = valueMap #np.copy(valueMap)
        deltaState = []
        for state in states:
            weightedRewards = 0
            for action in transitions:
                finalPosition, reward = actionRewardFunction(state, action)
                weightedRewards += (1/len(transitions))*(reward+(gamma*valueMap[finalPosition[0], finalPosition[1]]))
            deltaState.append(np.abs(copyValueMap[state[0], state[1]]-weightedRewards))
            copyValueMap[state[0], state[1]] = weightedRewards
        deltas.append(deltaState)
        valueMap = copyValueMap
        if it in [0,1,2,9, 99, trials-1]:
            print("Iteration {}".format(it+1))
            print(valueMap)
            print("")

    plt.figure(figsize=(20, 10))
    plt.plot(deltas)
    plt.show()

    vm.visualizeMap(states, valueMap, maxXSize, maxYSize, maxRewardStates, maxPenaltyStates, transitions)


if __name__ == "__main__":
    main()