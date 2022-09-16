import gym 
import random 
import numpy as np 

from gym.spaces import Discrete, Tuple, Box
from gym.utils import seeding

class BlockWorldNewEnv2(gym.Env):
		def __init__(self, size = 4, endsize = 4, stacks = 4):

			# Number of blocks in enviorment 
			self.numblocks = size

			self.previous = -1

			# Number of stacks in enviorment 
			self.numstacks = stacks

			# Action space is a tuple of (block, stack)
			# Stack... + End Stack
			self.action_space = Discrete(self.numblocks * self.numblocks)

			self.actions = []

			for i in range(0, self.numblocks):
				for x in range(0, self.numblocks):
					self.actions.append((i, x))

			print(self.actions)

			# observation space is a tuple of tuples of discrete
			obsspace = "self.observation_space = Tuple(["
			for i in range(0, self.numstacks):
				obsspace += "Tuple(["
				for x in range(0, self.numblocks):
					obsspace += "Discrete(self.numblocks+1)"
					if x != self.numblocks-1:
						obsspace += ", "
					else:
						obsspace += "])"
				if i != self.numstacks:
					obsspace += ", "
			obsspace += "])"
			exec(obsspace)

		def reset(self):
			self.generateState()
			finalTuple = self.obsformat()

			return finalTuple

		def generateState(self):
			self.enviorment = []

			for i in range(0, self.numstacks):
				self.enviorment.append([])

			options = []
			for i in range(0, self.numblocks):
				options.append(i)

			while len(options) != 0:
				choice = random.choice(options)
				options.remove(choice)
				# Change this for scalability
				self.enviorment[random.randint(0, self.numblocks-1)].append(choice)

		def obsformat(self):
			obs = []
			table = []

			for i in range(0, len(self.enviorment)-1):
				obs.append([])
				for x in range(0, self.numblocks):
					if x < len(self.enviorment[i]):
						obs[i].append(self.enviorment[i][x])
					else:
						obs[i].append(6)

			for i in range(0, self.numblocks):
				if i < len(self.enviorment[len(self.enviorment)-1]):
					table.append(self.enviorment[len(self.enviorment)-1][i])
				else:
					table.append(6)

			for i in range(0, len(obs)):
				obs[i] = tuple(obs[i])

			obs = sorted(obs)
			obs.append(table)
			obs = tuple(obs)
			return obs

		def step(self, action):

			done = False
			reward = 0
			maxlen = 0
			blockindex = -1
			destinationindex = -1

			block = self.actions[action][0]
			destination = self.actions[action][1]

			for x in range(0, len(self.enviorment)):
						if (len(self.enviorment[x]) != 0) and (self.enviorment[x][len(self.enviorment[x]) - 1] == destination):
							destinationindex = x

			for x in range(0, len(self.enviorment)):
						if (len(self.enviorment[x]) != 0) and (block in self.enviorment[x]):
							blockindex = x

			if block == destination:
				self.enviorment[len(self.enviorment)-1].append(block)
				self.enviorment[blockindex].remove(block)
			else:
				self.enviorment[blockindex].remove(block)
				self.enviorment[destinationindex].append(block)
			

			for i in range(0, len(self.enviorment)):
				if len(self.enviorment[i]) > maxlen:
					maxlen = len(self.enviorment[i])

			reward += maxlen

			for i in range(0, len(self.enviorment)-1):
				if len(self.enviorment[i]) == self.numblocks:
					reward += 1000
					done = True

			finalTuple = self.obsformat()

			return finalTuple, reward, done, {}

		def render(self):
			for x in range(0, self.numblocks):
				line = "print(\""
				for i in range(0, len(self.enviorment)):
					if self.numblocks-1-x < len(self.enviorment[i]):
						line += "[" + str(self.enviorment[i][self.numblocks-1-x]) + "]"
					else:
						line += "[ ]"
				line += "\")"
				exec(line)
