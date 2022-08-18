#!/usr/bin/env python
# coding: utf-8

# In[19]:


num_blocks = 4


# In[2]:


stackings = [[['a'], ['b'], ['c'], ['d']], [['a'], ['b'], ['c', 'd']], [['a'], ['c'], ['b', 'd']], [['a'], ['d'], ['b', 'c']], [['a'], ['b', 'c', 'd']], [['d'], ['b', 'c', 'a']], [['a'], ['b'], ['d', 'c']], [['b'], ['d'], ['a', 'c']], [['b'], ['a', 'c', 'd']], [['b', 'c'], ['d', 'a']], [['b'], ['d'], ['c', 'a']], [['b'], ['c'], ['d', 'a']], [['c', 'b'], ['d', 'a']], [['a'], ['d'], ['c', 'b']], [['a', 'd'], ['c', 'b']], [['b'], ['c'], ['a', 'd']], [['b'], ['a', 'd', 'c']], [['a', 'd'], ['b', 'c']], [['a'], ['c', 'd', 'b']], [['a', 'b'], ['c', 'd']], [['c'], ['a', 'd', 'b']], [['c'], ['d'], ['a', 'b']], [['a', 'c'], ['b', 'd']], [['a'], ['b', 'd', 'c']], [['d'], ['a', 'c', 'b']], [['a', 'b'], ['d', 'c']], [['a'], ['d', 'c', 'b']], [['b', 'a'], ['d', 'c']], [['b'], ['d', 'c', 'a']], [['d'], ['b', 'a', 'c']], [['c'], ['d'], ['b', 'a']], [['b'], ['c', 'a', 'd']], [['a', 'c'], ['d', 'b']], [['a'], ['d', 'b', 'c']], [['a'], ['c'], ['d', 'b']], [['c'], ['b', 'a', 'd']], [['d'], ['a', 'b', 'c']], [['b', 'd'], ['c', 'a']], [['b', 'a'], ['c', 'd']], [['b'], ['c', 'd', 'a']], [['c'], ['d', 'a', 'b']], [['a'], ['c', 'b', 'd']], [['c'], ['a', 'b', 'd']], [['b'], ['d', 'a', 'c']], [['d'], ['c', 'a', 'b']], [['c', 'a'], ['d', 'b']], [['c'], ['d', 'b', 'a']], [['c'], ['b', 'd', 'a']], [['d'], ['c', 'b', 'a']]]


# In[3]:


Qtable = [{('d', 'c'): -0.8799224863146268, ('a', 'c'): -1.7594868650307736, ('b', 'c'): -1.1898012699240088, ('d', 'a'): 1.1147301159233773, ('c', 'a'): 0.9854028484952575, ('a', 'b'): -1.7006054795697512, ('d', 'b'): -0.8887839152885366, ('a', 'floor'): -1.5535169337431274, ('c', 'floor'): -1.7952527419380173, ('c', 'd'): -0.7228191450461644, ('b', 'd'): -1.0631639331635185, ('b', 'a'): 0.7477291547026269, ('c', 'b'): -0.9387440790325181, ('a', 'd'): -1.7333048672022264, ('b', 'floor'): -1.681999463919989, ('d', 'floor'): -1.3884588896363736}, {('d', 'b'): -0.8864937732721014, ('b', 'd'): 1.1109808268398145, ('d', 'floor'): -1.251674445207576, ('a', 'd'): 0.4248564738660709, ('a', 'b'): -1.3026086298692725, ('b', 'a'): 1.48048770343943, ('d', 'a'): 1.345009590192296, ('a', 'floor'): -0.9116794848452175, ('b', 'floor'): -1.4858117397757484}, {('a', 'floor'): -0.9404507043285735, ('c', 'a'): 1.2482103426611557, ('c', 'd'): 1.1705611678085306, ('d', 'floor'): -1.5689116659935554, ('c', 'floor'): -0.9318149018904767, ('a', 'd'): 0.3292042216328679, ('d', 'a'): 1.1118387858223284, ('d', 'c'): -1.1430090434455775, ('a', 'c'): -1.3108655322774134}, {('d', 'c'): 1.0207393479438083, ('a', 'floor'): -0.8577431519649532, ('c', 'd'): -1.0536713759182934, ('d', 'floor'): -0.9467989578574356, ('c', 'a'): 1.2198301654853891, ('d', 'a'): 1.5721278023131025, ('a', 'd'): -1.2078046765651884, ('a', 'c'): 0.6869402587817769, ('c', 'floor'): -1.4584273409501007}, {('d', 'floor'): -0.8216489715690515, ('d', 'a'): 1.4477538005262787, ('a', 'floor'): 1.1209583914492536, ('a', 'd'): 8.0}, {('a', 'floor'): -0.9484297832353179, ('d', 'a'): 8.0, ('a', 'd'): -1.0792633341532918, ('d', 'floor'): 0.6894939295686853}, {('c', 'a'): 0.40418466349391785, ('a', 'floor'): -0.6933820184750966, ('c', 'floor'): -1.5089166388074415, ('a', 'c'): 0.6080298020426369, ('b', 'a'): 1.2212154814547005, ('b', 'floor'): -0.5958399156921439, ('b', 'c'): 1.0284532523447862, ('c', 'b'): -0.7452341482288629, ('a', 'b'): -1.424249739631268}, {('d', 'c'): 9.521296085661094, ('b', 'floor'): 0.5461336462992137, ('b', 'c'): 10.222911455043258, ('b', 'd'): 2.091016170358899, ('c', 'b'): -0.7354526360441522, ('d', 'floor'): 0.8535379392664565, ('c', 'd'): -1.1828491558095546, ('c', 'floor'): -1.442324717590437, ('d', 'b'): 1.2064187771300494}, {('d', 'floor'): 1.437277729311004, ('d', 'b'): 0.8347152373900951, ('b', 'd'): 40.0, ('b', 'floor'): 10.834466526856456}, {('a', 'c'): 0.41888160609786357, ('c', 'a'): 0.3091179106937471, ('a', 'floor'): -0.9321832947626368, ('c', 'floor'): -1.7074459400499253}, {('a', 'floor'): -1.5758417177145, ('b', 'floor'): -1.6401346303251654, ('b', 'a'): 0.34482988554677246, ('a', 'b'): -1.5955232249434697, ('d', 'b'): -1.2543124436179824, ('d', 'floor'): -1.7086932801369772, ('a', 'd'): -1.6163135371086161, ('d', 'a'): -0.09295204242096956, ('b', 'd'): -1.0101581325539346}, {('b', 'c'): -1.2865439238639376, ('b', 'floor'): -1.7150959475768142, ('c', 'a'): 0.3201086176935008, ('a', 'c'): -1.6246368866637622, ('a', 'floor'): -1.3721598934974593, ('c', 'b'): -1.1617642155702528, ('b', 'a'): 0.37234518501953434, ('c', 'floor'): -1.6993952350302688, ('a', 'b'): -1.9253488741998985}, {('a', 'floor'): -0.8340757963219905, ('b', 'a'): 0.3324500853191201, ('b', 'floor'): -1.7061256196120704, ('a', 'b'): 0.3161877532458175}, {('a', 'd'): -1.1297365165942448, ('a', 'floor'): -0.7793841505001238, ('d', 'floor'): -0.991531107645212, ('d', 'a'): 1.3912017932762275, ('b', 'd'): -0.7784450747781514, ('d', 'b'): 0.9220742697120963, ('b', 'a'): 0.6308239485612576, ('a', 'b'): 0.27453413776305197, ('b', 'floor'): -1.6917420707586104}, {('b', 'floor'): 0.8232216898519765, ('d', 'floor'): -1.0304117551177383, ('b', 'd'): 9.642921170403714, ('d', 'b'): 1.1903274473871508}, {('b', 'floor'): 0.9817183602060555, ('d', 'c'): -0.9873574681624465, ('c', 'b'): 2.3531800319885545, ('c', 'floor'): 0.5721031296580745, ('d', 'b'): -0.946454030999512, ('b', 'c'): 1.660823699154336, ('d', 'floor'): -1.4391653191929916, ('c', 'd'): 9.3246713322399, ('b', 'd'): 9.577141385779282}, {('c', 'floor'): 1.21335146029564, ('c', 'b'): 1.2242934126849898, ('b', 'c'): 40.0, ('b', 'floor'): 10.655024594852184}, {('c', 'd'): 11.095821119602286, ('d', 'c'): 1.2959644287510266, ('c', 'floor'): 0.8813248983063288, ('d', 'floor'): -0.8787029214155803}, {('b', 'a'): 1.0194440946377903, ('a', 'floor'): 1.1924954282679505, ('a', 'b'): 8.0, ('b', 'floor'): -0.9553345324829037}, {('b', 'floor'): -0.8053371041199718, ('d', 'floor'): 0.4393553739199318, ('b', 'd'): 0.9211319724981434, ('d', 'b'): 9.734894167322095}, {('c', 'b'): 40.0, ('b', 'c'): 1.8461896340161583, ('b', 'floor'): 1.3481608970383, ('c', 'floor'): 9.960777382886754}, {('b', 'c'): -0.8241379819528873, ('c', 'b'): 9.158816677757994, ('d', 'floor'): 1.0453563556051826, ('c', 'd'): 1.83684266660077, ('b', 'floor'): -1.5379167740526807, ('b', 'd'): -0.7416255281771839, ('c', 'floor'): 0.9236611565174873, ('d', 'c'): 1.4291995565894888, ('d', 'b'): 9.187501941083895}, {('c', 'd'): 0.7350828845610519, ('d', 'floor'): 1.488958356907042, ('c', 'floor'): -0.7993638384902618, ('d', 'c'): 9.103836279745769}, {('a', 'floor'): 1.5281549924811593, ('a', 'c'): 8.0, ('c', 'a'): 0.7797527980190152, ('c', 'floor'): -0.8426149255628714}, {('b', 'floor'): 1.4939797212026527, ('b', 'd'): 2.0473505501631983, ('d', 'floor'): 10.537822383535927, ('d', 'b'): 40.0}, {('b', 'c'): 1.1835096233734093, ('c', 'b'): 10.164559862919779, ('b', 'floor'): -0.8722200077200777, ('c', 'floor'): 1.271702866026981}, {('b', 'floor'): -1.0282215272848985, ('a', 'b'): 8.0, ('b', 'a'): 1.6321529417607554, ('a', 'floor'): 1.3702735846789462}, {('a', 'c'): 0.32339627450659136, ('c', 'floor'): -1.8294652043715673, ('c', 'a'): 0.3585206161310635, ('a', 'floor'): -0.8503068779682683}, {('a', 'floor'): -0.7232899523119348, ('a', 'b'): -1.0814623322924488, ('b', 'floor'): 0.20360792947515555, ('b', 'a'): 8.0}, {('d', 'floor'): 0.3041907292756712, ('c', 'd'): -1.417168467487255, ('c', 'floor'): -1.6938144215371504, ('d', 'c'): 8.0}, {('c', 'a'): -0.05276624940533462, ('d', 'a'): 0.38887499363515143, ('c', 'floor'): -1.6766553589305926, ('a', 'd'): -1.6196706265260603, ('d', 'floor'): -1.634526770202357, ('c', 'd'): -0.9845570429889066, ('d', 'c'): -1.1146452198124506, ('a', 'c'): -1.7301602683497974, ('a', 'floor'): -1.4960553196511224}, {('b', 'floor'): 0.17496212649345327, ('b', 'd'): 8.0, ('d', 'b'): -1.5217364192046563, ('d', 'floor'): -1.4014914411917265}, {('c', 'b'): 1.0752042896666754, ('b', 'c'): 9.764544065016109, ('b', 'floor'): 1.3335342397160836, ('c', 'floor'): -0.7770658510587254}, {('c', 'floor'): -0.9778406208205173, ('a', 'floor'): 1.120978075356336, ('a', 'c'): 8.0, ('c', 'a'): 1.2914811042047687}, {('b', 'c'): -1.309720047409194, ('b', 'a'): 1.170893252976232, ('c', 'b'): 1.103201300940079, ('c', 'floor'): -0.8705592415673278, ('a', 'c'): -1.089336642950644, ('c', 'a'): 1.6092586046259905, ('a', 'b'): 0.493899031319318, ('a', 'floor'): -0.9111275596384402, ('b', 'floor'): -1.5085670591779088}, {('c', 'd'): 8.0, ('d', 'c'): -1.3617766906804698, ('c', 'floor'): 0.3807831603495104, ('d', 'floor'): -1.5997789604488233}, {('c', 'd'): 1.224585818629204, ('d', 'c'): 40.0, ('d', 'floor'): 9.708744225529776, ('c', 'floor'): 1.0988441419785984}, {('a', 'floor'): -1.1892748335900223, ('a', 'd'): 0.2454530803687117, ('d', 'floor'): -1.7516269978436334, ('d', 'a'): 0.2883450618697719}, {('a', 'floor'): -1.0237536630069843, ('d', 'floor'): -1.7006852629295346, ('a', 'd'): 0.3120697273770399, ('d', 'a'): 0.20598138595442217}, {('a', 'b'): -1.3335396683136866, ('a', 'floor'): -0.9987855348221111, ('b', 'floor'): 0.3873673037484177, ('b', 'a'): 8.0}, {('c', 'floor'): 0.26960067985773173, ('b', 'c'): -0.8317565297746382, ('c', 'b'): 8.0, ('b', 'floor'): -1.6068420876900629}, {('a', 'floor'): 0.8688225522019892, ('a', 'd'): 8.0, ('d', 'a'): 1.0609539452352688, ('d', 'floor'): -1.1515964466753583}, {('d', 'floor'): 1.347612314328975, ('d', 'c'): 1.3282490879088955, ('c', 'floor'): 10.429193035878061, ('c', 'd'): 40.0}, {('c', 'floor'): -1.6494055456799004, ('b', 'c'): 7.982683982683983, ('b', 'floor'): 0.5851461605524686, ('c', 'b'): -1.1367236766843558}, {('b', 'floor'): -1.7101630150003022, ('b', 'd'): -0.9260223009357824, ('d', 'b'): 8.0, ('d', 'floor'): 0.3297110564140052}, {('a', 'b'): 0.656055791839485, ('b', 'floor'): -1.8269026409501066, ('b', 'a'): 0.4776400563060801, ('a', 'floor'): -0.6220544527559453}, {('c', 'a'): 8.0, ('a', 'floor'): -0.834305509432251, ('a', 'c'): -0.866621176246276, ('c', 'floor'): 0.4351091953951895}, {('a', 'c'): -1.0358959909215573, ('a', 'floor'): -1.197414893177425, ('c', 'floor'): 0.20983200041220956, ('c', 'a'): 8.0}, {('d', 'floor'): 0.13388978299010448, ('d', 'a'): 8.0, ('a', 'd'): -0.9933600134692215, ('a', 'floor'): -0.9247237070878128}]


# In[4]:


blocks = ['a', 'b', 'c', 'd', 'floor']


# In[5]:


move_table = [] # fill this with the same info as Qtable, except where each move gets a "true" or "false"
for Qstate in Qtable:
    move_state = dict()
    for act in Qstate:
        move_state[act] = (Qstate[act] > 0.9) # A cutoff of 0.9 was decided as it gives almost the same true positive and true negative rates
    move_table.append(move_state)
#print(move_table)


# In[6]:


def location(state, X):
    for i, col in enumerate(state):
        if X in col:
            colnum = i
            rownum = 3 - col.index(X)
            return (rownum, colnum)
    return (-1, -1)


# In[7]:


def on(state, X, Y):
    if (location(state, X)[0] == 3 and Y == 'floor'):
        return True
    if (location(state, X)[0] == location(state, Y)[0] - 1 and location(state, X)[1] == location(state, Y)[1]):
        return True
    return False


# In[8]:


def top(state, X):
    if X == 'floor':
        return False
    loc = location(state, X)
    return len(state[loc[1]]) == 4 - loc[0]


# In[9]:


def isFloor(stack, X):
    return X == 'floor'


# In[63]:


preds = ['on', 'top', 'isFloor', 'neq']


# In[123]:


import random

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
        possible_assignments = [x for x in possible_assignments if on(state, X, x[0])]
        for j in range(1, i - 1):
            #lits_to_add.append([best_pred[0][0], new_ext_vars[j - 1], new_ext_vars[j]])
            possible_assignments = [x for x in possible_assignments if on(state, x[j - 1], x[j])]
            if len(possible_assignments) == 0:
                break
        #lits_to_add.append([best_pred[0][0], new_ext_vars[i - 2], best_pred[0][2]])
        possible_assignments = [x for x in possible_assignments if on(state, x[i - 2], Y)]
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
        return

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

def new_existential_var(unusable_variables):
    if 'Z' not in unusable_variables: return 'Z'
    else:
        for i in range(ord('V'), ord('A') - 1, -1):
            if chr(i) not in unusable_variables:
                return chr(i)
        print("Error: out of variables")
        return None

def new_existential_vars_chain(n_vars, unusable_variables):
    potential_variables = ['Z'] + [chr(i) for i in range(ord('V'), ord('A') - 1, -1)]
    variables = []
    var_ind = 0
    for i in range(n_vars):
        if var_ind > len(potential_variables):
            print("Error: out of variables")
        while potential_variables[var_ind] in unusable_variables:
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
neg = [] # negative examples, which are just all pairs of blocks that don't satisfy our Q-table approximation to move(X, Y)

# get the examples from n randomly chosen states (for more variation while training)
def random_state_examples(n):
    random_stackings = random.sample(stackings, n)
    random_pos = [x for x in pos if x[0] in random_stackings]
    random_neg = [x for x in neg if x[0] in random_stackings]
    return random_pos, random_neg

def print_if_allowed(allowed, *args):
    if allowed:
        print(*args)

def learn_horn_clause(print_messages=True):
    global pos, neg

    for state, move_state in zip(stackings, move_table):
        for (X, Y) in move_state:
            if move_state[(X, Y)]:
                pos.append((state, X, Y))

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
            random_pos, random_neg = random_state_examples(3) # use random examples to test our predicate, introduces a degree of randomness into the computation
            ev = new_existential_var(usable_variables)
            if pred in ['top', 'isFloor']: # these predicates only take one argument
                for var in usable_variables + [ev]:
                    test_pred = [pred, var]
                    if test_pred in curr_clause:
                        continue
                    print_if_allowed(print_messages, "get predicting power of", curr_clause + [test_pred])
                    this_and_move_true, this_true = get_pred_power(random_pos, random_neg, curr_clause + [test_pred])
                    print_if_allowed(print_messages, "the predicting power is {}/{}".format(this_and_move_true, this_true))
                    if this_true == 0:
                        continue
                    pred_power = this_and_move_true/this_true
                    info_gain[tuple([pred, var])] = pred_power
            if pred in ['on', 'neq']: # on, neq, and move take two arguments
                for var1 in usable_variables + [ev]:
                    for var2 in usable_variables + [ev]:
                        test_pred = [pred, var1, var2]
                        if test_pred in curr_clause:
                            continue
                        print_if_allowed(print_messages, "get predicting power of", curr_clause + [test_pred])
                        this_and_move_true, this_true = get_pred_power(random_pos, random_neg, curr_clause + [test_pred])
                        print_if_allowed(print_messages, "the predicting power is {}/{}".format(this_and_move_true, this_true))
                        if this_true == 0:
                            continue
                        pred_power = this_and_move_true/this_true
                        info_gain[tuple([pred, var1, var2])] = pred_power
        print_if_allowed(print_messages, info_gain)
        if len(info_gain) == 0:
            print_if_allowed(print_messages, "The length of info_gain is 0, no more predicates to add")
            break
        best_pred = max(list(info_gain.items()), key=lambda x: x[1])
        print_if_allowed(print_messages, "best pred is", best_pred)
        # see if replacing the last predicate with a chain of predicates does any better
        #input()

        # for testing purposes
        #best_pred = (['on', 'Z', 'a'], 0.5)

        if best_pred[0][0] == 'on' and (best_pred[0][1] not in usable_variables and best_pred[0][2] in usable_variables or best_pred[0][1] in usable_variables and best_pred[0][2] not in usable_variables):
            # We're going to use the same random_pos and random_neg as above
            '''# choose sample of positive and negative samples randomly from one of the examples
            i = random.randrange(len(stackings))
            print_if_allowed(print_messages, "Random state chosen:", stackings[i])
            #input()
            new_pos = [(stackings[i], x, y) for (x, y) in move_table[i] if move_table[i][(x, y)]]
            new_neg = []
            for X in blocks:
                for Y in blocks:
                    if (X, Y) not in move_table[i] or not move_table[i][(X, Y)]:
                        new_neg.append((state, X, Y))'''
            better_pred_powers = dict()
            if best_pred[0][1] in usable_variables:
                index_with_free = 2
                index_with_bound = 1
            else:
                index_with_free = 1
                index_with_bound = 2
            new_ext_vars = new_existential_vars_chain(5, usable_variables + [best_pred[0][1], best_pred[0][2]]) # a set of new existential variables we are going to need
            for i in range(2, num_blocks + 2): # length of the chain
                lits_to_add = [] # the chain of literals to add
                new_lit = [best_pred[0][0], None, None]
                new_lit[index_with_bound] = best_pred[0][index_with_bound]
                new_lit[index_with_free] = new_ext_vars[0]
                lits_to_add.append(new_lit)
                for j in range(1, i - 1):
                    new_lit = [best_pred[0][0], None, None]
                    new_lit[index_with_bound] = new_ext_vars[j - 1]
                    
                    new_lit[index_with_free] = new_ext_vars[j]
                    lits_to_add.append(new_lit)
                new_lit = [best_pred[0][0], None, None]
                new_lit[index_with_bound] = new_ext_vars[i - 2]
                lits_to_add.append(None)
                # Try putting any of the usable_variables at the end of the chain
                for var in usable_variables:
                    #new_lit[index_with_free] = best_pred[0][index_with_free] # this isn't entirely correct, we want to test out a bunch of different usable_variables at this index
                    # (because this is what my algorithm outlined in the class project does)
                    # Update: Fixed
                    new_lit[index_with_free] = var
                    lits_to_add[-1] = new_lit
                    print_if_allowed(print_messages, "Testing the chain", lits_to_add)
                    #print("Original predicate:", best_pred[0])
                    this_and_move_true, this_true = get_pred_power(random_pos, random_neg, curr_clause + lits_to_add)
                    if (this_and_move_true, this_true) != (0, 0):
                        lits_to_add_as_tuple = tuple(tuple(x) for x in lits_to_add)
                        better_pred_powers[lits_to_add_as_tuple] = this_and_move_true/this_true
                    # ...
            if any([better_pred_powers[x] > best_pred[1] for x in better_pred_powers]):
                best_chain = max(list(better_pred_powers.items()), key=lambda x: x[1])[0]
                print_if_allowed(print_messages, best_chain)
                best_pred = [['on-chain', best_chain[0][index_with_bound], best_chain[-1][index_with_free]], max(list(better_pred_powers.items()), key=lambda x: x[1])[1]]
                print_if_allowed(print_messages, best_chain, "does better than", best_pred[0])
            else:
                print_if_allowed(print_messages, "Nothing does better than", best_pred[0])

        '''if best_pred[0][0] == 'on':
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
                '''
        # test if curr_clause + best_pred is actually an improvement over any of the last three clauses
        # if not, learning more predicates seems to be futile
        if len(info_gains) >= 3 and all([best_pred[1] <= x for x in info_gains[-3:]]):
            print_if_allowed(print_messages, "Learning more predicates doesn't improve quality. Breaking.")
            print_if_allowed(print_messages, "Final clause:", curr_clause)
            break
            #pass

        curr_clause.append(list(best_pred[0]))
        print_if_allowed(print_messages, curr_clause)
        info_gains.append(best_pred[1])
        if best_pred[0][1] not in usable_variables:
            usable_variables.append(best_pred[0][1])
        if len(best_pred[0]) > 2 and best_pred[0][2] not in usable_variables:
            usable_variables.append(best_pred[0][2])
        print_if_allowed(print_messages, usable_variables)
        # update the set of negative examples still satisfied
        new_rule_neg = [(state, X, Y) for (state, X, Y) in new_rule_neg if test(state, curr_clause, X, Y)]
        print_if_allowed(print_messages, "Cardinality of new_rule_neg is", len(new_rule_neg))

    # Remove the positive examples that satisfy the previous clause
    pos = [(state, X, Y) for (state, X, Y) in pos if not test(state, curr_clause, X, Y)]
    print_if_allowed(print_messages, "Cardinality of pos is", len(pos))

    return curr_clause

print("Learned clause", learn_horn_clause())


# In[124]:


# Including this even though I don't think I need it anymore

# determines the predicting power of an arbitrary-length chain P(A, Z), P(Z, W), ..., P(Q, B) via the two values count(move(X, Y) and P(X, Y)) and count(P(X, Y))
# considers the clause to be the "or" of clauses of all possible lengths

# actually wait no I should probably make a new on-chain clause and have special "test" rules
def get_pred_power_for_chain(pos, neg, singular_clause): # singular_clause is just P(A, B)
    this_and_move_true = 0
    this_true = 0
    new_ext_vars = new_existential_vars_chain(5, usable_variables)
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


def get_rates(conj):
    true_pos = 0
    false_pos = 0
    true_neg = 0
    false_neg = 0
    for state, move_state in zip(stackings, move_table):
        for X in blocks:
            for Y in blocks:
                if (X, Y) in move_state and move_state[(X, Y)]:
                    if test(state, conj, X, Y):
                        true_pos += 1
                    else:
                        false_neg += 1
                else:
                    if test(state, conj, X, Y):
                        false_pos += 1
                    else:
                        true_neg += 1
    return true_pos, false_pos, true_neg, false_neg

# learn horn clause several times, see if it ever learns "correctly" (or close to it)
rates = [] # is this precisions? recalls? what?
for i in range(100):
    learned_clause = learn_horn_clause(print_messages=False)
    print(learned_clause)
    true_pos, false_pos, true_neg, false_neg = get_rates(learned_clause)
    print(true_pos/(true_pos + false_neg)) # fraction of positive examples correctly predicted as positive
    print(true_neg/(false_pos + true_neg)) # fraction of negative examples correctly predicted as negative
    rates.append(true_pos/(true_pos + false_neg))

print("The maximum success rate is", max(rates), "at index", rates.index(max(rates)))


# In[24]:


# Info:
# The above mostly follows the algorithm described in my class project in https://docs.google.com/document/d/1sNrIA3QxtSknMTQKFqKfFiTlg7pSnEQg_wqc2VAt-sU/edit
# Instead of "has one free and one bound variable", we require the "on" literal to have one variable not bound by any previous literals in the clause, and one that is.


# In[ ]:


# Printing all learned actions and rewards
for state, Qstate in zip(stackings, Qtable):
    print(str(state) + ':')
    for act in Qstate:
        print("\tmove({}, {}) = {} (reward = {})".format(*act, Qstate[act] > 0.9, Qstate[act]))
    move_table.append(move_state)
#print(move_table)


# In[ ]:




