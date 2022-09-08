# This is an attempt to use the FOIL learning algorithm to learn a logical predicate from tabular data about which (state, action) pairs are good moves.

# Include these libraries because they are needed to import Max's results
import pickle
import numpy as np
# Import my code's state normalize function
from normalize import normalize
from cutoff_finding import find_cutoff_value

# import results from previous
with open("maximus_code/V3.1/Dict4.pkl", "rb") as f:
	states = pickle.load(f)
#with open("maximus_code/SDict4.pkl", "rb") as f:
#	states = pickle.load(f)
qtable = np.load("maximus_code/V3.1/Qtable4.npy")

'''stackings = [[['a'], ['b'], ['c'], ['d']], [['a'], ['b'], ['c', 'd']], [['a'], ['c'], ['b', 'd']], [['a'], ['d'], ['b', 'c']], [['a'], ['b', 'c', 'd']], [['d'], ['b', 'c', 'a']], [['a'], ['b'], ['d', 'c']], [['b'], ['d'], ['a', 'c']], [['b'], ['a', 'c', 'd']], [['b', 'c'], ['d', 'a']], [['b'], ['d'], ['c', 'a']], [['b'], ['c'], ['d', 'a']], [['c', 'b'], ['d', 'a']], [['a'], ['d'], ['c', 'b']], [['a', 'd'], ['c', 'b']], [['b'], ['c'], ['a', 'd']], [['b'], ['a', 'd', 'c']], [['a', 'd'], ['b', 'c']], [['a'], ['c', 'd', 'b']], [['a', 'b'], ['c', 'd']], [['c'], ['a', 'd', 'b']], [['c'], ['d'], ['a', 'b']], [['a', 'c'], ['b', 'd']], [['a'], ['b', 'd', 'c']], [['d'], ['a', 'c', 'b']], [['a', 'b'], ['d', 'c']], [['a'], ['d', 'c', 'b']], [['b', 'a'], ['d', 'c']], [['b'], ['d', 'c', 'a']], [['d'], ['b', 'a', 'c']], [['c'], ['d'], ['b', 'a']], [['b'], ['c', 'a', 'd']], [['a', 'c'], ['d', 'b']], [['a'], ['d', 'b', 'c']], [['a'], ['c'], ['d', 'b']], [['c'], ['b', 'a', 'd']], [['d'], ['a', 'b', 'c']], [['b', 'd'], ['c', 'a']], [['b', 'a'], ['c', 'd']], [['b'], ['c', 'd', 'a']], [['c'], ['d', 'a', 'b']], [['a'], ['c', 'b', 'd']], [['c'], ['a', 'b', 'd']], [['b'], ['d', 'a', 'c']], [['d'], ['c', 'a', 'b']], [['c', 'a'], ['d', 'b']], [['c'], ['d', 'b', 'a']], [['c'], ['b', 'd', 'a']], [['d'], ['c', 'b', 'a']]]
# To do: reformat this as Max's result and change the following code

Qtable = [{('d', 'c'): -0.8799224863146268, ('a', 'c'): -1.7594868650307736, ('b', 'c'): -1.1898012699240088, ('d', 'a'): 1.1147301159233773, ('c', 'a'): 0.9854028484952575, ('a', 'b'): -1.7006054795697512, ('d', 'b'): -0.8887839152885366, ('a', 'floor'): -1.5535169337431274, ('c', 'floor'): -1.7952527419380173, ('c', 'd'): -0.7228191450461644, ('b', 'd'): -1.0631639331635185, ('b', 'a'): 0.7477291547026269, ('c', 'b'): -0.9387440790325181, ('a', 'd'): -1.7333048672022264, ('b', 'floor'): -1.681999463919989, ('d', 'floor'): -1.3884588896363736}, {('d', 'b'): -0.8864937732721014, ('b', 'd'): 1.1109808268398145, ('d', 'floor'): -1.251674445207576, ('a', 'd'): 0.4248564738660709, ('a', 'b'): -1.3026086298692725, ('b', 'a'): 1.48048770343943, ('d', 'a'): 1.345009590192296, ('a', 'floor'): -0.9116794848452175, ('b', 'floor'): -1.4858117397757484}, {('a', 'floor'): -0.9404507043285735, ('c', 'a'): 1.2482103426611557, ('c', 'd'): 1.1705611678085306, ('d', 'floor'): -1.5689116659935554, ('c', 'floor'): -0.9318149018904767, ('a', 'd'): 0.3292042216328679, ('d', 'a'): 1.1118387858223284, ('d', 'c'): -1.1430090434455775, ('a', 'c'): -1.3108655322774134}, {('d', 'c'): 1.0207393479438083, ('a', 'floor'): -0.8577431519649532, ('c', 'd'): -1.0536713759182934, ('d', 'floor'): -0.9467989578574356, ('c', 'a'): 1.2198301654853891, ('d', 'a'): 1.5721278023131025, ('a', 'd'): -1.2078046765651884, ('a', 'c'): 0.6869402587817769, ('c', 'floor'): -1.4584273409501007}, {('d', 'floor'): -0.8216489715690515, ('d', 'a'): 1.4477538005262787, ('a', 'floor'): 1.1209583914492536, ('a', 'd'): 8.0}, {('a', 'floor'): -0.9484297832353179, ('d', 'a'): 8.0, ('a', 'd'): -1.0792633341532918, ('d', 'floor'): 0.6894939295686853}, {('c', 'a'): 0.40418466349391785, ('a', 'floor'): -0.6933820184750966, ('c', 'floor'): -1.5089166388074415, ('a', 'c'): 0.6080298020426369, ('b', 'a'): 1.2212154814547005, ('b', 'floor'): -0.5958399156921439, ('b', 'c'): 1.0284532523447862, ('c', 'b'): -0.7452341482288629, ('a', 'b'): -1.424249739631268}, {('d', 'c'): 9.521296085661094, ('b', 'floor'): 0.5461336462992137, ('b', 'c'): 10.222911455043258, ('b', 'd'): 2.091016170358899, ('c', 'b'): -0.7354526360441522, ('d', 'floor'): 0.8535379392664565, ('c', 'd'): -1.1828491558095546, ('c', 'floor'): -1.442324717590437, ('d', 'b'): 1.2064187771300494}, {('d', 'floor'): 1.437277729311004, ('d', 'b'): 0.8347152373900951, ('b', 'd'): 40.0, ('b', 'floor'): 10.834466526856456}, {('a', 'c'): 0.41888160609786357, ('c', 'a'): 0.3091179106937471, ('a', 'floor'): -0.9321832947626368, ('c', 'floor'): -1.7074459400499253}, {('a', 'floor'): -1.5758417177145, ('b', 'floor'): -1.6401346303251654, ('b', 'a'): 0.34482988554677246, ('a', 'b'): -1.5955232249434697, ('d', 'b'): -1.2543124436179824, ('d', 'floor'): -1.7086932801369772, ('a', 'd'): -1.6163135371086161, ('d', 'a'): -0.09295204242096956, ('b', 'd'): -1.0101581325539346}, {('b', 'c'): -1.2865439238639376, ('b', 'floor'): -1.7150959475768142, ('c', 'a'): 0.3201086176935008, ('a', 'c'): -1.6246368866637622, ('a', 'floor'): -1.3721598934974593, ('c', 'b'): -1.1617642155702528, ('b', 'a'): 0.37234518501953434, ('c', 'floor'): -1.6993952350302688, ('a', 'b'): -1.9253488741998985}, {('a', 'floor'): -0.8340757963219905, ('b', 'a'): 0.3324500853191201, ('b', 'floor'): -1.7061256196120704, ('a', 'b'): 0.3161877532458175}, {('a', 'd'): -1.1297365165942448, ('a', 'floor'): -0.7793841505001238, ('d', 'floor'): -0.991531107645212, ('d', 'a'): 1.3912017932762275, ('b', 'd'): -0.7784450747781514, ('d', 'b'): 0.9220742697120963, ('b', 'a'): 0.6308239485612576, ('a', 'b'): 0.27453413776305197, ('b', 'floor'): -1.6917420707586104}, {('b', 'floor'): 0.8232216898519765, ('d', 'floor'): -1.0304117551177383, ('b', 'd'): 9.642921170403714, ('d', 'b'): 1.1903274473871508}, {('b', 'floor'): 0.9817183602060555, ('d', 'c'): -0.9873574681624465, ('c', 'b'): 2.3531800319885545, ('c', 'floor'): 0.5721031296580745, ('d', 'b'): -0.946454030999512, ('b', 'c'): 1.660823699154336, ('d', 'floor'): -1.4391653191929916, ('c', 'd'): 9.3246713322399, ('b', 'd'): 9.577141385779282}, {('c', 'floor'): 1.21335146029564, ('c', 'b'): 1.2242934126849898, ('b', 'c'): 40.0, ('b', 'floor'): 10.655024594852184}, {('c', 'd'): 11.095821119602286, ('d', 'c'): 1.2959644287510266, ('c', 'floor'): 0.8813248983063288, ('d', 'floor'): -0.8787029214155803}, {('b', 'a'): 1.0194440946377903, ('a', 'floor'): 1.1924954282679505, ('a', 'b'): 8.0, ('b', 'floor'): -0.9553345324829037}, {('b', 'floor'): -0.8053371041199718, ('d', 'floor'): 0.4393553739199318, ('b', 'd'): 0.9211319724981434, ('d', 'b'): 9.734894167322095}, {('c', 'b'): 40.0, ('b', 'c'): 1.8461896340161583, ('b', 'floor'): 1.3481608970383, ('c', 'floor'): 9.960777382886754}, {('b', 'c'): -0.8241379819528873, ('c', 'b'): 9.158816677757994, ('d', 'floor'): 1.0453563556051826, ('c', 'd'): 1.83684266660077, ('b', 'floor'): -1.5379167740526807, ('b', 'd'): -0.7416255281771839, ('c', 'floor'): 0.9236611565174873, ('d', 'c'): 1.4291995565894888, ('d', 'b'): 9.187501941083895}, {('c', 'd'): 0.7350828845610519, ('d', 'floor'): 1.488958356907042, ('c', 'floor'): -0.7993638384902618, ('d', 'c'): 9.103836279745769}, {('a', 'floor'): 1.5281549924811593, ('a', 'c'): 8.0, ('c', 'a'): 0.7797527980190152, ('c', 'floor'): -0.8426149255628714}, {('b', 'floor'): 1.4939797212026527, ('b', 'd'): 2.0473505501631983, ('d', 'floor'): 10.537822383535927, ('d', 'b'): 40.0}, {('b', 'c'): 1.1835096233734093, ('c', 'b'): 10.164559862919779, ('b', 'floor'): -0.8722200077200777, ('c', 'floor'): 1.271702866026981}, {('b', 'floor'): -1.0282215272848985, ('a', 'b'): 8.0, ('b', 'a'): 1.6321529417607554, ('a', 'floor'): 1.3702735846789462}, {('a', 'c'): 0.32339627450659136, ('c', 'floor'): -1.8294652043715673, ('c', 'a'): 0.3585206161310635, ('a', 'floor'): -0.8503068779682683}, {('a', 'floor'): -0.7232899523119348, ('a', 'b'): -1.0814623322924488, ('b', 'floor'): 0.20360792947515555, ('b', 'a'): 8.0}, {('d', 'floor'): 0.3041907292756712, ('c', 'd'): -1.417168467487255, ('c', 'floor'): -1.6938144215371504, ('d', 'c'): 8.0}, {('c', 'a'): -0.05276624940533462, ('d', 'a'): 0.38887499363515143, ('c', 'floor'): -1.6766553589305926, ('a', 'd'): -1.6196706265260603, ('d', 'floor'): -1.634526770202357, ('c', 'd'): -0.9845570429889066, ('d', 'c'): -1.1146452198124506, ('a', 'c'): -1.7301602683497974, ('a', 'floor'): -1.4960553196511224}, {('b', 'floor'): 0.17496212649345327, ('b', 'd'): 8.0, ('d', 'b'): -1.5217364192046563, ('d', 'floor'): -1.4014914411917265}, {('c', 'b'): 1.0752042896666754, ('b', 'c'): 9.764544065016109, ('b', 'floor'): 1.3335342397160836, ('c', 'floor'): -0.7770658510587254}, {('c', 'floor'): -0.9778406208205173, ('a', 'floor'): 1.120978075356336, ('a', 'c'): 8.0, ('c', 'a'): 1.2914811042047687}, {('b', 'c'): -1.309720047409194, ('b', 'a'): 1.170893252976232, ('c', 'b'): 1.103201300940079, ('c', 'floor'): -0.8705592415673278, ('a', 'c'): -1.089336642950644, ('c', 'a'): 1.6092586046259905, ('a', 'b'): 0.493899031319318, ('a', 'floor'): -0.9111275596384402, ('b', 'floor'): -1.5085670591779088}, {('c', 'd'): 8.0, ('d', 'c'): -1.3617766906804698, ('c', 'floor'): 0.3807831603495104, ('d', 'floor'): -1.5997789604488233}, {('c', 'd'): 1.224585818629204, ('d', 'c'): 40.0, ('d', 'floor'): 9.708744225529776, ('c', 'floor'): 1.0988441419785984}, {('a', 'floor'): -1.1892748335900223, ('a', 'd'): 0.2454530803687117, ('d', 'floor'): -1.7516269978436334, ('d', 'a'): 0.2883450618697719}, {('a', 'floor'): -1.0237536630069843, ('d', 'floor'): -1.7006852629295346, ('a', 'd'): 0.3120697273770399, ('d', 'a'): 0.20598138595442217}, {('a', 'b'): -1.3335396683136866, ('a', 'floor'): -0.9987855348221111, ('b', 'floor'): 0.3873673037484177, ('b', 'a'): 8.0}, {('c', 'floor'): 0.26960067985773173, ('b', 'c'): -0.8317565297746382, ('c', 'b'): 8.0, ('b', 'floor'): -1.6068420876900629}, {('a', 'floor'): 0.8688225522019892, ('a', 'd'): 8.0, ('d', 'a'): 1.0609539452352688, ('d', 'floor'): -1.1515964466753583}, {('d', 'floor'): 1.347612314328975, ('d', 'c'): 1.3282490879088955, ('c', 'floor'): 10.429193035878061, ('c', 'd'): 40.0}, {('c', 'floor'): -1.6494055456799004, ('b', 'c'): 7.982683982683983, ('b', 'floor'): 0.5851461605524686, ('c', 'b'): -1.1367236766843558}, {('b', 'floor'): -1.7101630150003022, ('b', 'd'): -0.9260223009357824, ('d', 'b'): 8.0, ('d', 'floor'): 0.3297110564140052}, {('a', 'b'): 0.656055791839485, ('b', 'floor'): -1.8269026409501066, ('b', 'a'): 0.4776400563060801, ('a', 'floor'): -0.6220544527559453}, {('c', 'a'): 8.0, ('a', 'floor'): -0.834305509432251, ('a', 'c'): -0.866621176246276, ('c', 'floor'): 0.4351091953951895}, {('a', 'c'): -1.0358959909215573, ('a', 'floor'): -1.197414893177425, ('c', 'floor'): 0.20983200041220956, ('c', 'a'): 8.0}, {('d', 'floor'): 0.13388978299010448, ('d', 'a'): 8.0, ('a', 'd'): -0.9933600134692215, ('a', 'floor'): -0.9247237070878128}]
# To do: also reformat this as Max's result'''

blocks = ['a', 'b', 'c', 'd', 'floor']

# Reformat Max's Q table in my format
Qtable = []

# to do: ask max how/whether he encodes blocks moved to the floor as a possible action (actually he probably doesn't)
for row in qtable:
    curr_state_Q_values = {}
    i = 0
    for i, value in enumerate(row):
        if value != 0:
            src_ind = i % (len(blocks) - 1)
            dest_ind = i // (len(blocks) - 1)
            # special case: both digits in the number in base 4 are the same. in this case, the destination is the floor.
            if src_ind == dest_ind:
                dest_ind = blocks.index('floor')
            src = blocks[src_ind]
            dest = blocks[dest_ind]
            curr_state_Q_values[(src, dest)] = value # to do: has Max updated his code yet so that the destination is a block, not a column?
    Qtable.append(curr_state_Q_values)
    #print(row)
    #print(curr_state_Q_values)
    #input()

# convert a stacking of blocks from Max's format to my format.
def convert_stack_format(m_stacking):
    m_stacking_tuple = eval(m_stacking)
    # In Max's format, each column of the tuple represents a stack, except the last one, which is a list of blocks on the floor.
    # This means that several "distinct" states in Max's state space, even after normalization, map to the same state in my state space and hence there are several rows of the Q table corresponding to the same state, but possibly with a different set of Boolean actions.
    # To do: ask Ramyaa, is this a problem?
    stacking = []
    for i, m_col in enumerate(m_stacking_tuple[:-1]):
        '''# the first element of the outer tuple isn't an actual column, it's the "goal"
        if i == 0:
            continue'''
        col = []
        for blocknum in m_col:
            if blocknum > len(blocks):
                break # we've reached the top of the column
            col.append(blocks[blocknum])
        if col != []:
            stacking.append(col)
    # add blocks in the "floor list"
    for blocknum in m_stacking_tuple[-1]:
        if blocknum > len(blocks):
            break # we've reached the top of the column
        stacking.append([blocks[blocknum]])
    # convert stacking to canonical/sorted form
    stacking = normalize(stacking)
    return stacking

# get list of stackings in the same order they're indexed in the Q table
stackings = []
for i in range(len(states)):
    stackings.append(convert_stack_format(list(states.keys())[list(states.values()).index(i)])) # This one-liner for getting key from value was gotten here: https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/

# print some of the stackings in my list format
#print(stackings[:10])
print("There are", len(stackings), "stackings")

def location(state, X):
    for i, col in enumerate(state):
        if X in col:
            colnum = i
            rownum = 3 - col.index(X)
            return (rownum, colnum)
    return (-1, -1)

def on(state, X, Y):
    if (location(state, X)[0] == 3 and Y == 'floor'):
        return True
    if (location(state, X)[0] == location(state, Y)[0] - 1 and location(state, X)[1] == location(state, Y)[1]):
        return True
    return False

def top(state, X):
    if X == 'floor':
        return False
    loc = location(state, X)
    return len(state[loc[1]]) == 4 - loc[0]

def isFloor(stack, X):
    return X == 'floor'

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

def new_existential_var():
    if 'Z' not in usable_variables: return 'Z'
    else:
        for i in range(ord('V'), ord('A') - 1, -1):
            if chr(i) not in usable_variables:
                return chr(i)
        print("Error: out of variables")
        return None

# try learning without recursive predicates
# This takes time to run. Uncomment the input() statements to see intermediate progress.

optimal_cutoff = find_cutoff_value(stackings, Qtable)
print("Optimal cutoff value {} (sensitivity = {}, specificity = {})".format(*optimal_cutoff))

# convert Q table to Boolean policy based on previously decided cutoff value
move_table = [] # fill this with the same info as Qtable, except where each move gets a "true" or "false"
for Qstate in Qtable:
    move_state = dict()
    for act in Qstate:
        move_state[act] = (Qstate[act] > optimal_cutoff[0])
    move_table.append(move_state)
#print(move_table)
preds = ['on', 'top', 'isFloor', 'neq']

print("An example row from the move table is", move_table[0])

'''
# print learned Boolean tabular policy
for state, Qstate, move_state in zip(stackings, Qtable, move_table):
    print("{}:".format(state))
    for (X, Y) in move_state:
        print("    move({}, {}) = {} (reward = {})".format(X, Y, move_state[(X, Y)], Qstate[(X, Y)]))'''

# learn logical formula for the tabular policy
# To do: This seems to have an infinite loop. Why?
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
