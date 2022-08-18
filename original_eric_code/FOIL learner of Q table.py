#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This is an attempt to use the FOIL learning algorithm to learn a logical predicate from data about which moves to make.


# In[ ]:


# import results from previous


# In[1]:


stackings = [[['a'], ['b'], ['c'], ['d']], [['a'], ['b'], ['c', 'd']], [['a'], ['c'], ['b', 'd']], [['a'], ['d'], ['b', 'c']], [['a'], ['b', 'c', 'd']], [['d'], ['b', 'c', 'a']], [['a'], ['b'], ['d', 'c']], [['b'], ['d'], ['a', 'c']], [['b'], ['a', 'c', 'd']], [['b', 'c'], ['d', 'a']], [['b'], ['d'], ['c', 'a']], [['b'], ['c'], ['d', 'a']], [['c', 'b'], ['d', 'a']], [['a'], ['d'], ['c', 'b']], [['a', 'd'], ['c', 'b']], [['b'], ['c'], ['a', 'd']], [['b'], ['a', 'd', 'c']], [['a', 'd'], ['b', 'c']], [['a'], ['c', 'd', 'b']], [['a', 'b'], ['c', 'd']], [['c'], ['a', 'd', 'b']], [['c'], ['d'], ['a', 'b']], [['a', 'c'], ['b', 'd']], [['a'], ['b', 'd', 'c']], [['d'], ['a', 'c', 'b']], [['a', 'b'], ['d', 'c']], [['a'], ['d', 'c', 'b']], [['b', 'a'], ['d', 'c']], [['b'], ['d', 'c', 'a']], [['d'], ['b', 'a', 'c']], [['c'], ['d'], ['b', 'a']], [['b'], ['c', 'a', 'd']], [['a', 'c'], ['d', 'b']], [['a'], ['d', 'b', 'c']], [['a'], ['c'], ['d', 'b']], [['c'], ['b', 'a', 'd']], [['d'], ['a', 'b', 'c']], [['b', 'd'], ['c', 'a']], [['b', 'a'], ['c', 'd']], [['b'], ['c', 'd', 'a']], [['c'], ['d', 'a', 'b']], [['a'], ['c', 'b', 'd']], [['c'], ['a', 'b', 'd']], [['b'], ['d', 'a', 'c']], [['d'], ['c', 'a', 'b']], [['c', 'a'], ['d', 'b']], [['c'], ['d', 'b', 'a']], [['c'], ['b', 'd', 'a']], [['d'], ['c', 'b', 'a']]]


# In[2]:


Qtable = [{('d', 'c'): -0.8799224863146268, ('a', 'c'): -1.7594868650307736, ('b', 'c'): -1.1898012699240088, ('d', 'a'): 1.1147301159233773, ('c', 'a'): 0.9854028484952575, ('a', 'b'): -1.7006054795697512, ('d', 'b'): -0.8887839152885366, ('a', 'floor'): -1.5535169337431274, ('c', 'floor'): -1.7952527419380173, ('c', 'd'): -0.7228191450461644, ('b', 'd'): -1.0631639331635185, ('b', 'a'): 0.7477291547026269, ('c', 'b'): -0.9387440790325181, ('a', 'd'): -1.7333048672022264, ('b', 'floor'): -1.681999463919989, ('d', 'floor'): -1.3884588896363736}, {('d', 'b'): -0.8864937732721014, ('b', 'd'): 1.1109808268398145, ('d', 'floor'): -1.251674445207576, ('a', 'd'): 0.4248564738660709, ('a', 'b'): -1.3026086298692725, ('b', 'a'): 1.48048770343943, ('d', 'a'): 1.345009590192296, ('a', 'floor'): -0.9116794848452175, ('b', 'floor'): -1.4858117397757484}, {('a', 'floor'): -0.9404507043285735, ('c', 'a'): 1.2482103426611557, ('c', 'd'): 1.1705611678085306, ('d', 'floor'): -1.5689116659935554, ('c', 'floor'): -0.9318149018904767, ('a', 'd'): 0.3292042216328679, ('d', 'a'): 1.1118387858223284, ('d', 'c'): -1.1430090434455775, ('a', 'c'): -1.3108655322774134}, {('d', 'c'): 1.0207393479438083, ('a', 'floor'): -0.8577431519649532, ('c', 'd'): -1.0536713759182934, ('d', 'floor'): -0.9467989578574356, ('c', 'a'): 1.2198301654853891, ('d', 'a'): 1.5721278023131025, ('a', 'd'): -1.2078046765651884, ('a', 'c'): 0.6869402587817769, ('c', 'floor'): -1.4584273409501007}, {('d', 'floor'): -0.8216489715690515, ('d', 'a'): 1.4477538005262787, ('a', 'floor'): 1.1209583914492536, ('a', 'd'): 8.0}, {('a', 'floor'): -0.9484297832353179, ('d', 'a'): 8.0, ('a', 'd'): -1.0792633341532918, ('d', 'floor'): 0.6894939295686853}, {('c', 'a'): 0.40418466349391785, ('a', 'floor'): -0.6933820184750966, ('c', 'floor'): -1.5089166388074415, ('a', 'c'): 0.6080298020426369, ('b', 'a'): 1.2212154814547005, ('b', 'floor'): -0.5958399156921439, ('b', 'c'): 1.0284532523447862, ('c', 'b'): -0.7452341482288629, ('a', 'b'): -1.424249739631268}, {('d', 'c'): 9.521296085661094, ('b', 'floor'): 0.5461336462992137, ('b', 'c'): 10.222911455043258, ('b', 'd'): 2.091016170358899, ('c', 'b'): -0.7354526360441522, ('d', 'floor'): 0.8535379392664565, ('c', 'd'): -1.1828491558095546, ('c', 'floor'): -1.442324717590437, ('d', 'b'): 1.2064187771300494}, {('d', 'floor'): 1.437277729311004, ('d', 'b'): 0.8347152373900951, ('b', 'd'): 40.0, ('b', 'floor'): 10.834466526856456}, {('a', 'c'): 0.41888160609786357, ('c', 'a'): 0.3091179106937471, ('a', 'floor'): -0.9321832947626368, ('c', 'floor'): -1.7074459400499253}, {('a', 'floor'): -1.5758417177145, ('b', 'floor'): -1.6401346303251654, ('b', 'a'): 0.34482988554677246, ('a', 'b'): -1.5955232249434697, ('d', 'b'): -1.2543124436179824, ('d', 'floor'): -1.7086932801369772, ('a', 'd'): -1.6163135371086161, ('d', 'a'): -0.09295204242096956, ('b', 'd'): -1.0101581325539346}, {('b', 'c'): -1.2865439238639376, ('b', 'floor'): -1.7150959475768142, ('c', 'a'): 0.3201086176935008, ('a', 'c'): -1.6246368866637622, ('a', 'floor'): -1.3721598934974593, ('c', 'b'): -1.1617642155702528, ('b', 'a'): 0.37234518501953434, ('c', 'floor'): -1.6993952350302688, ('a', 'b'): -1.9253488741998985}, {('a', 'floor'): -0.8340757963219905, ('b', 'a'): 0.3324500853191201, ('b', 'floor'): -1.7061256196120704, ('a', 'b'): 0.3161877532458175}, {('a', 'd'): -1.1297365165942448, ('a', 'floor'): -0.7793841505001238, ('d', 'floor'): -0.991531107645212, ('d', 'a'): 1.3912017932762275, ('b', 'd'): -0.7784450747781514, ('d', 'b'): 0.9220742697120963, ('b', 'a'): 0.6308239485612576, ('a', 'b'): 0.27453413776305197, ('b', 'floor'): -1.6917420707586104}, {('b', 'floor'): 0.8232216898519765, ('d', 'floor'): -1.0304117551177383, ('b', 'd'): 9.642921170403714, ('d', 'b'): 1.1903274473871508}, {('b', 'floor'): 0.9817183602060555, ('d', 'c'): -0.9873574681624465, ('c', 'b'): 2.3531800319885545, ('c', 'floor'): 0.5721031296580745, ('d', 'b'): -0.946454030999512, ('b', 'c'): 1.660823699154336, ('d', 'floor'): -1.4391653191929916, ('c', 'd'): 9.3246713322399, ('b', 'd'): 9.577141385779282}, {('c', 'floor'): 1.21335146029564, ('c', 'b'): 1.2242934126849898, ('b', 'c'): 40.0, ('b', 'floor'): 10.655024594852184}, {('c', 'd'): 11.095821119602286, ('d', 'c'): 1.2959644287510266, ('c', 'floor'): 0.8813248983063288, ('d', 'floor'): -0.8787029214155803}, {('b', 'a'): 1.0194440946377903, ('a', 'floor'): 1.1924954282679505, ('a', 'b'): 8.0, ('b', 'floor'): -0.9553345324829037}, {('b', 'floor'): -0.8053371041199718, ('d', 'floor'): 0.4393553739199318, ('b', 'd'): 0.9211319724981434, ('d', 'b'): 9.734894167322095}, {('c', 'b'): 40.0, ('b', 'c'): 1.8461896340161583, ('b', 'floor'): 1.3481608970383, ('c', 'floor'): 9.960777382886754}, {('b', 'c'): -0.8241379819528873, ('c', 'b'): 9.158816677757994, ('d', 'floor'): 1.0453563556051826, ('c', 'd'): 1.83684266660077, ('b', 'floor'): -1.5379167740526807, ('b', 'd'): -0.7416255281771839, ('c', 'floor'): 0.9236611565174873, ('d', 'c'): 1.4291995565894888, ('d', 'b'): 9.187501941083895}, {('c', 'd'): 0.7350828845610519, ('d', 'floor'): 1.488958356907042, ('c', 'floor'): -0.7993638384902618, ('d', 'c'): 9.103836279745769}, {('a', 'floor'): 1.5281549924811593, ('a', 'c'): 8.0, ('c', 'a'): 0.7797527980190152, ('c', 'floor'): -0.8426149255628714}, {('b', 'floor'): 1.4939797212026527, ('b', 'd'): 2.0473505501631983, ('d', 'floor'): 10.537822383535927, ('d', 'b'): 40.0}, {('b', 'c'): 1.1835096233734093, ('c', 'b'): 10.164559862919779, ('b', 'floor'): -0.8722200077200777, ('c', 'floor'): 1.271702866026981}, {('b', 'floor'): -1.0282215272848985, ('a', 'b'): 8.0, ('b', 'a'): 1.6321529417607554, ('a', 'floor'): 1.3702735846789462}, {('a', 'c'): 0.32339627450659136, ('c', 'floor'): -1.8294652043715673, ('c', 'a'): 0.3585206161310635, ('a', 'floor'): -0.8503068779682683}, {('a', 'floor'): -0.7232899523119348, ('a', 'b'): -1.0814623322924488, ('b', 'floor'): 0.20360792947515555, ('b', 'a'): 8.0}, {('d', 'floor'): 0.3041907292756712, ('c', 'd'): -1.417168467487255, ('c', 'floor'): -1.6938144215371504, ('d', 'c'): 8.0}, {('c', 'a'): -0.05276624940533462, ('d', 'a'): 0.38887499363515143, ('c', 'floor'): -1.6766553589305926, ('a', 'd'): -1.6196706265260603, ('d', 'floor'): -1.634526770202357, ('c', 'd'): -0.9845570429889066, ('d', 'c'): -1.1146452198124506, ('a', 'c'): -1.7301602683497974, ('a', 'floor'): -1.4960553196511224}, {('b', 'floor'): 0.17496212649345327, ('b', 'd'): 8.0, ('d', 'b'): -1.5217364192046563, ('d', 'floor'): -1.4014914411917265}, {('c', 'b'): 1.0752042896666754, ('b', 'c'): 9.764544065016109, ('b', 'floor'): 1.3335342397160836, ('c', 'floor'): -0.7770658510587254}, {('c', 'floor'): -0.9778406208205173, ('a', 'floor'): 1.120978075356336, ('a', 'c'): 8.0, ('c', 'a'): 1.2914811042047687}, {('b', 'c'): -1.309720047409194, ('b', 'a'): 1.170893252976232, ('c', 'b'): 1.103201300940079, ('c', 'floor'): -0.8705592415673278, ('a', 'c'): -1.089336642950644, ('c', 'a'): 1.6092586046259905, ('a', 'b'): 0.493899031319318, ('a', 'floor'): -0.9111275596384402, ('b', 'floor'): -1.5085670591779088}, {('c', 'd'): 8.0, ('d', 'c'): -1.3617766906804698, ('c', 'floor'): 0.3807831603495104, ('d', 'floor'): -1.5997789604488233}, {('c', 'd'): 1.224585818629204, ('d', 'c'): 40.0, ('d', 'floor'): 9.708744225529776, ('c', 'floor'): 1.0988441419785984}, {('a', 'floor'): -1.1892748335900223, ('a', 'd'): 0.2454530803687117, ('d', 'floor'): -1.7516269978436334, ('d', 'a'): 0.2883450618697719}, {('a', 'floor'): -1.0237536630069843, ('d', 'floor'): -1.7006852629295346, ('a', 'd'): 0.3120697273770399, ('d', 'a'): 0.20598138595442217}, {('a', 'b'): -1.3335396683136866, ('a', 'floor'): -0.9987855348221111, ('b', 'floor'): 0.3873673037484177, ('b', 'a'): 8.0}, {('c', 'floor'): 0.26960067985773173, ('b', 'c'): -0.8317565297746382, ('c', 'b'): 8.0, ('b', 'floor'): -1.6068420876900629}, {('a', 'floor'): 0.8688225522019892, ('a', 'd'): 8.0, ('d', 'a'): 1.0609539452352688, ('d', 'floor'): -1.1515964466753583}, {('d', 'floor'): 1.347612314328975, ('d', 'c'): 1.3282490879088955, ('c', 'floor'): 10.429193035878061, ('c', 'd'): 40.0}, {('c', 'floor'): -1.6494055456799004, ('b', 'c'): 7.982683982683983, ('b', 'floor'): 0.5851461605524686, ('c', 'b'): -1.1367236766843558}, {('b', 'floor'): -1.7101630150003022, ('b', 'd'): -0.9260223009357824, ('d', 'b'): 8.0, ('d', 'floor'): 0.3297110564140052}, {('a', 'b'): 0.656055791839485, ('b', 'floor'): -1.8269026409501066, ('b', 'a'): 0.4776400563060801, ('a', 'floor'): -0.6220544527559453}, {('c', 'a'): 8.0, ('a', 'floor'): -0.834305509432251, ('a', 'c'): -0.866621176246276, ('c', 'floor'): 0.4351091953951895}, {('a', 'c'): -1.0358959909215573, ('a', 'floor'): -1.197414893177425, ('c', 'floor'): 0.20983200041220956, ('c', 'a'): 8.0}, {('d', 'floor'): 0.13388978299010448, ('d', 'a'): 8.0, ('a', 'd'): -0.9933600134692215, ('a', 'floor'): -0.9247237070878128}]


# In[3]:


blocks = ['a', 'b', 'c', 'd', 'floor']


# In[4]:


def location(state, X):
    for i, col in enumerate(state):
        if X in col:
            colnum = i
            rownum = 3 - col.index(X)
            return (rownum, colnum)
    return (-1, -1)


# In[5]:


def on(state, X, Y):
    if (location(state, X)[0] == 3 and Y == 'floor'):
        return True
    if (location(state, X)[0] == location(state, Y)[0] - 1 and location(state, X)[1] == location(state, Y)[1]):
        return True
    return False


# In[6]:


def top(state, X):
    if X == 'floor':
        return False
    loc = location(state, X)
    return len(state[loc[1]]) == 4 - loc[0]


# In[7]:


def isFloor(stack, X):
    return X == 'floor'


# In[ ]:


'''# Use FOIL (?) to learn
# Next step: Review tutorials to see if this is actually FOIL. I'm still not fully getting it.
primitives = ['on', 'top', 'isFloor', 'neq']
variables = ['X', 'Y', 'a']
current_clause = []
while True:
    see what fraction of the results the current clause satisfies
    for new_predicate in <all possible combinations of primitives and variables, as well as a new free variable>
        store the info_gain of current_clause + new predicate
    see which predicate provides the highest info_gain, and add that.
    add a new variable to variables as needed.

what are "positive bindings" and "negative bindings" of a clause?
formula given in video: log(p1/(p1 + n1)) - log(p0/(p0 + n0))
maybe it means "settings of variables [implicitly meaning those that satisfy the actual goal] that yield true resp. false for the working clause"
'''


# In[8]:


# functions for testing a non-recursive predicate
def test_with_unbounded_variables(state, and_conj, X, Y, unbounded_vars, assignments):
    def test_single_literal(state, lit, X, Y): # Y == None if the literal just requires one argument
        if lit == 'on':
            return on(state, X, Y)
        if lit == 'top':
            return top(state, X)
        if lit == 'isFloor':
            return isFloor(state, X)
        if lit == 'neq':
            return X != Y
        print("Error: literal contains invalid predicate which is {}".format(lit))
        input()
        return

    # Converts a string representing a variable to the value of the variable
    def var_to_value(v_str):
        if v_str == 'X':
            return X
        if v_str == 'Y':
            return Y
        if v_str == 'a':
            return 'a'
        if v_str in unbounded_vars and unbounded_vars.index(v_str) < len(assignments):
            return assignments[unbounded_vars.index(v_str)]
        print("Error: variable {} is not bound to value in test".format(v_str))
        return

    results = []
    # Go through all predicates that use only X, Y, and the values from unbounded_vars. Check whether each of them is true.
    for literal in and_conj:
        if all([v in ['X', 'Y', 'a'] or v in unbounded_vars[:len(assignments)] for v in literal[1:]]):
            var1 = var_to_value(literal[1])
            var2 = var_to_value(literal[2]) if len(literal) > 2 else None
            results.append(test_single_literal(state, literal[0], var1, var2))
            #print("result for", literal, "is", results[-1])
    if len(unbounded_vars) == len(assignments):
        # assignment of variables is complete
        #print("Complete assignment {} = {} may or may not satisfy predicate.".format(unbounded_vars, assignments))
        return all(results)
    elif all(results):
        # assignment is not complete but current partial assignment is logically consistent
        #print("Partial assignment {} = {} is consistent".format(unbounded_vars, assignments))
        for new_assignment in blocks:
            if test_with_unbounded_variables(state, and_conj, X, Y, unbounded_vars, assignments + [new_assignment]):
                #print("Predicate {} is satisfied with assignment {} = {}".format(and_conj, unbounded_vars, assignments + [new_assignment]))
                return True
        return False
    else:
        #print("Partial assignment {} = {} is not even consistent".format(unbounded_vars, assignments))
        return False

# Takes in a state, a clause, and some variable assignments and checks if the clause is true
def test(state, and_conj, X, Y):
    def test_single_literal(state, lit, X, Y): # Y == None if the literal just requires one argument
        if lit == 'on':
            return on(state, X, Y)
        if lit == 'top':
            return top(state, X)
        if lit == 'isFloor':
            return isFloor(state, X)
        if lit == 'neq':
            return X != Y
        print("Error: literal contains invalid predicate which is {}".format(lit))
        input()
    unbounded_variables = [] # I'm not sure if this is the correct terminology, but these are the variables bound by "there exists"
    for clause in and_conj:
        for var in clause[1:]:
            if var not in ['X', 'Y', 'a'] and var not in unbounded_variables:
                unbounded_variables.append(var)
    #print(unbounded_variables)
    return test_with_unbounded_variables(state, and_conj, X, Y, unbounded_variables, [])
    '''results = [None]*len(and_conj)
    for i, literal in enumerate(and_conj):
        # extract values of variables in literal predicate
        var1 = None
        var2 = None
        if literal[1] in ['X', 'Y']:
            var1 = eval(literal[1])
        else:
            print("Unbounded variables not implemented yet.")
            return
        if len(literal) > 2 and literal[2] in ['X', 'Y']:
            var2 = eval(literal[2])
        elif len(literal) > 2:
            print("Unbounded variables not implemented yet.")
            return
        results[i] = test_single_literal(state, literal[0], var1, var2)
    return all(results)'''

# Code to test whether a conjunction is satisfied by examples of move(X, Y).
'''and_conjunction = [['on', 'Z', 'X'], ['top', 'Z'], ['top', 'Y']]
print(stackings[2])
x = test(stackings[2], and_conjunction, 'b', 'c')
print(x)'''
'''conj = [['on', 'X', 'X']]
print(stackings[2])
test(stackings[2], conj, 'floor', 'b')'''
conj = [['on', 'Y', 'Z'], ['on', 'Z', 'V'], ['on', 'X', 'V']]
test([['a'], ['b'], ['c'], ['d']], [['top', 'a'], ['on', 'X', 'Z'], ['on', 'Y', 'Z']], 'd', 'a')


# In[9]:


# another test
top([['a'], ['c'], ['b', 'd']], 'd')


# In[10]:


# determines the predicting power of predicate P via the two values count(move(X, Y) and P(X, Y)) and count(P(X, Y))
def get_pred_power(pos, neg, clause):
    this_and_move_true = 0
    this_true = 0
    '''for state, state_table in zip(stackings, table):
        this_and_move_true += len([(X, Y) for (X, Y) in state_table if test(state, clause, X, Y) and state_table[X, Y]])
        this_true += len([(X, Y) for (X, Y) in state_table if test(state, clause, X, Y)])
        print("The condition", clause, "is satisfied by these:", [(X, Y) for (X, Y) in state_table if test(state, clause, X, Y)])'''
    this_and_move_true = len([(state, X, Y) for (state, X, Y) in pos if test(state, clause, X, Y)])
    this_true = len([(state, X, Y) for (state, X, Y) in pos + neg if test(state, clause, X, Y)])
    return this_and_move_true, this_true


# In[12]:


# try learning without recursive predicates
# This takes time to run. Uncomment the input() statements to see intermediate progress.
def new_existential_var():
    if 'Z' not in usable_variables: return 'Z'
    else:
        for i in range(ord('V'), ord('A') - 1, -1):
            if chr(i) not in usable_variables:
                return chr(i)
        print("Error: out of variables")
        return None

move_table = [] # fill this with the same info as Qtable, except where each move gets a "true" or "false"
for Qstate in Qtable:
    move_state = dict()
    for act in Qstate:
        move_state[act] = (Qstate[act] > 0.9) # A cutoff of 0.9 was decided as it gives almost the same true positive and true negative rates
    move_table.append(move_state)
#print(move_table)
preds = ['on', 'top', 'isFloor', 'neq']

pos = [] # positive examples
for state, move_state in zip(stackings, move_table):
    for (X, Y) in move_state:
        if move_state[(X, Y)]:
            pos.append((state, X, Y))

neg = [] # negative examples, which are just all pairs of blocks that don't satisfy our Q-table approximation to move(X, Y)
# regardless of whether or not they are valid moves
for state, move_state in zip(stackings, move_table):
    for X in blocks:
        for Y in blocks:
            if (X, Y) not in move_state or not move_state[(X, Y)]:
                neg.append((state, X, Y))

print("Cardinality of pos starts as", len(pos))
#input()
while len(pos) > 0:
    curr_clause = []
    info_gains = []
    usable_variables = ['X', 'Y', 'a'] # the variables that the learner can use in the next predicate in the clause
    new_rule_neg = neg[:] # the negative examples that are satisfied by the current clause as if they were positive
    # learn an "and" clause that matches a subset of all positive examples
    while len(new_rule_neg) > 0:
        info_gain = dict() # information gain from each predicate. predicate is stored as a tuple as key
        for pred in preds:
            ev = new_existential_var()
            if pred in ['top', 'isFloor']: # these predicates only take one argument
                for var in usable_variables + [ev]:
                    test_pred = [pred, var]
                    if test_pred in curr_clause:
                        continue
                    print("get predicting power of", curr_clause + [test_pred])
                    this_and_move_true, this_true = get_pred_power(pos, neg, curr_clause + [test_pred])
                    print("the predicting power is {}/{}".format(this_and_move_true, this_true))
                    if this_true == 0:
                        continue
                    pred_power = this_and_move_true/this_true
                    info_gain[tuple([pred, var])] = pred_power
            if pred in ['on', 'neq']: # on and neq take two arguments
                for var1 in usable_variables + [ev]:
                    for var2 in usable_variables + [ev]:
                        test_pred = [pred, var1, var2]
                        if test_pred in curr_clause:
                            continue
                        print("get predicting power of", curr_clause + [test_pred])
                        this_and_move_true, this_true = get_pred_power(pos, neg, curr_clause + [test_pred])
                        print("the predicting power is {}/{}".format(this_and_move_true, this_true))
                        if this_true == 0:
                            continue
                        pred_power = this_and_move_true/this_true
                        info_gain[tuple([pred, var1, var2])] = pred_power
        print(info_gain)
        if len(info_gain) == 0:
            print("The length of info_gain is 0, no more predicates to add")
            break
        best_pred = max(list(info_gain.items()), key=lambda x: x[1])
        print(best_pred)
        # test if curr_clause + best_pred is actually an improvement over any of the last three clauses
        # if not, learning more predicates seems to be futile
        if len(info_gains) >= 3 and all([best_pred[1] <= x for x in info_gains[-3:]]):
            print("Learning more predicates doesn't improve quality. Breaking.")
            print("Final clause:", curr_clause)
            break
            #pass

        curr_clause.append(list(best_pred[0]))
        print(curr_clause)
        info_gains.append(best_pred[1])
        if best_pred[0][1] not in usable_variables:
            usable_variables.append(best_pred[0][1])
        if len(best_pred[0]) > 2 and best_pred[0][2] not in usable_variables:
            usable_variables.append(best_pred[0][2])
        print(usable_variables)
        # update the set of negative examples still satisfied
        new_rule_neg = [(state, X, Y) for (state, X, Y) in new_rule_neg if test(state, curr_clause, X, Y)]
        print("Cardinality of new_rule_neg is", len(new_rule_neg))

    # Remove the positive examples that satisfy the previous clause
    pos = [(state, X, Y) for (state, X, Y) in pos if not test(state, curr_clause, X, Y)]
    print("Cardinality of pos is", len(pos))
    #input()


# In[210]:


# Some scrap calculation used to show that 0.9 is the optimal cutoff point of the reward to imitate the move() function
'''import matplotlib.pyplot as plt

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
    \'\'\'self.env[3][0] = 'a'
    self.env[3][1] = 'b'
    self.env[3][2] = 'c'
    self.env[3][3] = 'd'\'\'
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

# “X is on the top of the stack containing Y”
def topofstackwith(env_lists, X, Y):
stack = Stack(env_lists)
return (X == Y and stack.is_on_top(X)) or any([stack.on(Z, Y) and topofstackwith(env_lists, X, Z) for Z in blocks])
def move(env_lists, X, Y):
stack = Stack(env_lists)
return topofstackwith(env_lists, Y, 'a') and stack.is_on_top(X) and X != Y

Qtable_dict = {}
for i, Qstate in enumerate(Qtable):
for act in Qstate:
    Qtable_dict[(i, act[0], act[1])] = Qstate[act]

# Plot a ROC curve to see how well value > n predicts move(X, Y)
# Set up a table with all state+actions and values
data = []
for key in Qtable_dict:
data.append([Qtable_dict[key], move(stackings[key[0]], key[1], key[2])])

sensitivities = []
specificities = []
cutoff = 0.8
while cutoff < 1: # may need to change these values
sensitivities.append(len([[x, y] for [x, y] in data if x > cutoff and y == True])/len([[x, y] for [x, y] in data if y == True]))
specificities.append(len([[x, y] for [x, y] in data if x <= cutoff and y == False])/len([[x, y] for [x, y] in data if y == False]))
cutoff += 0.1
print(list(zip(specificities, sensitivities)))
plt.scatter([1 - x for x in specificities], sensitivities)'''


# In[13]:


# Calculate performance metrics of final learned predicate

'''learned_disj = [
    [['top', 'X'], ['on', 'Y', 'a'], ['top', 'Y']],
    [['top', 'X'], ['top', 'Y'], ['on', 'Z', 'a'], ['on', 'Y', 'Z']],
    [['top', 'X'], ['top', 'Y'], ['on', 'Z', 'a'], ['on', 'X', 'Z']],
    [['top', 'X'], ['on', 'a', 'Y'], ['on', 'Z', 'a'], ['on', 'X', 'Z']],
    [['top', 'X'], ['top', 'Y'], ['top', 'a']],
    [['on', 'X', 'Y'], ['on', 'a', 'Y'], ['top', 'X'], ['on', 'Z', 'a'], ['on', 'V', 'Z']],
    [['on', 'X', 'a'], ['top', 'Y'], ['top', 'X']],
    [['on', 'a', 'Y'], ['top', 'X'], ['isFloor', 'Y'], ['on', 'X', 'Y'], ['on', 'Z', 'a']],
    [['on', 'a', 'Y'], ['top', 'X'], ['isFloor', 'Y'], ['on', 'X', 'Y'], ['top', 'a']],
    [['top', 'X'], ['on', 'Z', 'a'], ['on', 'a', 'Y'], ['isFloor', 'Y']],
    [['top', 'X'], ['on', 'Z', 'a'], ['top', 'Y'], ['top', 'Z']],
]'''

'''learned_disj = [
    [['top', 'X'], ['on', 'Y', 'a'], ['neq', 'X', 'Y'], ['top', 'Y']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['on', 'Z', 'a'], ['on', 'Y', 'Z']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['on', 'Z', 'a'], ['neq', 'X', 'Z'], ['top', 'Z']],
    [['top', 'X'], ['on', 'a', 'Y'], ['on', 'Z', 'a'], ['on', 'X', 'Z']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['neq', 'X', 'a'], ['top', 'a'], ['on', 'X', 'Z'], ['on', 'a', 'Z'], ['on', 'X', 'V'], ['on', 'X', 'U']],
    [['top', 'X'], ['on', 'a', 'Y'], ['on', 'Z', 'a'], ['on', 'V', 'Z']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['on', 'Z', 'a'], ['on', 'X', 'Z'], ['on', 'X', 'V'], ['on', 'X', 'U']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['neq', 'X', 'a'], ['top', 'a'], ['on', 'X', 'Z'], ['on', 'Z', 'V'], ['on', 'V', 'U'], ['on', 'X', 'T'], ['on', 'X', 'S']],
    [['top', 'X'], ['on', 'a', 'Y'], ['isFloor', 'Y'], ['on', 'X', 'Y'], ['on', 'Z', 'a'], ['on', 'X', 'V'], ['on', 'X', 'U']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['on', 'X', 'a'], ['on', 'X', 'Z'], ['on', 'X', 'V']],
    [['top', 'X'], ['on', 'a', 'Y'], ['isFloor', 'Y'], ['on', 'X', 'Y'], ['top', 'a'], ['on', 'X', 'Z'], ['on', 'X', 'V']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['top', 'a'], ['neq', 'X', 'a'], ['on', 'X', 'Z'], ['isFloor', 'Z'], ['on', 'X', 'V'], ['on', 'X', 'U']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['top', 'a'], ['on', 'X', 'Z'], ['isFloor', 'Z'], ['on', 'a', 'Z'], ['neq', 'Y', 'a'], ['on', 'X', 'V'], ['on', 'X', 'U']],
    [['top', 'X'], ['on', 'a', 'Y'], ['on', 'Z', 'a'], ['neq', 'X', 'Z'], ['isFloor', 'Y'], ['on', 'X', 'V'], ['on', 'V', 'Y'], ['on', 'X', 'U'], ['on', 'X', 'T']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['neq', 'X', 'a'], ['top', 'a'], ['on', 'X', 'Z'], ['on', 'Z', 'V'], ['on', 'Y', 'V'], ['on', 'X', 'U'], ['on', 'X', 'T']]
]'''

learned_disj = [
    [['top', 'X'], ['on', 'Y', 'a'], ['neq', 'X', 'Y'], ['top', 'Y']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['on', 'Z', 'a'], ['on', 'Y', 'Z']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['on', 'Z', 'a'], ['neq', 'X', 'Z'], ['top', 'Z']],
    [['top', 'X'], ['on', 'a', 'Y'], ['on', 'Z', 'a'], ['on', 'X', 'Z']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['neq', 'X', 'a'], ['top', 'a'], ['on', 'X', 'Z'], ['on', 'a', 'Z'], ['on', 'X', 'V'], ['on', 'X', 'U']],
    [['top', 'X'], ['on', 'a', 'Y'], ['on', 'Z', 'a'], ['on', 'V', 'Z']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['on', 'Z', 'a'], ['on', 'X', 'Z'], ['on', 'X', 'V'], ['on', 'X', 'U']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['neq', 'X', 'a'], ['top', 'a'], ['on', 'X', 'Z'], ['on', 'Z', 'V'], ['on', 'V', 'U'], ['on', 'X', 'T'], ['on', 'X', 'S']],
    [['top', 'X'], ['on', 'a', 'Y'], ['isFloor', 'Y'], ['on', 'X', 'Y'], ['on', 'Z', 'a'], ['on', 'X', 'V'], ['on', 'X', 'U']],
    [['top', 'X'], ['on', 'a', 'Y'], ['on', 'Z', 'a'], ['neq', 'X', 'Z'], ['isFloor', 'Y'], ['on', 'X', 'V'], ['on', 'V', 'Y'], ['on', 'X', 'U'], ['on', 'X', 'T']],
]

learned_disj = [
    [['top', 'X'], ['on', 'Y', 'a'], ['neq', 'X', 'Y'], ['top', 'Y']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['on', 'Z', 'a'], ['on', 'Y', 'Z']],
    [['top', 'X'], ['top', 'Y'], ['neq', 'X', 'Y'], ['on', 'Z', 'a'], ['neq', 'X', 'Z'], ['top', 'Z']],
    [['top', 'X'], ['on', 'a', 'Y'], ['on', 'Z', 'a'], ['on', 'X', 'Z']],
    [['top', 'X'], ['on', 'a', 'Y'], ['on', 'Z', 'a'], ['on', 'V', 'Z']],
]

def apply(disj, state, X, Y):
    return any([test(state, conj, X, Y) for conj in disj])

pos = [] # positive examples
for state, move_state in zip(stackings, move_table):
    for (X, Y) in move_state:
        if move_state[(X, Y)]:
            pos.append((state, X, Y))

neg = [] # negative examples, which are just all pairs of blocks that don't satisfy our Q-table approximation to move(X, Y)
# regardless of whether or not they are valid moves
for state, move_state in zip(stackings, move_table):
    for X in blocks:
        for Y in blocks:
            if (X, Y) not in move_state or not move_state[(X, Y)]:
                neg.append((state, X, Y))

true_pos = 0
false_pos = 0
true_neg = 0
false_neg = 0
for state, move_state in zip(stackings, move_table):
    for X in blocks:
        for Y in blocks:
            if (X, Y) in move_state and move_state[(X, Y)]:
                if apply(learned_disj, state, X, Y):
                    true_pos += 1
                else:
                    false_neg += 1
            else:
                if apply(learned_disj, state, X, Y):
                    false_pos += 1
                else:
                    true_neg += 1

print(true_pos, false_pos, true_neg, false_neg)


# In[14]:


# some more testing
for state, move_state in zip(stackings, move_table):
    for X in blocks:
        for Y in blocks:
            if apply(learned_disj, state, X, Y):
                if (X, Y) in move_state and move_state[(X, Y)]:
                    print("works")
                else:
                    print("does not work")


# In[ ]:





# In[70]:


# This is an attempt to rewrite the above learner to include parsing recursive predicates
# When testing a recursive predicate, there is a maximum depth to the recursion before we decide the recursion is infinite.
# Okay, so I'm going to need to rewrite this to take in an "or" of predicates which themselves are "and"s

depth = 0 # depth of recursive calls of 'move' or 'test'

'''def test_with_unbounded_variables(state, disj, and_conj, X, Y, unbounded_vars, assignments):
    def test_single_literal(state, lit, X, Y): # Y == None if the literal just requires one argument
        global depth
        if lit == 'on':
            return on(state, X, Y)
        if lit == 'top':
            return top(state, X)
        if lit == 'isFloor':
            return isFloor(state, X)
        if lit == 'neq':
            return X != Y
        if lit == 'move':
            depth += 1
            t = apply(state, disj, X, Y)
            depth -= 1
            return t
        print("Error: literal contains invalid predicate which is {}".format(lit))
        input()
        return

    # Converts a string representing a variable to the value of the variable
    def var_to_value(v_str):
        if v_str == 'X':
            return X
        if v_str == 'Y':
            return Y
        if v_str == 'a':
            return 'a'
        if v_str in unbounded_vars and unbounded_vars.index(v_str) < len(assignments):
            return assignments[unbounded_vars.index(v_str)]
        print("Error: variable {} is not bound to value in test".format(v_str))
        return

    results = []
    # Go through all predicates that use only X, Y, and the values from unbounded_vars. Check whether each of them is true.
    for literal in and_conj:
        if all([v in ['X', 'Y', 'a'] or v in unbounded_vars[:len(assignments)] for v in literal[1:]]):
            var1 = var_to_value(literal[1])
            var2 = var_to_value(literal[2]) if len(literal) > 2 else None
            results.append(test_single_literal(state, literal[0], var1, var2))
            #print("result for", literal, "is", results[-1])
    if len(unbounded_vars) == len(assignments):
        # assignment of variables is complete
        #print("Complete assignment {} = {} may or may not satisfy predicate.".format(unbounded_vars, assignments))
        return all(results)
    elif all(results):
        # assignment is not complete but current partial assignment is logically consistent
        #print("Partial assignment {} = {} is consistent".format(unbounded_vars, assignments))
        for new_assignment in blocks:
            if test_with_unbounded_variables(state, disj, and_conj, X, Y, unbounded_vars, assignments + [new_assignment]):
                #print("Predicate {} is satisfied with assignment {} = {}".format(and_conj, unbounded_vars, assignments + [new_assignment]))
                return True
        return False
    else:
        #print("Partial assignment {} = {} is not even consistent".format(unbounded_vars, assignments))
        return False'''

# simple cartesian product of a list with itself num_vars times
def all_possible_assignments(vals, num_vars):
    if num_vars == 0:
        return [[]]
    assignments = []
    for v in vals:
        assignments.extend([[v] + a for a in all_possible_assignments(vals, num_vars - 1)])
    return assignments

# Takes in a state, a clause, and some variable assignments and checks if the clause is true
# This tests a single and_conj
def test(state, disj, and_conj, X, Y):
    def test_single_literal(state, lit, X, Y): # Y == None if the literal just requires one argument
        global depth
        if lit == 'on':
            return on(state, X, Y)
        if lit == 'top':
            return top(state, X)
        if lit == 'isFloor':
            return isFloor(state, X)
        if lit == 'neq':
            return X != Y
        if lit == 'move':
            depth += 1
            t = apply(state, disj, X, Y)
            depth -= 1
            return t
        print("Error: literal contains invalid predicate which is {}".format(lit))
        #input()

    # Converts a string representing a variable to the value of the variable
    def var_to_value(v_str, assignment):
        if v_str == 'X':
            return X
        if v_str == 'Y':
            return Y
        if v_str == 'a':
            return 'a'
        if v_str in unbounded_variables:
            return assignment[unbounded_variables.index(v_str)]
        print("Error: variable {} is not bound to value in test".format(v_str))
        return

    unbounded_variables = [] # I'm not sure if this is the correct terminology, but these are the variables bound by "there exists"
    #print("and conj is", and_conj)
    for clause in and_conj:
        #print("clause is", clause)
        for var in clause[1:]:
            if var not in ['X', 'Y', 'a'] and var not in unbounded_variables:
                unbounded_variables.append(var)
    # get all possible assignments of unbounded variables
    possible_assignments = all_possible_assignments(blocks, len(unbounded_variables))
    #print("All possible assignments", possible_assignments)
    #return test_with_unbounded_variables(state, disj, and_conj, X, Y, unbounded_variables, [])
    # Okay, new plan: look at all possible assignments of variables, and narrow down the set for every new predicate encountered
    # make sure this works on the case with no unbounded variables
    for i, literal in enumerate(and_conj):
        new_assignments = []
        for a in possible_assignments:
            var1 = var_to_value(literal[1], a)
            var2 = var_to_value(literal[2], a) if len(literal) > 2 else None
            if test_single_literal(state, literal[0], var1, var2):
                new_assignments.append(a)
        possible_assignments = new_assignments
        if len(possible_assignments) == 0:
            return [] # there are no assignments left that can satisfy the clause
        #print("New possible assignments", possible_assignments)
    return possible_assignments

    '''results = [None]*len(and_conj)
    for i, literal in enumerate(and_conj):
        # extract values of variables in literal predicate
        var1 = None
        var2 = None
        if literal[1] in ['X', 'Y']:
            var1 = eval(literal[1])
        else:
            print("Unbounded variables not implemented yet.")
            return
        if len(literal) > 2 and literal[2] in ['X', 'Y']:
            var2 = eval(literal[2])
        elif len(literal) > 2:
            print("Unbounded variables not implemented yet.")
            return
        results[i] = test_single_literal(state, literal[0], var1, var2)
    return all(results)'''

# Checks a variable assignment to a disjunction of predicates to see if it works
def apply(state, disj, X, Y):
    if depth >= 20:
        raise RuntimeError("Infinite recursion detected.")
    # We need to check this predicate by predicate and "short circuit" if any end up "true"
    # so that we can avoid infinite loops when we use recursive predicates
    for conj in disj:
        #print("About to test conj", conj, "of disj", disj)
        #input()
        if test(state, disj, conj, X, Y) != []:
            #print(conj, "returned true")
            return True
    return False

# Code to test whether a conjunction is satisfied by examples of move(X, Y).
'''and_conjunction = [['on', 'Z', 'X'], ['top', 'Z'], ['top', 'Y']]
print(stackings[2])
x = test(stackings[2], and_conjunction, 'b', 'c')
print(x)'''
'''conj = [['on', 'X', 'X']]
print(stackings[2])
test(stackings[2], conj, 'floor', 'b')'''
conj = [['on', 'Y', 'Z'], ['on', 'Z', 'V'], ['on', 'X', 'V']]
apply([['b', 'a', 'd'], ['c']], [[['on', 'X', 'Y']], [['on', 'X', 'Z'], ['move', 'Z', 'Y']]], 'b', 'floor')


# In[15]:


on([['b', 'a'], ['c'], ['d']], 'b', 'a')


# In[71]:


# This is a learner for move() using recursive predicates that tests each recursive predicate using the currently learned predicate.
# This runs very slowly because it has to check a lot of infinite recursions and only aborts when they reach a depth of 20

# determines the predicting power of predicate P via the two values count(move(X, Y) and P(X, Y)) and count(P(X, Y))
def get_pred_power(pos, neg, disj, clause):
    this_and_move_true = 0
    this_true = 0
    '''for state, state_table in zip(stackings, table):
        this_and_move_true += len([(X, Y) for (X, Y) in state_table if test(state, clause, X, Y) and state_table[X, Y]])
        this_true += len([(X, Y) for (X, Y) in state_table if test(state, clause, X, Y)])
        print("The condition", clause, "is satisfied by these:", [(X, Y) for (X, Y) in state_table if test(state, clause, X, Y)])'''
    print("About to test first thing")
    this_and_move_true = len([(state, X, Y) for (state, X, Y) in pos if test(state, disj, clause, X, Y) != []])
    print("About to test second thing")
    this_true = len([(state, X, Y) for (state, X, Y) in pos + neg if test(state, disj, clause, X, Y) != []])
    return this_and_move_true, this_true

def new_existential_var():
    if 'Z' not in usable_variables: return 'Z'
    else:
        for i in range(ord('V'), ord('A') - 1, -1):
            if chr(i) not in usable_variables:
                return chr(i)
        print("Error: out of variables")
        return None

move_table = [] # fill this with the same info as Qtable, except where each move gets a "true" or "false"
for Qstate in Qtable:
    move_state = dict()
    for act in Qstate:
        move_state[act] = (Qstate[act] > 0.9) # A cutoff of 0.9 was decided as it gives almost the same true positive and true negative rates
    move_table.append(move_state)
#print(move_table)
preds = ['on', 'top', 'isFloor', 'neq', 'move']

pos = [] # positive examples
for state, move_state in zip(stackings, move_table):
    for (X, Y) in move_state:
        if move_state[(X, Y)]:
            pos.append((state, X, Y))

neg = [] # negative examples, which are just all pairs of blocks that don't satisfy our Q-table approximation to move(X, Y)
# regardless of whether or not they are valid moves
for state, move_state in zip(stackings, move_table):
    for X in blocks:
        for Y in blocks:
            if (X, Y) not in move_state or not move_state[(X, Y)]:
                neg.append((state, X, Y))

disj = []
while len(pos) > 0:
    curr_clause = []
    info_gains = []
    usable_variables = ['X', 'Y', 'a'] # the variables that the learner can use in the next predicate in the clause
    new_rule_neg = neg[:] # the negative examples that are satisfied by the current clause as if they were positive
    # learn an "and" clause that matches a subset of all positive examples
    while len(new_rule_neg) > 0:
        info_gain = dict() # information gain from each predicate. predicate is stored as a tuple as key
        for pred in preds:
            ev = new_existential_var()
            if pred in ['top', 'isFloor']: # these predicates only take one argument
                for var in usable_variables + [ev]:
                    test_pred = [pred, var]
                    if test_pred in curr_clause:
                        continue
                    print("get predicting power of", curr_clause + [test_pred])
                    try:
                        this_and_move_true, this_true = get_pred_power(pos, neg, disj + [curr_clause + [test_pred]], curr_clause + [test_pred])
                    except RuntimeError:
                        # infinite recursion detected
                        continue
                    print("the predicting power is {}/{}".format(this_and_move_true, this_true))
                    if this_true == 0:
                        continue
                    pred_power = this_and_move_true/this_true
                    info_gain[tuple([pred, var])] = pred_power
            if pred in ['on', 'neq', 'move']: # on, neq, and move take two arguments
                for var1 in usable_variables + [ev]:
                    for var2 in usable_variables + [ev]:
                        test_pred = [pred, var1, var2]
                        if test_pred in curr_clause:
                            continue
                        print("get predicting power of", curr_clause + [test_pred])
                        try:
                            this_and_move_true, this_true = get_pred_power(pos, neg, disj + [curr_clause + [test_pred]], curr_clause + [test_pred])
                        except RuntimeError:
                            # infinite recursion detected
                            continue
                        print("the predicting power is {}/{}".format(this_and_move_true, this_true))
                        if this_true == 0:
                            continue
                        pred_power = this_and_move_true/this_true
                        info_gain[tuple([pred, var1, var2])] = pred_power
        print(info_gain)
        if len(info_gain) == 0:
            print("The length of info_gain is 0, no more predicates to add")
            break
        best_pred = max(list(info_gain.items()), key=lambda x: x[1])
        print(best_pred)
        # test if curr_clause + best_pred is actually an improvement over any of the last three clauses
        # if not, learning more predicates seems to be futile
        if len(info_gains) >= 3 and all([best_pred[1] <= x for x in info_gains[-3:]]):
            print("Learning more predicates doesn't improve quality. Breaking.")
            print("Final clause:", curr_clause)
            break
            #pass

        curr_clause.append(list(best_pred[0]))
        print(curr_clause)
        info_gains.append(best_pred[1])
        if best_pred[0][1] not in usable_variables:
            usable_variables.append(best_pred[0][1])
        if len(best_pred[0]) > 2 and best_pred[0][2] not in usable_variables:
            usable_variables.append(best_pred[0][2])
        print(usable_variables)
        # update the set of negative examples still satisfied
        new_rule_neg = [(state, X, Y) for (state, X, Y) in new_rule_neg if test(state, disj + [curr_clause], curr_clause, X, Y) != []]
        print("Cardinality of new_rule_neg is", len(new_rule_neg))

    disj.append(curr_clause)
    # Remove the positive examples that satisfy the previous clause
    pos = [(state, X, Y) for (state, X, Y) in pos if not test(state, disj, curr_clause, X, Y) != []]
    print("Cardinality of pos is", len(pos))
    input()


# In[61]:


# This is a new learner for move() using recursive predicates that tests each recursive move() call using actual examples
# I don't think this will be able to learn something resembling my handmade policy, because that policy uses a recursive definition of above(), not move().
# But it might
# work in progress

# This is an attempt to rewrite the above learner to include parsing recursive predicates
# When testing a recursive predicate, there is a maximum depth to the recursion before we decide the recursion is infinite.
# Okay, so I'm going to need to rewrite this to take in an "or" of predicates which themselves are "and"s

'''def test_with_unbounded_variables(state, disj, and_conj, X, Y, unbounded_vars, assignments):
    def test_single_literal(state, lit, X, Y): # Y == None if the literal just requires one argument
        global depth
        if lit == 'on':
            return on(state, X, Y)
        if lit == 'top':
            return top(state, X)
        if lit == 'isFloor':
            return isFloor(state, X)
        if lit == 'neq':
            return X != Y
        if lit == 'move':
            depth += 1
            t = apply(state, disj, X, Y)
            depth -= 1
            return t
        print("Error: literal contains invalid predicate which is {}".format(lit))
        input()
        return

    # Converts a string representing a variable to the value of the variable
    def var_to_value(v_str):
        if v_str == 'X':
            return X
        if v_str == 'Y':
            return Y
        if v_str == 'a':
            return 'a'
        if v_str in unbounded_vars and unbounded_vars.index(v_str) < len(assignments):
            return assignments[unbounded_vars.index(v_str)]
        print("Error: variable {} is not bound to value in test".format(v_str))
        return

    results = []
    # Go through all predicates that use only X, Y, and the values from unbounded_vars. Check whether each of them is true.
    for literal in and_conj:
        if all([v in ['X', 'Y', 'a'] or v in unbounded_vars[:len(assignments)] for v in literal[1:]]):
            var1 = var_to_value(literal[1])
            var2 = var_to_value(literal[2]) if len(literal) > 2 else None
            results.append(test_single_literal(state, literal[0], var1, var2))
            #print("result for", literal, "is", results[-1])
    if len(unbounded_vars) == len(assignments):
        # assignment of variables is complete
        #print("Complete assignment {} = {} may or may not satisfy predicate.".format(unbounded_vars, assignments))
        return all(results)
    elif all(results):
        # assignment is not complete but current partial assignment is logically consistent
        #print("Partial assignment {} = {} is consistent".format(unbounded_vars, assignments))
        for new_assignment in blocks:
            if test_with_unbounded_variables(state, disj, and_conj, X, Y, unbounded_vars, assignments + [new_assignment]):
                #print("Predicate {} is satisfied with assignment {} = {}".format(and_conj, unbounded_vars, assignments + [new_assignment]))
                return True
        return False
    else:
        #print("Partial assignment {} = {} is not even consistent".format(unbounded_vars, assignments))
        return False'''

# simple cartesian product of a list with itself num_vars times
def all_possible_assignments(vals, num_vars):
    if num_vars == 0:
        return [[]]
    assignments = []
    for v in vals:
        assignments.extend([[v] + a for a in all_possible_assignments(vals, num_vars - 1)])
    return assignments

# Takes in a state, a clause, and some variable assignments and checks if the clause is true
# This tests a single and_conj
def test(state, and_conj, X, Y):
    def test_single_literal(state, lit, X, Y): # Y == None if the literal just requires one argument
        if lit == 'on':
            return on(state, X, Y)
        if lit == 'top':
            return top(state, X)
        if lit == 'isFloor':
            return isFloor(state, X)
        if lit == 'neq':
            return X != Y
        if lit == 'move':
            # use data from the actual move table rather than making a recursive call
            return (X, Y) in move_table[stackings.index(state)] and move_table[stackings.index(state)][(X, Y)]
        print("Error: literal contains invalid predicate which is {}".format(lit))
        #input()

    # Converts a string representing a variable to the value of the variable
    def var_to_value(v_str, assignment):
        if v_str == 'X':
            return X
        if v_str == 'Y':
            return Y
        if v_str == 'a':
            return 'a'
        if v_str in unbounded_variables:
            return assignment[unbounded_variables.index(v_str)]
        print("Error: variable {} is not bound to value in test".format(v_str))
        return

    unbounded_variables = [] # I'm not sure if this is the correct terminology, but these are the variables bound by "there exists"
    #print("and conj is", and_conj)
    for clause in and_conj:
        #print("clause is", clause)
        for var in clause[1:]:
            if var not in ['X', 'Y', 'a'] and var not in unbounded_variables:
                unbounded_variables.append(var)
    # get all possible assignments of unbounded variables
    possible_assignments = all_possible_assignments(blocks, len(unbounded_variables))
    #print("All possible assignments", possible_assignments)
    #return test_with_unbounded_variables(state, disj, and_conj, X, Y, unbounded_variables, [])
    # Okay, new plan: look at all possible assignments of variables, and narrow down the set for every new predicate encountered
    # make sure this works on the case with no unbounded variables
    for i, literal in enumerate(and_conj):
        new_assignments = []
        for a in possible_assignments:
            var1 = var_to_value(literal[1], a)
            var2 = var_to_value(literal[2], a) if len(literal) > 2 else None
            if test_single_literal(state, literal[0], var1, var2):
                new_assignments.append(a)
        possible_assignments = new_assignments
        if len(possible_assignments) == 0:
            return False # there are no assignments left that can satisfy the clause
        #print("New possible assignments", possible_assignments)
    return True

    '''results = [None]*len(and_conj)
    for i, literal in enumerate(and_conj):
        # extract values of variables in literal predicate
        var1 = None
        var2 = None
        if literal[1] in ['X', 'Y']:
            var1 = eval(literal[1])
        else:
            print("Unbounded variables not implemented yet.")
            return
        if len(literal) > 2 and literal[2] in ['X', 'Y']:
            var2 = eval(literal[2])
        elif len(literal) > 2:
            print("Unbounded variables not implemented yet.")
            return
        results[i] = test_single_literal(state, literal[0], var1, var2)
    return all(results)'''

# Checks a variable assignment to a disjunction of predicates to see if it works
def apply(state, disj, X, Y):
    # We need to check this predicate by predicate and "short circuit" if any end up "true"
    for conj in disj:
        #print("About to test conj", conj, "of disj", disj)
        #input()
        if test(state, conj, X, Y):
            #print(conj, "returned true")
            return True
    return False

# Code to test whether a conjunction is satisfied by examples of move(X, Y).
'''and_conjunction = [['on', 'Z', 'X'], ['top', 'Z'], ['top', 'Y']]
print(stackings[2])
x = test(stackings[2], and_conjunction, 'b', 'c')
print(x)'''
'''conj = [['on', 'X', 'X']]
print(stackings[2])
test(stackings[2], conj, 'floor', 'b')'''
conj = [['on', 'Y', 'Z'], ['on', 'Z', 'V'], ['on', 'X', 'V']]
apply([['b', 'a', 'd'], ['c']], [[['on', 'X', 'Y']], [['on', 'X', 'Z'], ['move', 'Z', 'Y']]], 'b', 'floor')

# determines the predicting power of predicate P via the two values count(move(X, Y) and P(X, Y)) and count(P(X, Y))
def get_pred_power(pos, neg, clause):
    this_and_move_true = 0
    this_true = 0
    '''for state, state_table in zip(stackings, table):
        this_and_move_true += len([(X, Y) for (X, Y) in state_table if test(state, clause, X, Y) and state_table[X, Y]])
        this_true += len([(X, Y) for (X, Y) in state_table if test(state, clause, X, Y)])
        print("The condition", clause, "is satisfied by these:", [(X, Y) for (X, Y) in state_table if test(state, clause, X, Y)])'''
    print("About to test first thing")
    this_and_move_true = len([(state, X, Y) for (state, X, Y) in pos if test(state, clause, X, Y)])
    print("About to test second thing")
    this_true = len([(state, X, Y) for (state, X, Y) in pos + neg if test(state, clause, X, Y)])
    return this_and_move_true, this_true

def new_existential_var():
    if 'Z' not in usable_variables: return 'Z'
    else:
        for i in range(ord('V'), ord('A') - 1, -1):
            if chr(i) not in usable_variables:
                return chr(i)
        print("Error: out of variables")
        return None

move_table = [] # fill this with the same info as Qtable, except where each move gets a "true" or "false"
for Qstate in Qtable:
    move_state = dict()
    for act in Qstate:
        move_state[act] = (Qstate[act] > 0.9) # A cutoff of 0.9 was decided as it gives almost the same true positive and true negative rates
    move_table.append(move_state)
#print(move_table)
preds = ['on', 'top', 'isFloor', 'neq', 'move']

pos = [] # positive examples
for state, move_state in zip(stackings, move_table):
    for (X, Y) in move_state:
        if move_state[(X, Y)]:
            pos.append((state, X, Y))

neg = [] # negative examples, which are just all pairs of blocks that don't satisfy our Q-table approximation to move(X, Y)
# regardless of whether or not they are valid moves
for state, move_state in zip(stackings, move_table):
    for X in blocks:
        for Y in blocks:
            if (X, Y) not in move_state or not move_state[(X, Y)]:
                neg.append((state, X, Y))

disj = []
while len(pos) > 0:
    curr_clause = []
    info_gains = []
    usable_variables = ['X', 'Y', 'a'] # the variables that the learner can use in the next predicate in the clause
    new_rule_neg = neg[:] # the negative examples that are satisfied by the current clause as if they were positive
    # learn an "and" clause that matches a subset of all positive examples
    while len(new_rule_neg) > 0:
        info_gain = dict() # information gain from each predicate. predicate is stored as a tuple as key
        for pred in preds:
            ev = new_existential_var()
            if pred in ['top', 'isFloor']: # these predicates only take one argument
                for var in usable_variables + [ev]:
                    test_pred = [pred, var]
                    if test_pred in curr_clause:
                        continue
                    print("get predicting power of", curr_clause + [test_pred])
                    this_and_move_true, this_true = get_pred_power(pos, neg, curr_clause + [test_pred])
                    print("the predicting power is {}/{}".format(this_and_move_true, this_true))
                    if this_true == 0:
                        continue
                    pred_power = this_and_move_true/this_true
                    info_gain[tuple([pred, var])] = pred_power
            if pred in ['on', 'neq', 'move']: # on, neq, and move take two arguments
                for var1 in usable_variables + [ev]:
                    for var2 in usable_variables + [ev]:
                        test_pred = [pred, var1, var2]
                        # skip the ones that will definitely lead to infinite loops
                        if test_pred in [['move', 'X', 'Y'], ['move', 'Y', 'X']]:
                            continue
                        if test_pred in curr_clause:
                            continue
                        print("get predicting power of", curr_clause + [test_pred])
                        this_and_move_true, this_true = get_pred_power(pos, neg, curr_clause + [test_pred])
                        print("the predicting power is {}/{}".format(this_and_move_true, this_true))
                        if this_true == 0:
                            continue
                        pred_power = this_and_move_true/this_true
                        info_gain[tuple([pred, var1, var2])] = pred_power
        print(info_gain)
        if len(info_gain) == 0:
            print("The length of info_gain is 0, no more predicates to add")
            break
        best_pred = max(list(info_gain.items()), key=lambda x: x[1])
        print(best_pred)
        # test if curr_clause + best_pred is actually an improvement over any of the last three clauses
        # if not, learning more predicates seems to be futile
        if len(info_gains) >= 3 and all([best_pred[1] <= x for x in info_gains[-3:]]):
            print("Learning more predicates doesn't improve quality. Breaking.")
            print("Final clause:", curr_clause)
            break
            #pass

        curr_clause.append(list(best_pred[0]))
        print(curr_clause)
        info_gains.append(best_pred[1])
        if best_pred[0][1] not in usable_variables:
            usable_variables.append(best_pred[0][1])
        if len(best_pred[0]) > 2 and best_pred[0][2] not in usable_variables:
            usable_variables.append(best_pred[0][2])
        print(usable_variables)
        # update the set of negative examples still satisfied
        new_rule_neg = [(state, X, Y) for (state, X, Y) in new_rule_neg if test(state, curr_clause, X, Y)]
        print("Cardinality of new_rule_neg is", len(new_rule_neg))

    disj.append(curr_clause)
    # Remove the positive examples that satisfy the previous clause
    pos = [(state, X, Y) for (state, X, Y) in pos if not test(state, curr_clause, X, Y)]
    print("Cardinality of pos is", len(pos))
    input()


# In[63]:


disj


# In[58]:


test_conj = [['move', 'X', 'Y'], ['move', 'Y', 'Z'], ['neq', 'Y', 'Z']]
test([['d'], ['a', 'c', 'b']], test_conj, 'd', 'b')


# In[56]:


move_table[stackings.index([['d'], ['a', 'c', 'b']])]


# In[65]:


def test(state, and_conj, X, Y):
    def test_single_literal(state, lit, X, Y): # Y == None if the literal just requires one argument
        global depth
        if lit == 'on':
            return on(state, X, Y)
        if lit == 'top':
            return top(state, X)
        if lit == 'isFloor':
            return isFloor(state, X)
        if lit == 'neq':
            return X != Y
        if lit == 'move':
            # use data from the actual move table rather than making a recursive call
            print(X, Y)
            return (X, Y) in move_table[stackings.index(state)] and move_table[stackings.index(state)][(X, Y)]
        print("Error: literal contains invalid predicate which is {}".format(lit))
        #input()

    # Converts a string representing a variable to the value of the variable
    def var_to_value(v_str, assignment):
        if v_str == 'X':
            return X
        if v_str == 'Y':
            return Y
        if v_str == 'a':
            return 'a'
        if v_str in unbounded_variables:
            return assignment[unbounded_variables.index(v_str)]
        print("Error: variable {} is not bound to value in test".format(v_str))
        return

    unbounded_variables = [] # I'm not sure if this is the correct terminology, but these are the variables bound by "there exists"
    #print("and conj is", and_conj)
    for clause in and_conj:
        #print("clause is", clause)
        for var in clause[1:]:
            if var not in ['X', 'Y', 'a'] and var not in unbounded_variables:
                unbounded_variables.append(var)
    # get all possible assignments of unbounded variables
    possible_assignments = all_possible_assignments(blocks, len(unbounded_variables))
    #print("All possible assignments", possible_assignments)
    #return test_with_unbounded_variables(state, disj, and_conj, X, Y, unbounded_variables, [])
    # Okay, new plan: look at all possible assignments of variables, and narrow down the set for every new predicate encountered
    # make sure this works on the case with no unbounded variables
    for i, literal in enumerate(and_conj):
        new_assignments = []
        for a in possible_assignments:
            var1 = var_to_value(literal[1], a)
            var2 = var_to_value(literal[2], a) if len(literal) > 2 else None
            if test_single_literal(state, literal[0], var1, var2):
                new_assignments.append(a)
        possible_assignments = new_assignments
        if len(possible_assignments) == 0:
            return False # there are no assignments left that can satisfy the clause
        #print("New possible assignments", possible_assignments)
    return True


# In[68]:


# Use forward chaining to evaluate a predicate by enumerating all of its "true" instances
def test_forward_chaining(state, and_conj, X, Y):
    def test_single_literal(state, lit, X, Y): # Y == None if the literal just requires one argument
        global depth
        if lit == 'on':
            return on(state, X, Y)
        if lit == 'top':
            return top(state, X)
        if lit == 'isFloor':
            return isFloor(state, X)
        if lit == 'neq':
            return X != Y
        if lit == 'move':
            # use data from the actual move table rather than making a recursive call
            return (state, X, Y) in inferred_examples
        print("Error: literal contains invalid predicate which is {}".format(lit))
        #input()

    # Converts a string representing a variable to the value of the variable
    def var_to_value(v_str, assignment):
        if v_str == 'X':
            return X
        if v_str == 'Y':
            return Y
        if v_str == 'a':
            return 'a'
        if v_str in unbounded_variables:
            return assignment[unbounded_variables.index(v_str)]
        print("Error: variable {} is not bound to value in test".format(v_str))
        return

    unbounded_variables = [] # I'm not sure if this is the correct terminology, but these are the variables bound by "there exists"
    #print("and conj is", and_conj)
    for clause in and_conj:
        #print("clause is", clause)
        for var in clause[1:]:
            if var not in ['X', 'Y', 'a'] and var not in unbounded_variables:
                unbounded_variables.append(var)
    # get all possible assignments of unbounded variables
    possible_assignments = all_possible_assignments(blocks, len(unbounded_variables))
    #print("All possible assignments", possible_assignments)
    #return test_with_unbounded_variables(state, disj, and_conj, X, Y, unbounded_variables, [])
    # Okay, new plan: look at all possible assignments of variables, and narrow down the set for every new predicate encountered
    # make sure this works on the case with no unbounded variables
    for i, literal in enumerate(and_conj):
        new_assignments = []
        for a in possible_assignments:
            var1 = var_to_value(literal[1], a)
            var2 = var_to_value(literal[2], a) if len(literal) > 2 else None
            if test_single_literal(state, literal[0], var1, var2):
                new_assignments.append(a)
        possible_assignments = new_assignments
        if len(possible_assignments) == 0:
            return False # there are no assignments left that can satisfy the clause
        #print("New possible assignments", possible_assignments)
    return True

learned_disj = [
    [['move', 'X', 'Z'], ['move', 'V', 'Y'], ['move', 'Z', 'V']],
    [['move', 'X', 'a'], ['move', 'Z', 'Y'], ['neq', 'X', 'Y'], ['on', 'Y', 'V']],
    [['on', 'Y', 'a'], ['move', 'X', 'Z'], ['on', 'Z', 'a']],
    [['move', 'a', 'Y'], ['move', 'X', 'Z'], ['on', 'X', 'Y']],
    [['move', 'a', 'Y'], ['move', 'X', 'Z'], ['on', 'X', 'Z']],
    [['move', 'X', 'Z'], ['move', 'V', 'Y'], ['on', 'X', 'Y'], ['on', 'X', 'Z']],
    [['move', 'X', 'Z'], ['move', 'V', 'Y'], ['neq', 'X', 'Y'], ['on', 'X', 'Z']],
    [['on', 'a', 'Y'], ['move', 'X', 'Z'], ['on', 'a', 'Z']]
]

inferred_examples = []

new_batch = []

while True:
    for state in stackings:
        for X in blocks:
            for Y in blocks:
                if (state, X, Y) in inferred_examples: # we don't want to test examples already shown to be true
                    continue
                for conj in learned_disj:
                    if test_forward_chaining(state, conj, X, Y):
                        new_batch.append((state, X, Y))
                        break
    print("new batch is", new_batch)
    input()
    if len(new_batch) == 0:
        break
    inferred_examples.extend(new_batch)


# In[ ]:


# simple cartesian product of a list with itself num_vars times
def all_possible_assignments(vals, num_vars):
    if num_vars == 0:
        return [[]]
    assignments = []
    for v in vals:
        assignments.extend([[v] + a for a in all_possible_assignments(vals, num_vars - 1)])
    return assignments

# Now try something similar with my own learning algorithm

def on_chain(state, X, Y):
    if on(state, X, Y):
        return True # length 1 is matched for on-chain
    for i in range(2, 6): # length of the chain
        possible_assignments = all_possible_assignments(blocks, i)
        #lits_to_add.append([best_pred[0][0], best_pred[0][1], new_ext_vars[0]])
        possible_assignments = [x for x in possible_assignments if on(X, x[0])]
        for j in range(1, i - 1):
            #lits_to_add.append([best_pred[0][0], new_ext_vars[j - 1], new_ext_vars[j]])
            possible_assignments = [x for x in possible_assignments if on(x[j - 1], x[j])]
            if len(possible_assignments) == 0:
                break
        #lits_to_add.append([best_pred[0][0], new_ext_vars[i - 2], best_pred[0][2]])
        possible_assignments = [x for x in possible_assignments if on(x[i - 2], Y)]
        #print(lits_to_add)
        #input()
        if len(possible_assignments) > 0: # this length is matched for on-chain
            return True
        # ...
    return False # no length is matched for on-chain

# functions for testing a non-recursive predicate
def test_with_unbounded_variables(state, and_conj, X, Y, unbounded_vars, assignments):
    def test_single_literal(state, lit, X, Y): # Y == None if the literal just requires one argument
        if lit == 'on':
            return on(state, X, Y)
        if lit == 'top':
            return top(state, X)
        if lit == 'isFloor':
            return isFloor(state, X)
        if lit == 'neq':
            return X != Y
        if lit == 'on-chain':
            return on_chain(state, X, Y)
        print("Error: literal contains invalid predicate which is {}".format(lit))
        input()
        return

    # Converts a string representing a variable to the value of the variable
    def var_to_value(v_str):
        if v_str == 'X':
            return X
        if v_str == 'Y':
            return Y
        if v_str == 'a':
            return 'a'
        if v_str in unbounded_vars and unbounded_vars.index(v_str) < len(assignments):
            return assignments[unbounded_vars.index(v_str)]
        print("Error: variable {} is not bound to value in test".format(v_str))
        return

    results = []
    # Go through all predicates that use only X, Y, and the values from unbounded_vars. Check whether each of them is true.
    for literal in and_conj:
        if all([v in ['X', 'Y', 'a'] or v in unbounded_vars[:len(assignments)] for v in literal[1:]]):
            var1 = var_to_value(literal[1])
            var2 = var_to_value(literal[2]) if len(literal) > 2 else None
            results.append(test_single_literal(state, literal[0], var1, var2))
            #print("result for", literal, "is", results[-1])
    if len(unbounded_vars) == len(assignments):
        # assignment of variables is complete
        #print("Complete assignment {} = {} may or may not satisfy predicate.".format(unbounded_vars, assignments))
        return all(results)
    elif all(results):
        # assignment is not complete but current partial assignment is logically consistent
        #print("Partial assignment {} = {} is consistent".format(unbounded_vars, assignments))
        for new_assignment in blocks:
            if test_with_unbounded_variables(state, and_conj, X, Y, unbounded_vars, assignments + [new_assignment]):
                #print("Predicate {} is satisfied with assignment {} = {}".format(and_conj, unbounded_vars, assignments + [new_assignment]))
                return True
        return False
    else:
        #print("Partial assignment {} = {} is not even consistent".format(unbounded_vars, assignments))
        return False

# Takes in a state, a clause, and some variable assignments and checks if the clause is true
def test(state, and_conj, X, Y):
    def test_single_literal(state, lit, X, Y): # Y == None if the literal just requires one argument
        if lit == 'on':
            return on(state, X, Y)
        if lit == 'top':
            return top(state, X)
        if lit == 'isFloor':
            return isFloor(state, X)
        if lit == 'neq':
            return X != Y
        if lit == 'on-chain':
            return on_chain(state, X, Y)
        print("Error: literal contains invalid predicate which is {}".format(lit))
        input()
    unbounded_variables = [] # I'm not sure if this is the correct terminology, but these are the variables bound by "there exists"
    for clause in and_conj:
        for var in clause[1:]:
            if var not in ['X', 'Y', 'a'] and var not in unbounded_variables:
                unbounded_variables.append(var)
    #print(unbounded_variables)
    return test_with_unbounded_variables(state, and_conj, X, Y, unbounded_variables, [])
    '''results = [None]*len(and_conj)
    for i, literal in enumerate(and_conj):
        # extract values of variables in literal predicate
        var1 = None
        var2 = None
        if literal[1] in ['X', 'Y']:
            var1 = eval(literal[1])
        else:
            print("Unbounded variables not implemented yet.")
            return
        if len(literal) > 2 and literal[2] in ['X', 'Y']:
            var2 = eval(literal[2])
        elif len(literal) > 2:
            print("Unbounded variables not implemented yet.")
            return
        results[i] = test_single_literal(state, literal[0], var1, var2)
    return all(results)'''

def new_existential_var():
    if 'Z' not in usable_variables: return 'Z'
    else:
        for i in range(ord('V'), ord('A') - 1, -1):
            if chr(i) not in usable_variables:
                return chr(i)
        print("Error: out of variables")
        return None

def new_existential_vars_chain(n_vars):
    potential_variables = ['Z'] + [chr(i) for i in range(ord('V'), ord('A') - 1, -1)]
    variables = []
    var_ind = 0
    for i in range(n_vars):
        if var_ind > len(potential_variables):
            print("Error: out of variables")
        while potential_variables[var_ind] in usable_variables:
            var_ind += 1
            if var_ind > len(potential_variables):
                print("Error: out of variables")
        variables.append(potential_variables[var_ind])
        var_ind += 1
    return variables

# determines the predicting power of predicate P via the two values count(move(X, Y) and P(X, Y)) and count(P(X, Y))
def get_pred_power(pos, neg, clause):
    this_and_move_true = 0
    this_true = 0
    '''for state, state_table in zip(stackings, table):
        this_and_move_true += len([(X, Y) for (X, Y) in state_table if test(state, clause, X, Y) and state_table[X, Y]])
        this_true += len([(X, Y) for (X, Y) in state_table if test(state, clause, X, Y)])
        print("The condition", clause, "is satisfied by these:", [(X, Y) for (X, Y) in state_table if test(state, clause, X, Y)])'''
    this_and_move_true = len([(state, X, Y) for (state, X, Y) in pos if test(state, clause, X, Y)])
    this_true = len([(state, X, Y) for (state, X, Y) in pos + neg if test(state, clause, X, Y)])
    return this_and_move_true, this_true

pos = [] # positive examples
for state, move_state in zip(stackings, move_table):
    for (X, Y) in move_state:
        if move_state[(X, Y)]:
            pos.append((state, X, Y))

neg = [] # negative examples, which are just all pairs of blocks that don't satisfy our Q-table approximation to move(X, Y)
# regardless of whether or not they are valid moves
for state, move_state in zip(stackings, move_table):
    for X in blocks:
        for Y in blocks:
            if (X, Y) not in move_state or not move_state[(X, Y)]:
                neg.append((state, X, Y))

curr_clause = []
info_gains = []
usable_variables = ['X', 'Y', 'a'] # the variables that the learner can use in the next predicate in the clause
new_rule_neg = neg[:] # the negative examples that are satisfied by the current clause as if they were positive
# learn an "and" clause that matches a subset of all positive examples
while len(new_rule_neg) > 0:
    info_gain = dict() # information gain from each predicate. predicate is stored as a tuple as key
    for pred in preds:
        ev = new_existential_var()
        if pred in ['top', 'isFloor']: # these predicates only take one argument
            for var in usable_variables + [ev]:
                test_pred = [pred, var]
                if test_pred in curr_clause:
                    continue
                print("get predicting power of", curr_clause + [test_pred])
                this_and_move_true, this_true = get_pred_power(pos, neg, curr_clause + [test_pred])
                print("the predicting power is {}/{}".format(this_and_move_true, this_true))
                if this_true == 0:
                    continue
                pred_power = this_and_move_true/this_true
                info_gain[tuple([pred, var])] = pred_power
        if pred in ['on', 'neq']: # on, neq, and move take two arguments
            for var1 in usable_variables + [ev]:
                for var2 in usable_variables + [ev]:
                    test_pred = [pred, var1, var2]
                    # skip the ones that will definitely lead to infinite loops
                    if test_pred in [['move', 'X', 'Y'], ['move', 'Y', 'X']]:
                        continue
                    if test_pred in curr_clause:
                        continue
                    print("get predicting power of", curr_clause + [test_pred])
                    this_and_move_true, this_true = get_pred_power(pos, neg, curr_clause + [test_pred])
                    print("the predicting power is {}/{}".format(this_and_move_true, this_true))
                    if this_true == 0:
                        continue
                    pred_power = this_and_move_true/this_true
                    info_gain[tuple([pred, var1, var2])] = pred_power
    print(info_gain)
    if len(info_gain) == 0:
        print("The length of info_gain is 0, no more predicates to add")
        break
    best_pred = max(list(info_gain.items()), key=lambda x: x[1])
    print("best pred is", best_pred)
    # see if replacing the last predicate with a chain of predicates does any better
    input()
    if best_pred[0][0] == 'on':
        new_ext_vars = new_existential_vars_chain(5)
        for i in range(2, 6): # length of the chain
            lits_to_add = [] # the chain of literals to add
            lits_to_add.append([best_pred[0][0], best_pred[0][1], new_ext_vars[0]])
            for j in range(1, i - 1):
                lits_to_add.append([best_pred[0][0], new_ext_vars[j - 1], new_ext_vars[j]])
            lits_to_add.append([best_pred[0][0], new_ext_vars[i - 2], best_pred[0][2]])
            print(lits_to_add)
            input()
            this_and_move_true, this_true = get_pred_power(pos, neg, curr_clause + lits_to_add)
            # ...
    # test if curr_clause + best_pred is actually an improvement over any of the last three clauses
    # if not, learning more predicates seems to be futile
    if len(info_gains) >= 3 and all([best_pred[1] <= x for x in info_gains[-3:]]):
        print("Learning more predicates doesn't improve quality. Breaking.")
        print("Final clause:", curr_clause)
        break
        #pass

    curr_clause.append(list(best_pred[0]))
    print(curr_clause)
    info_gains.append(best_pred[1])
    if best_pred[0][1] not in usable_variables:
        usable_variables.append(best_pred[0][1])
    if len(best_pred[0]) > 2 and best_pred[0][2] not in usable_variables:
        usable_variables.append(best_pred[0][2])
    print(usable_variables)
    # update the set of negative examples still satisfied
    new_rule_neg = [(state, X, Y) for (state, X, Y) in new_rule_neg if test(state, curr_clause, X, Y)]
    print("Cardinality of new_rule_neg is", len(new_rule_neg))

disj.append(curr_clause)
# Remove the positive examples that satisfy the previous clause
pos = [(state, X, Y) for (state, X, Y) in pos if not test(state, curr_clause, X, Y)]
print("Cardinality of pos is", len(pos))
input()


# In[ ]:


# determines the predicting power of an arbitrary-length chain P(A, Z), P(Z, W), ..., P(Q, B) via the two values count(move(X, Y) and P(X, Y)) and count(P(X, Y))
# considers the clause to be the "or" of clauses of all possible lengths

# actually wait no I should probably make a new on-chain clause and have special "test" rules
def get_pred_power_for_chain(pos, neg, singular_clause): # singular_clause is just P(A, B)
    this_and_move_true = 0
    this_true = 0
    new_ext_vars = new_existential_vars_chain(5)
    for i in range(2, 6): # length of the chain
        lits_to_add = [] # the chain of literals to add
        lits_to_add.append([best_pred[0][0], best_pred[0][1], new_ext_vars[0]])
        for j in range(1, i - 1):
            lits_to_add.append([best_pred[0][0], new_ext_vars[j - 1], new_ext_vars[j]])
        lits_to_add.append([best_pred[0][0], new_ext_vars[i - 2], best_pred[0][2]])
        print(lits_to_add)
        input()
        this_and_move_true, this_true = get_pred_power(pos, neg, curr_clause + lits_to_add)
        # ...
    '''for state, state_table in zip(stackings, table):
        this_and_move_true += len([(X, Y) for (X, Y) in state_table if test(state, clause, X, Y) and state_table[X, Y]])
        this_true += len([(X, Y) for (X, Y) in state_table if test(state, clause, X, Y)])
        print("The condition", clause, "is satisfied by these:", [(X, Y) for (X, Y) in state_table if test(state, clause, X, Y)])'''
    print("About to test first thing")
    this_and_move_true = len([(state, X, Y) for (state, X, Y) in pos if test(state, clause, X, Y)])
    print("About to test second thing")
    this_true = len([(state, X, Y) for (state, X, Y) in pos + neg if test(state, clause, X, Y)])
    return this_and_move_true, this_true


# In[ ]:




