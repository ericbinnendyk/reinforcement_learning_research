import random

class Stack:
    def __init__(self, lists=[['a'], ['b'], ['c'], ['d']]):
        # 'a', 'b', 'c', 'd', 'floor'
        # build 4x4 grid of blocks
        self.env = []
        for i in range(4):
            self.env.append(['', '', '', ''])
        j = 0
        # Populate environment with content of lists. This should also work when len(lists) < 4
        for l in lists:
            i = 3
            for block in l:
                self.env[i][j] = block
                i -= 1
            j += 1
        '''self.env[3][0] = 'a'
        self.env[3][1] = 'b'
        self.env[3][2] = 'c'
        self.env[3][3] = 'd'''
    def is_move_valid(self, block1, block2):
        if block1 == 'floor' or not self.is_on_top(block1) or (block2 != 'floor' and not self.is_on_top(block2)) or block1 == block2:
            return False
        return True
    # performs the action of moving, and returns (reward, is_done)
    # reward is -5 if move is invalid, -1 if move is valid but does not complete the game.
    # +50 if the game is complete with all blocks stacked atop 'a'.
    # +10 if the game is complete otherwise
    def move(self, block1, block2):
        if block1 == block2:
            print("Error: cannot move block {} to itself".format(block1, block2))
            return (-5, False)
        if block1 == 'floor':
            print("Error: cannot move floor atop other block")
            return (-5, False)
        if self.is_on_top(block1):
            if block2 == 'floor':
                loc = self.location(block1)
                # if block is already on floor, do nothing. otherwise, find a new column with nothing in it and move there.
                if loc[0] == 3:
                    # do nothing
                    pass
                else:
                    self.env[loc[0]][loc[1]] = ''
                    i = 0
                    for i in range(4):
                        if self.env[3][i] == '':
                            break
                    self.env[3][i] = block1
            else:
                if self.is_on_top(block2):
                    loc1 = self.location(block1)
                    loc2 = self.location(block2)
                    self.env[loc1[0]][loc1[1]] = ''
                    self.env[loc2[0] - 1][loc2[1]] = block1 # loc2[0] - 1 should never be less than 0, try to see why
                else:
                    print("Error: cannot move block {} to block {}".format(block1, block2))
                    return (-5, False)
        else:
            print("Error: cannot move block {} to block {}".format(block1, block2))
            return (-5, False)
        if self.is_stacked() and self.location('a')[0] == 3:
            return (50, True)
        elif self.is_stacked():
            return (10, True)
        else:
            return (-1, False)
    def is_stacked(self):
        return self.location('a')[1] == self.location('b')[1] == self.location('c')[1] == self.location('d')[1]
    def location(self, block):
        loc = [-1, -1] # [-1, -1] is location of floor
        for i in range(4):
            for j in range(4):
                if self.env[i][j] == block:
                    loc = [i, j]
                    return loc
        return loc
    def on(self, block1, block2):
        return (self.location(block1)[0] == 3 and block2 == 'floor') or (self.location(block1)[0] == self.location(block2)[0] - 1 and self.location(block1)[1] == self.location(block2)[1])
    def is_on_top(self, block):
        loc = self.location(block)
        if loc == [-1, -1]: # block is 'floor'
            return False
        return loc[0] == 0 or self.env[loc[0] - 1][loc[1]] == ''
    def display(self):
        for i in range(4):
            for j in range(4):
                print(self.env[i][j] if self.env[i][j] != '' else ' ', end='')
            print()
        print("____")
    def get_env_as_lists(self):
        lists = []
        for i in range(4):
            l = []
            for j in range(3, -1, -1):
                if self.env[j][i] == '':
                    break
                l.append(self.env[j][i])
            lists.append(l)
        return lists

blocks = ['a', 'b', 'c', 'd', 'floor']

# write idealized move predicate
# the top function means “X is on the top of the stack containing Y”
def topofstackwith(env_lists, X, Y):
    stack = Stack(env_lists)
    return (X == Y and stack.is_on_top(X)) or any([stack.on(Z, Y) and topofstackwith(env_lists, X, Z) for Z in blocks])
def move(env_lists, X, Y):
    stack = Stack(env_lists)
    return topofstackwith(env_lists, Y, 'a') and stack.is_on_top(X) and X != Y

# function that takes a policy as input and plays according to the policy
# policy is a function from state -> action. In this case, an action is represented as a pair of blocks (X, Y)
# and is the action of moving X to Y.
gamma = 0.8
def gen_episode(policy):
    maxrun = 100
    states = [None] * maxrun
    actions = [None] * maxrun
    rewards = [0] * (maxrun + 1)
    returns = [0] * (maxrun + 1)
    stack = Stack()
    states[0] = stack.get_env_as_lists()
    for i in range(maxrun):
        action = policy(stack.get_env_as_lists())
        actions[i] = action
        reward, done = stack.move(*action)
        if i < maxrun - 1:
            states[i + 1] = stack.get_env_as_lists()
        rewards[i + 1] = reward
        if done:
            break
    for i in range(maxrun - 1, -1, -1):
        returns[i] = gamma*(rewards[i] + returns[i + 1])
    return states, actions, rewards, returns

# policy that randomly chooses actions with uniform probabilities
# use rejection sampling to repeatedly sample actions until we get a valid action
def random_action(env):
    while True:
        i = random.randrange(5)
        j = random.randrange(5)
        stack = Stack(env)
        if stack.is_move_valid(blocks[i], blocks[j]):
            return (blocks[i], blocks[j])

# to do: redo it so the policy only produces actions that are "possible"?
# Ramyaa never mentioned what reward I should return when moving can't be done, so I guess I just avoid choosing those actions altogether
# UPDATE: Done.
def is_equivalent(state1, state2):
    if [] in state1:
        state1 = state1[:]
        while [] in state1:
            state1.remove([])
    if [] in state2:
        state2 = state2[:]
        while [] in state2:
            state2.remove([])
    sorted_state1 = sorted(state1, key=lambda x: (len(x), ord(x[0]) if len(x) > 0 else 0))
    sorted_state2 = sorted(state2, key=lambda x: (len(x), ord(x[0]) if len(x) > 0 else 0))
    return sorted_state1 == sorted_state2

# Learn the Q-table by generating episodes repeatedly
# The output of this process should be a table mapping certain states to the value of each possible action.
def normalize(state):
    state = state[:] # make a copy
    while [] in state:
        state.remove([])
    return sorted(state, key=lambda x: (len(x), ord(x[0]) if len(x) > 0 else 0))

stackings = []
# Counter: a list of dictionaries mapping (X, Y) to the number of counts of move(X, Y).
# One dictionary for each state.
counter = []
# Qtable is similar, but it maps (X, Y) to the Q-value of move(X, Y).
Qtable = []

maxiter = 20000
for h in range(maxiter):
    (states, actions, rewards, returns) = gen_episode(random_action)
    reached_states = [] # all states reached this episode
    for i, state in enumerate(states):
        if state == None:
            break
        if actions[i] == None:
            break
        state = normalize(state) # convert state to canonical form
        # If this is a genuinely new state, add it to the tables.
        if state not in stackings:
            stackings.append(state)
            counter.append(dict())
            Qtable.append(dict())
        if state not in reached_states:
            # add state to reached_states (for this episode)
            reached_states.append(state)
            # add value of state to table
            j = stackings.index(state)
            if actions[i] in counter[j]:
                counter[j][actions[i]] += 1
                Qtable[j][actions[i]] += returns[i + 1]
            else:
                counter[j][actions[i]] = 1
                Qtable[j][actions[i]] = returns[i + 1]

# divide each value in Q by the number of ocurrences to get the average Q value
for i, Qstate in enumerate(Qtable):
    for act in Qstate:
        Qstate[act] /= counter[i][act]

# Plot a ROC curve to see how well value > n predicts move(X, Y)
# Set up a table with all state+actions and values
data = []
for key in Qtable_dict:
    data.append([Qtable_dict[key], move(stackings[key[0]], key[1], key[2])])

sensitivities = []
specificities = []
cutoff = -30
while cutoff < 50: # may need to change these values
    sensitivities.append(len([[x, y] for [x, y] in data if x > cutoff and y == True])/len([[x, y] for [x, y] in data if y == True]))
    specificities.append(len([[x, y] for [x, y] in data if x <= cutoff and y == False])/len([[x, y] for [x, y] in data if y == False]))
    cutoff += 0.1
print(sensitivities, specificities)
