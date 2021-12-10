import math
import numpy as np
import matplotlib.pyplot as plt

def visualizeMap(states, valMap, xSize, ySize, maxRewardStates, maxPenaltyStates, actions):

    rewardsList = []
    fig, ax = plt.subplots()
    for state in states:
        if state not in maxRewardStates and state not in maxPenaltyStates:
            # print(state, "------")
            for action in actions:
                currState = np.array(state) + np.array(action)
                if -1 < currState[0] < ySize and -1 < currState[1] < xSize: # If current state is within grid
                    rewardsList.append(valMap[currState[0]][currState[1]])
                    # print(currState)

            # print('list', rewardsList)
            maxReward = max(rewardsList)
            # print('max reward',maxReward)
            # print('state', state)
            for actions2 in actions:
                currState2 = np.array(state) + np.array(actions2)
                if -1 < currState2[0] < ySize and -1 < currState2[1] < xSize:  # If current state is within grid
                    # print('val', valMap[currState2[0]][currState2[1]])
                    # print('mystate', currState2)
                    if math.isclose(valMap[currState2[0]][currState2[1]], maxReward, abs_tol=0.1):
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

    plt.xlim([-0.5, xSize-0.5])
    plt.ylim([-0.5, ySize-0.5])
    plt.gca().invert_yaxis()
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    plt.show()

    return None