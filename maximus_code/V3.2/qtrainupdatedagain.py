from blockworldupdatedagain import BlockWorldNewEnv2
import gym 
import random
import numpy as np 
import pickle
from tqdm import tqdm
np.set_printoptions(threshold=np.inf)

size = int(input("SIZE -- "))
env = BlockWorldNewEnv2(size)
env.reset()

action_space_size = env.action_space.n
state_space_size = 10000000

q_table = np.zeros((state_space_size, action_space_size))

num_episodes = 10000
max_steps_per_episode = 100

learning_rate = 0.1
discount_rate = 0.99

exploration_rate = 0.1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.001

rewards_all = []

states = {}
tots = 0

for episode in tqdm(range(num_episodes)):
	state = env.reset()
	done = False
	rewards_current_episode = 0

	for step in range (max_steps_per_episode):
		if str(state) in states.keys():
			StateIndex = states[str(state)]
		else:
			states[str(state)] = tots
			StateIndex = states[str(state)]
			tots += 1

		exploration_rate_threshold = random.uniform(0, 1)

		if exploration_rate_threshold > exploration_rate:
			action = np.argmax(q_table[StateIndex,:])
		else:
			action = env.action_space.sample()

		new_state, reward, done, info = env.step(action)

		if str(new_state) in states.keys():
			new_state_index = states[str(new_state)]
		else:
			states[str(new_state)] = tots
			new_state_index = states[str(new_state)]
			tots += 1

		q_table[StateIndex, action] = q_table[StateIndex, action] * (1 - learning_rate) + learning_rate * (reward + (discount_rate * np.max(q_table[new_state_index, :])))

		state = new_state
		rewards_current_episode += reward

		if done == True:
			break

	exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(-exploration_decay_rate*episode)
	rewards_all.append(rewards_current_episode)

print(len(q_table))

q_table = np.resize(q_table, (len(states), action_space_size))

print(len(q_table))

rewards_per_thousand_episodes = np.split(np.array(rewards_all), num_episodes/100)
count = 1000
print("AVERAGE REWARD PER THOUSAND EPISODES")
for r in rewards_per_thousand_episodes:
	print(count, ":", str(sum(r/1000)))
	count += 1000

with open("Qtable" + str(size) + ".npy", "wb") as f:
	np.save(f, q_table)

with open("Dict" + str(size) + ".pkl", "wb") as f:
	pickle.dump(states, f)