#!/usr/bin/env python
# coding: utf-8

# In[76]:


import random


# In[380]:


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


# In[323]:


blocks = ['a', 'b', 'c', 'd', 'floor']


# In[213]:


# testing

stack = Stack()
stack.display()
stack.move('a', 'b')
stack.display()
stack.move('c', 'b') # should fail
stack.display()
stack.move('c', 'a')
stack.display()
stack.move('d', 'c')
stack.display()
stack.move('d', 'floor')
stack.display()
stack.move('b', 'floor') # should fail
stack.display()


# In[214]:


# testing predicates
stack = Stack([['c'], ['b', 'a'], ['d']])
stack.display()
print(stack.on('a', 'floor'))
print(stack.on('a', 'b'))
print(stack.on('a', 'c'))
print(stack.is_on_top('a'))
print(stack.is_on_top('floor'))


# In[215]:


# “X is on the top of the stack containing Y”
def topofstackwith(env_lists, X, Y):
    stack = Stack(env_lists)
    return (X == Y and stack.is_on_top(X)) or any([stack.on(Z, Y) and topofstackwith(env_lists, X, Z) for Z in blocks])
def move(env_lists, X, Y):
    stack = Stack(env_lists)
    return topofstackwith(env_lists, Y, 'a') and stack.is_on_top(X) and X != Y


# In[180]:


# tests
env_lists = [['c'], ['b', 'a'], ['d']]
print(move(env_lists, 'c', 'a'))
print(move(env_lists, 'c', 'b'))


# In[87]:


# prints a portion of the (idealized) q-table

# incomplete list of all distinct block arrangements
stackings = [ [['a'], ['b'], ['c'], ['d']], [['a', 'b'], ['c'], ['d']], [['b', 'a'], ['c'], ['d']],
             [['a', 'c'], ['b'], ['d']], [['c', 'a'], ['b'], ['d']], [['b', 'c'], ['a'], ['d']],
             [['c', 'b'], ['a'], ['d']], [['a', 'd'], ['b'], ['c']], [['d', 'a'], ['b'], ['c']],
             [['b', 'd'], ['a'], ['c']], [['d', 'b'], ['a'], ['c']], [['c', 'd'], ['a'], ['b']],
             [['d', 'c'], ['a'], ['b']], [['a', 'b'], ['c', 'd']], [['b', 'a'], ['c', 'd']],
             [['a', 'b'], ['d', 'c']], [['b', 'a'], ['d', 'c']], [['a', 'c'], ['b', 'd']],
             [['c', 'a'], ['b', 'd']], [['a', 'c'], ['d', 'b']], [['c', 'a'], ['d', 'b']] ]
for s in stackings:
    print(s)
    stack = Stack(lists=s)
    for X in blocks:
        for Y in blocks:
            if stack.is_move_valid(X, Y):
                print("    move({}, {}) = {}".format(X, Y, move(X, Y)))


# In[382]:


gamma = 0.8

# function that takes a policy as input and plays according to the policy
# policy is a function from state -> action. In this case, an action is represented as a pair of blocks (X, Y)
# and is the action of moving X to Y.
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


# In[124]:


# policy that randomly chooses actions with uniform probabilities
# use rejection sampling to repeatedly sample actions until we get a valid action
def random_action(env):
    while True:
        i = random.randrange(5)
        j = random.randrange(5)
        stack = Stack(env)
        if stack.is_move_valid(blocks[i], blocks[j]):
            return (blocks[i], blocks[j])


# In[127]:


gen_episode(random_action)


# In[143]:


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


# In[275]:


# This code was refactored, see the next cell.
'''# Learn the Q-table by generating episodes repeatedly
# The output of this process should be a table mapping certain states to the value of each possible action.
stackings = [ [['a'], ['b'], ['c'], ['d']], [['a', 'b'], ['c'], ['d']], [['b', 'a'], ['c'], ['d']],
             [['a', 'c'], ['b'], ['d']], [['c', 'a'], ['b'], ['d']], [['b', 'c'], ['a'], ['d']],
             [['c', 'b'], ['a'], ['d']], [['a', 'd'], ['b'], ['c']], [['d', 'a'], ['b'], ['c']],
             [['b', 'd'], ['a'], ['c']], [['d', 'b'], ['a'], ['c']], [['c', 'd'], ['a'], ['b']],
             [['d', 'c'], ['a'], ['b']], [['a', 'b'], ['c', 'd']], [['b', 'a'], ['c', 'd']],
             [['a', 'b'], ['d', 'c']], [['b', 'a'], ['d', 'c']], [['a', 'c'], ['b', 'd']],
             [['c', 'a'], ['b', 'd']], [['a', 'c'], ['d', 'b']], [['c', 'a'], ['d', 'b']] ]
# Counter: a list of dictionaries mapping (X, Y) to the number of counts of move(X, Y).
# One dictionary for each state.
counter = []
for state in stackings:
    counter.append(dict())
# Qtable is similar, but it maps (X, Y) to the Q-value of move(X, Y).
Qtable = []
for state in stackings:
    Qtable.append(dict())

maxiter = 20000
for i in range(maxiter):
    (states, actions, rewards, returns) = gen_episode(random_action)
    for i, state in enumerate(stackings):
        # find state in states in last episode
        for j, s in enumerate(states):
            if s == None:
                break
            # check if s and state are equivalent; that is, one of them's columns can be permuted into the other's.
            if is_equivalent(s, state):
                ret = returns[j + 1]
                if actions[j] in counter[i]:
                    counter[i][actions[j]] += 1
                    Qtable[i][actions[j]] += ret
                else:
                    counter[i][actions[j]] = 1
                    Qtable[i][actions[j]] = ret
                break

# divide each value in Q by the number of ocurrences to get the average Q value
for i, Qstate in enumerate(Qtable):
    for act in Qstate:
        Qstate[act] /= counter[i][act]'''


# In[383]:


# Redid the above so that stackings gets built up as we go
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


# In[385]:


# Print the Q table.
for i, Qstate in enumerate(Qtable):
    print("State", stackings[i], ":")
    for act in sorted([*Qstate]):
        print("    move({}, {}) has value {}".format(act[0], act[1], Qstate[act]))


# In[386]:


import matplotlib.pyplot as plt

# In general, higher action values should correspond to actions that are part of the move() policy.
# First, refactor Q table into a single dictionary: (state_ID, X, Y) -> value
Qtable_dict = {}
for i, Qstate in enumerate(Qtable):
    for act in Qstate:
        Qtable_dict[(i, act[0], act[1])] = Qstate[act]
#print(Qtable_dict)

# Plot the values of random actions from Q table along a line
random_keys = random.sample(list(Qtable_dict), 50)
off_policy_values = []
on_policy_values = []
for key in random_keys:
    if move(stackings[key[0]], key[1], key[2]):
        on_policy_values.append(Qtable_dict[key])
    else:
        print("{} is on-policy with value {}".format(key, Qtable_dict[key]))
        off_policy_values.append(Qtable_dict[key])

plt.scatter(on_policy_values, [1]*len(on_policy_values), c="red")
plt.scatter(off_policy_values, [0]*len(off_policy_values), c="blue")


# In[388]:


print(stackings[19])
print(move([['a'], ['b', 'c', 'd']], 'd', 'a'))


# In[392]:


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
plt.scatter([1 - x for x in specificities], sensitivities)


# In[393]:


print(data)


# In[398]:


# Do a run from a randomly chosen (?) starting state to see if it makes the correct moves
state = stackings[random.randrange(len(stackings))]
# We need to choose a state where 'a' is on the bottom of some stack, in order to succeed.
while not any([x[0] == 'a' for x in state]):
    state = stackings[random.randrange(len(stackings))]
print(state)
stack = Stack(state)
while True:
    try: i = stackings.index(state)
    except:
        print("Q table never learned action for state {}".format(state))
        break
    action, value = max(list(Qtable[i].items()), key=lambda x: x[1])
    print("Action {} chosen.".format(action))
    print("Is it on policy? {}".format("yes" if move(state, action[0], action[1]) else "no"))
    reward, done = stack.move(action[0], action[1])
    state = stack.get_env_as_lists()
    state = normalize(state)
    print(state)
    if done:
        break


# In[362]:


# print results for a particularly difficult scenario to learn the move() policy
i = stackings.index([['a'], ['c', 'b', 'd']])
print(list(Qtable[i].items()))
# Results from one run, taken with gamma = 0.8:
'''
[(('d', 'a'), 1.682455162240256),
 (('a', 'floor'), 1.0936110261197),
 (('a', 'd'), 8.0),
 (('d', 'floor'), -0.7827707054569227)]
 '''
# Notice how the value of Q(d, a) < 2 and Q(a, d) = 8 even though Q(d, a) is on policy.
# Results from another run, taken with gamma = 0.95:
'''
[(('a', 'd'), 9.5),
 (('d', 'a'), 4.79865991238065),
 (('a', 'floor'), 3.9532168320682732),
 (('d', 'floor'), -0.09727543962572971)]
'''
# Still better but they have a ways to go before learning that ('d', 'a') is better.
# Great news! After I built my Q table the second time with the "half-greedy, half-randomized" policy,
# the action (d, a) is successfully recognized as the optimal action!


# In[356]:


# Re-learn the Q table, this time with a policy that takes the optimal action half of the time
# and otherwise a random action.

old_Qtable = Qtable
old_stackings = stackings
def half_greedy(env):
    r = random.randrange(0, 2)
    if r == 0:
        # choose random action
        return random_action(env)
    if r == 1:
        # choose optimal action
        state = normalize(env)
        try:
            i = old_stackings.index(state)
            action, value = max(list(old_Qtable[i].items()), key=lambda x: x[1])
            return action
        except:
            return random_action(env)

stackings = []
# Counter: a list of dictionaries mapping (X, Y) to the number of counts of move(X, Y).
# One dictionary for each state.
counter = []
# Qtable is similar, but it maps (X, Y) to the Q-value of move(X, Y).
Qtable = []

maxiter = 20000
for h in range(maxiter):
    (states, actions, rewards, returns) = gen_episode(half_greedy)
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

# After you finish this, retry running the game from random start states. It should choose on-policy actions most of the time.


# In[ ]:


Idea for redesigning Q table statistics collection.
Generate episode.
reached_states = []
Iterate through all states that occur in the episode. For each state:
    Change to canonical form
    check for presense in stackings
    if not in stackings, add it.
    Add new empty dictionaries to counter and Qtable as appropriate
    check for presense in reached_states
    if not, add it. also tally value in Qtable and count in counter.
    if it is already in reached_states, continue.


# In[399]:


print(Qtable) # to extract


# In[400]:


print(stackings)


# In[ ]:




