def normalize(state):
    state = state[:] # make a copy
    while [] in state:
        state.remove([])
    return sorted(state, key=lambda x: (len(x), ord(x[0]) if len(x) > 0 else 0))

