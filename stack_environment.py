# Setup of stack environment, for use as a library function

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


