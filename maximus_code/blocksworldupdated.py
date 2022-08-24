import gym 
import random 
import numpy as np 
np.set_printoptions(threshold=np.inf)

from gym.spaces import Discrete, Tuple, Box
from gym.utils import seeding
from tqdm import tqdm

class BlockWorldNewEnv(gym.Env):
	def __init__(self, size = 4, stacks = 4, endsize = 4):

		self.previousaction = ()

		# Number of blocks in enviorment 
		self.numblocks = size

		# Number of blocks in goal
		self.endsize = endsize

		# Number of stacks in enviorment 
		self.numstacks = stacks

		# Action space is a tuple of (block, stack)
		# Stack... + End Stack
		self.action_space = Tuple([Discrete(self.numblocks), Discrete(self.numstacks + 1)])

		# observation space is a tuple of tuples of discrete
		obsspace = "self.observation_space = Tuple([Tuple(["
		for i in range(0, self.endsize):
			obsspace += "Discrete(self.numblocks+1)"
			if i != self.endsize-1:
				obsspace += ", "
		obsspace += "]), "
		for i in range(0, self.numstacks):
			obsspace += "Tuple(["
			for x in range(0, self.numblocks):
				obsspace += "Discrete(self.numblocks+1)"
				if x != self.numblocks-1:
					obsspace += ", "
				else:
					obsspace += "])"
			if i != self.numstacks-1:
				obsspace += ", "
		obsspace += "])"

		exec(obsspace)
		
	def step(self, action):

		reward = 0
		reward -= 5

		if action == self.previousaction:
			reward -= 10

		# find index as long as its not in the end stack and on top
		# move to index stated		
		for i in range(0, len(self.enviorment)-1):
			if (len(self.enviorment[i]) != 0) and (self.enviorment[i][len(self.enviorment[i])-1] == action[0]):
				self.enviorment[action[1]].append(self.enviorment[i][len(self.enviorment[i])-1])
				self.enviorment[i].remove(action[0])
				break
			elif (len(self.enviorment[i]) > 1):
				for x in range(0, len(self.enviorment[i]) - 2):
					if self.enviorment[i][x] == action[0]:
						reward -= 3


		for i in range(0, len(self.enviorment[len(self.enviorment) -1])):
			if self.enviorment[len(self.enviorment)-1][i] == self.goal[i]:
				reward += 3

		if len(self.enviorment[len(self.enviorment)-1]) == len(self.goal):
			reward += 10
			done = True
		else:
			done = False

		finalTuple = self.obsformat()
		self.previousaction = action

		return finalTuple, reward, done, {}

	def reset(self):
		self.generateState()
		finalTuple = self.obsformat()

		return finalTuple

	def render(self):
		for x in range(0, self.numblocks):
			line = "print(\""
			for i in range(0, len(self.enviorment)):
				if self.numblocks-1-x < len(self.enviorment[i]):
					line += "[" + str(self.enviorment[i][self.numblocks-1-x]) + "]"
				else:
					line += "[ ]"
			line += "[" + str(self.goal[self.numblocks-1-x]) + "]"
			line += "\")"
			exec(line)

	def generateState(self):
		self.goal = []
		self.enviorment = []

		for i in range(0, self.numstacks + 1):
			self.enviorment.append([])

		options = []
		for i in range(0, self.numblocks):
			options.append(i)

		while len(options) != 0:

			choice = random.choice(options)
			options.remove(choice)

			if len(self.goal) != self.endsize:
				self.goal.append(choice)

			self.enviorment[random.choice([0, 1, 2, 3])].append(choice)

	def obsformat(self):
		obs = []
		observe = []
		goalTuple = []
		finalTuple = []

		for i in range(0, len(self.enviorment)):
			obs.append([])
			for x in range(0, self.numblocks):
				if x < len(self.enviorment[i]):
					obs[i].append(self.enviorment[i][x])
				else:
					obs[i].append(6)

		for i in range(0, len(self.enviorment)):
			observe.append([])
			for x in range(0, len(obs[i])):
				observe[i].append(obs[i][x])

		for i in range(0, len(observe)):
			observe[i] = tuple(observe[i])

		for i in range(0, len(self.goal)):
			goalTuple.append(self.goal[i])

		goalTuple = tuple(goalTuple)

		observe = tuple(observe)

		finalTuple.append(goalTuple)
		for i in range(0, len(observe)):
			finalTuple.append(observe[i])

		finalTuple = tuple(finalTuple)

		return finalTuple
