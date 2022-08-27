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
			self.action_space = Discrete(self.numblocks * self.numblocks - 4)

			self.actions = []

			for i in range(0, self.numblocks):
				for x in range(0, self.numblocks):
					if i == x:
						x += 1
					self.actions.append((i, x))

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
				if i != self.numstacks-1:
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
				self.enviorment[random.choice([0, 1, 2, 3])].append(choice)

		def obsformat(self):
			obs = []

			for i in range(0, len(self.enviorment)):
				obs.append([])
				for x in range(0, self.numblocks):
					if x < len(self.enviorment[i]):
						obs[i].append(self.enviorment[i][x])
					else:
						obs[i].append(6)

			for i in range(0, len(obs)):
				obs[i] = tuple(obs[i])

			obs = sorted(obs)
			obs = tuple(obs)

			return obs

		def step(self, action):

			done = False
			reward = 0
			maxlen = 0

			block = self.actions[action][0]
			destination = self.actions[action][1]

			# find index as long as its not in the end stack and on top
			# move to index stated		
			for i in range(0, len(self.enviorment)):
				if (len(self.enviorment[i]) != 0) and (self.enviorment[i][len(self.enviorment[i])-1] == block):
					for x in range(0, len(self.enviorment)):
						if (len(self.enviorment[x]) != 0) and (self.enviorment[x][len(self.enviorment[x]) - 1] == destination):
							self.enviorment[i].remove(block)
							self.enviorment[x].append(block)

			for i in range(0, len(self.enviorment)):
				if len(self.enviorment[i]) > maxlen:
					maxlen = len(self.enviorment[i])

			reward += maxlen

			for i in range(0, len(self.enviorment)):
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
