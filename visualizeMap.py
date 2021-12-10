import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")


def visualizeMap(states, valMap, xSize, ySize, maxRewardStates, maxPenaltyStates, actions, startPoint):

    rewardsList = []
    fig, ax = plt.subplots()
    for state in states:
        if state not in maxRewardStates and state not in maxPenaltyStates:

            # Loop through surrounding states
            for action in actions:
                currState = np.array(state) + np.array(action)
                if 0 < currState[0] <= ySize and 0 < currState[1] <= xSize: # If current state is within grid
                    rewardsList.append(valMap[currState[0]-1][currState[1]-1])
            # Direction of quiver plots based on surrounding state of highest utility
            maxReward = max(rewardsList)

           # Loop through states again to find state(s) with this highest reward
            for actions2 in actions:
                currState2 = np.array(state) + np.array(actions2)
                if -1 < currState2[0] <= ySize and -1 < currState2[1] <= xSize:  # If current state is within grid continue
                    # Look for max reward around current state (rounding to nearest tenth)
                    if math.isclose(valMap[currState2[0]-1][currState2[1]-1], maxReward, abs_tol=0.1):
                        # Get vector between current state and state with highest reward
                        directionArr = currState2 - state

                        if directionArr[0] == 1 and directionArr[1] == 0: # (y, x) below
                            ax.quiver(state[1], state[0], 0, -1) # (x,y)
                        if directionArr[0] == -1 and directionArr[1] == 0:  # (y, x) above
                            ax.quiver(state[1], state[0], 0, 1)  # (x,y)
                        if directionArr[0] == 0 and directionArr[1] == 1:  # (y, x) right
                            ax.quiver(state[1], state[0], 1, 0)  # (x,y)
                        if directionArr[0] == 0 and directionArr[1] == -1:  # (y, x) left
                            ax.quiver(state[1], state[0], -1, 0)  # (x,y)

            rewardsList.clear()

    # Plotting
    xlim = [0, xSize]
    ylim = [0, ySize]
    circle1 = plt.Circle((startPoint[1], startPoint[0]), 0.1, color='blue')
    ax.add_patch(circle1)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.yticks(np.arange(ylim[0], ylim[1], 1))
    plt.xticks(np.arange(xlim[0], xlim[1], 1))
    plt.gca().invert_yaxis()
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    plt.show()

    return None