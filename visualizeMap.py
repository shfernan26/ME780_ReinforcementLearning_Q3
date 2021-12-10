import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

startPoint1 = [1, 1]
startPoint2 = [3, 2]

def visualizeMap(states, valMap, xSize, ySize, maxRewardStates, maxPenaltyStates, actions):

    rewardsList = []
    fig, ax = plt.subplots()
    for state in states:
        if state not in maxRewardStates and state not in maxPenaltyStates:
            # print(state, "------")
            for action in actions:
                currState = np.array(state) + np.array(action)
                if 0 < currState[0] <= ySize and 0 < currState[1] <= xSize: # If current state is within grid
                    rewardsList.append(valMap[currState[0]-1][currState[1]-1])
                    # print(currState)

            # print('list', rewardsList)
            maxReward = max(rewardsList)
            # print('max reward',maxReward)
            # print('state', state)
            for actions2 in actions:
                currState2 = np.array(state) + np.array(actions2)
                if -1 < currState2[0] <= ySize and -1 < currState2[1] <= xSize:  # If current state is within grid
                    # print('val', valMap[currState2[0]][currState2[1]])
                    # print('mystate', currState2)
                    if math.isclose(valMap[currState2[0]-1][currState2[1]-1], maxReward, abs_tol=0.1):
                        # print('max reward', maxReward)
                        # print('currstate2', currState2)
                        directionArr = currState2 - state
                        # print('max dir', directionArr)
                        if directionArr[0] == 1 and directionArr[1] == 0: # (y, x) below
                            ax.quiver(state[1], state[0], 0, -1) # (x,y)
                        if directionArr[0] == -1 and directionArr[1] == 0:  # (y, x) above
                            ax.quiver(state[1], state[0], 0, 1)  # (x,y)
                        if directionArr[0] == 0 and directionArr[1] == 1:  # (y, x) right
                            ax.quiver(state[1], state[0], 1, 0)  # (x,y)
                        if directionArr[0] == 0 and directionArr[1] == -1:  # (y, x) left
                            ax.quiver(state[1], state[0], -1, 0)  # (x,y)

            rewardsList.clear()

    xlim = [0, xSize]
    ylim = [0, ySize]
    print('hi', (maxPenaltyStates[0][0], maxPenaltyStates[0][1]))
    # circle1 = plt.Circle((startPoint1[0], startPoint1[1]), 0.15, color='black')
    # circle2 = plt.Circle((startPoint2[0], startPoint2[1]), 0.15, color='black')
    circle3 = plt.Circle((maxPenaltyStates[0][0], maxPenaltyStates[0][1]), 0.15, color='r')
    circle4 = plt.Circle((maxPenaltyStates[1][0], maxPenaltyStates[1][1]), 0.15, color='r')
    circle5 = plt.Circle((maxRewardStates[0][0], maxRewardStates[0][1]), 0.15, color='g')
    # ax.add_patch(circle1)
    # ax.add_patch(circle2)
    plt.gca().add_patch(circle3)
    ax.add_patch(circle4)
    ax.add_patch(circle5)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.yticks(np.arange(ylim[0], ylim[1], 1))
    plt.xticks(np.arange(xlim[0], xlim[1], 1))
    plt.gca().invert_yaxis()
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    plt.show()

    return None