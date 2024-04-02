import numpy as np


class MDP:
    """This class implements the MDP algorithm for a robot that moves
    in 3x3 world. The robot starts at left bottom square and should reach the
    diamond while avoiding fire and the blocked square

    @author: Dmitrii Kosintsev
    @date:   20 March 2024
  
    Initialise values for the class"""
    def __init__(self, world, currPosX, currPosY, rewards, actions):
        self.world = world
        self.currPosX = currPosX
        self.currPosY = currPosY
        self.rewards = rewards
        self.actions = actions
        # Define the discount factor
        self.gamma = 0.9
        # Initialize the value function and policy
        self.V = np.zeros((len(world), len(world[0])))
        self.policy = np.random.choice(actions, (len(world), len(world[0])))

    """The method defines the transition function to identify possible actions"""
    def transition_function(self):
        P = {}
        for action in actions:
            if action == "up":
                P[action] = [(-1, 0)]
            elif action == "down":
                P[action] = [(1, 0)]
            elif action == "left":
                P[action] = [(0, -1)]
            elif action == "right":
                P[action] = [(0, 1)]
        return P

    """ The method checks whether the goal is achieved"""
    def is_achieved(self):
        return self.world[self.currPosX][self.currPosY] == "D"

    """The method utilises the Markov Decision process to calculate the optimal policy"""
    def MDP(self, V, policy, gamma, theta=0.0001):
        while not self.is_achieved():
            delta = 0
            for i in range(len(world)):
                for j in range(len(world[0])):
                    old_v = V[i, j]

                    """Prevent the robot from reaching the fire and blocked square"""
                    if world[i][j] not in ["D", "B", "F"]:
                        new_v = np.zeros(len(actions))
                        for action in range(len(actions)):
                            for prob, (dx, dy) in zip(
                                    [1],
                                    self.transition_function()[actions[action]]):
                                new_x, new_y = i + dx, j + dy
                                if new_x < 0 or new_x >= len(
                                        world) or new_y < 0 or new_y >= len(
                                    world[0]) or world[new_x][new_y] == "B":
                                    new_x, new_y = i, j
                                reward = rewards[world[new_x][new_y]]
                                new_v[action] += prob * (reward + gamma * V[new_x, new_y])
                        best_action = np.argmax(new_v)
                        V[i, j] = new_v[best_action]
                        policy[i, j] = actions[best_action]
                    delta = max(delta, abs(old_v - V[i, j]))
            if delta < theta:
                break
        return policy

    """The method follows the steps of the robot according to the optimal policy
    and returns the ssequence of steps"""
    def print_results(self, currPosX, currPosY):
        curr_state = (currPosX, currPosY)
        action_sequence = []
        optimal_policy = self.MDP(self.V, self.policy, self.gamma)
        print(f"Optimal policy is: \n {optimal_policy}")

        # Loop through steps in the optimal policy and change the current location according to it
        while world[curr_state[0]][curr_state[1]] != "D":
            action = optimal_policy[curr_state[0]][curr_state[1]]
            action_sequence.append(action)

            # Change the current positions according to the action from the optimal policy
            if action == "up":
                curr_state = (max(curr_state[0] - 1, 0), curr_state[1])
            elif action == "down":
                curr_state = (min(curr_state[0] + 1, 2), curr_state[1])
            elif action == "left":
                curr_state = (curr_state[0], max(curr_state[1] - 1, 0))
            elif action == "right":
                curr_state = (curr_state[0], min(curr_state[1] + 1, 2))

        # Return the sequence of actions
        return action_sequence

# Define the world
world = [["F", "E", "D"],
         ["E", "E", "E"],
         ["E", "E", "B"]]

# Define the starting position
currPosX = 2
currPosY = 0

# Define the rewards
rewards = {"E": -0.04, "F": -1.0, "D": 1.0, "B": -0.5}

# Define the possible actions
actions = ["up", "down", "left", "right"]

# Main code
robot = MDP(world, currPosX, currPosY, rewards, actions)

# Print the sequence of actions
print(f"Sequence of steps: {robot.print_results(currPosX, currPosY)}")


""" Pseudocode implementation of the algorithm.
class MDP:
    initialise the class with values:
    - world: 2D array with values "E" (empty), "F" (fire), "B" (blocked), and "D" (diamond)
    - currPosX: current row of the 2D array
    - currPosY: current column of the 2D array
    - rewards: rewards according to the states
    - actions: set of possible movements UP, DOWN, LEFT, RIGHT

    # Define transition function P(s' | s, a), where s is a tuple of values currPosX and currPosY and a is the action to take
    transition_model(s, a, s') = probability of reaching state s' from state s after taking action a

    # Define reward function R(s, a)
    reward(s, a) = immediate reward received when taking action a in state s

    # Initialize value function (average future reward) V(s) for all states
    V(s) = 0 for all s in states

    # Discount factor (weightage on future rewards)
    gamma = 0.9

    # Policy - maps states to best actions
    policy(s) = None for all s in states

    # Loop for multiple iterations
    for i in range(iterations):
        # Update value function using Bellman equation
        for s in states:
            V_new(s) = max(a in actions: reward(s, a) + gamma * sum(s' in states: P(s' | s, a) * V(s')))
        V = V_new

        # Update policy based on the new value function
        for s in states:
            best_action = argmax(a in actions: reward(s, a) + gamma * sum(s' in states: P(s' | s, a) * V(s')))
            policy(s) = best_action

    # Return the optimal policy
    return policy

# Example usage
policy = MDP(world, currPosX, currPosY, rewards, actions)

# Follow the policy to reach the diamond
while world[currPosY][currPosX] != "D":
    action = policy[(currPosY, currPosX)]
    # Update position based on the action
"""
