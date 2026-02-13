def diff_states(prev, curr):
    changes = {}

    prev_locals = prev.locals
    curr_locals = curr.locals

    for key in curr_locals:
        if key not in prev_locals:
            changes[key] = ("ADDED", curr_locals[key])
        elif prev_locals[key] != curr_locals[key]:
            changes[key] = ("MODIFIED", curr_locals[key])

    for key in prev_locals:
        if key not in curr_locals:
            changes[key] = ("REMOVED", None)

    return changes
