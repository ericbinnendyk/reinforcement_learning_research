from blocksworldupdated import BlockWorldNewEnv
import gym 
import random
import numpy as np 
import pickle
from tqdm import tqdm
np.set_printoptions(threshold=np.inf)

size = int(input("SIZE -- "))
env = BlockWorldNewEnv(size)
env.reset()

action_space_size = size * (size + 1)
state_space_size = 10000000

q_table = np.zeros((state_space_size, action_space_size))

num_episodes = 10000
max_steps_per_episode = 100

learning_rate = 0.1
discount_rate = 0.99

exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.001
exploration_decay_rate = 0.001

rewards_all = []

states = {}
actions = {}

totalStates = 0
totalActions = 0

stateIndex = -1
newStateIndex = -1
actionIndex = -1

num = -1

for episode in tqdm(range(num_episodes)):
	state = env.reset()

	done = False
	rewards_current_episode = 0

	for step in range(max_steps_per_episode):
		if str(state) in states.keys():
			StateIndex = states[str(state)]
		else:
			states[str(state)] = totalStates
			StateIndex = totalStates
			totalStates += 1

		exploration_rate_threshold = random.uniform(0, 1)

		if exploration_rate_threshold < exploration_rate:
			try:
				action = actions[np.argmax(q_table[StateIndex,:].astype(int))]
			except:
				action = env.action_space.sample()
				actions[totalActions] = action
				totalActions += 1
		else:
			action = env.action_space.sample()
			actions[totalActions] = action
			totalActions += 1

		new_state, reward, done, info = env.step(tuple(action))

		if str(new_state) in states.keys():
			newStateIndex = states[str(new_state)]
		else:
			states[str(new_state)] = totalStates
			newStateIndex = totalStates
			totalStates += 1

		q_table[StateIndex, action] = q_table[StateIndex, action] * (1 - learning_rate) + learning_rate * (reward + discount_rate * np.max(q_table[newStateIndex, :]))

		state = new_state
		rewards_current_episode += reward

		if done == True:
			break

	exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate*episode)
	rewards_all.append(rewards_current_episode)

q_table = np.resize(q_table, (len(states), action_space_size))
print("Q Table size after resize: ", len(q_table))

rewards_per_thousand_episodes = np.split(np.array(rewards_all), num_episodes/100)
count = 100

print("AVERAGE REWARD PER THOUSAND EPISODES")
for r in rewards_per_thousand_episodes:
	print(count, ":", str(sum(r/100)))
	count += 100

with open("Qtable" + str(size) + ".npy", "wb") as f:
	np.save(f, q_table)

with open("SDict" + str(size) + ".pkl", "wb") as f:
	pickle.dump(states, f)

with open("ADict" + str(size) + ".pkl", "wb") as f:
	pickle.dump(actions, f)