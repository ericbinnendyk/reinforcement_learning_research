from blockworldupdatedagain import BlockWorldNewEnv2
import pickle
import os
import time
import numpy as np 
clear = lambda: os.system("cls")

size = int(input("SIZE? -- "))
env = BlockWorldNewEnv2(size)
env.reset()

max_steps_per_episode = 2 * (size * (size + 1))

with open("Qtable" + str(size) + ".npy", "rb") as f:
	q_table = np.load(f, allow_pickle=True)
with open("Dict" + str(size) + ".pkl", "rb") as f:
	states = pickle.load(f)

for episode in range(3):
	state = env.reset()
	done = False
	clear()
	print("EPISODE", episode + 1)
	time.sleep(2)

	for step in range(max_steps_per_episode):
		clear()
		env.render()
		
		action = np.argmax(q_table[states[str(state)],:].astype(int))
		print("ACTION", action)
		new_state, reward, done, info = env.step(action)
		print("REWARD", reward)
		time.sleep(3)

		if done:
			print("\nDONE")
			env.render()
			time.sleep(10)
			break

		state = new_state

env.close()
