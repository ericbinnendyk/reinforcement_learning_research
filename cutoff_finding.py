# single function from q_learning_and_cutoff_finding.py, for use as a library file

# find optimal threshold for converting numeric values of actions into yes/no policy for each action
# this function finds a threshold with predicts the idealized move() policy with almost the same level of sensitivity as specificity
def find_cutoff_value(stackings, Qtable):
    # In general, higher action values should correspond to actions that are part of the move() policy.
    # First, refactor Q table into a single dictionary: (state_ID, X, Y) -> value
    Qtable_dict = {}
    for i, Qstate in enumerate(Qtable):
        for act in Qstate:
            Qtable_dict[(i, act[0], act[1])] = Qstate[act]

    # Set up a list of all action values and corresponding idealized policy values
    data = []
    for key in Qtable_dict:
        data.append([Qtable_dict[key], move(stackings[key[0]], key[1], key[2])])

    sensitivities = []
    specificities = []
    cutoff = -30.0
    while cutoff < 50.0: # may need to change these values
        # fraction of actual positives that are recognized as positive
        sensitivities.append(len([[x, y] for [x, y] in data if x > cutoff and y == True])/len([[x, y] for [x, y] in data if y == True]))
        # fraction of actual negative examples that are recognized as negative
        specificities.append(len([[x, y] for [x, y] in data if x <= cutoff and y == False])/len([[x, y] for [x, y] in data if y == False]))
        cutoff += 0.1
    
    for i in range(len(sensitivities)):
        if specificities[i] > sensitivities[i]:
            if i == 0:
                return -30.0, sensitivities[0], specificities[0]
            # The specificity increases from 0 while the sensitivity decreases from 1. At the crossover point, find the index where the two values are closest, leading to the cutoff point.
            if abs(specificities[i] - sensitivities[i]) > abs(specificities[i - 1] - sensitivities[i - 1]):
                return -30.0 + 0.1*(i - 1), sensitivities[i - 1], specificities[i - 1]
            else:
                return -30.0 + 0.1*i, sensitivities[i], specificities[i]
    return 49.5, sensitivities[-1], specificities[-1] 

