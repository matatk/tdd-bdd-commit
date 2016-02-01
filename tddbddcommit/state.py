from tddbddcommit import Kind


def allowed(current_state, proposed_state):
    if not current_state:
        if proposed_state is Kind.initial:
            return True
    elif current_state is Kind.initial:
        if (proposed_state is Kind.red or
           proposed_state is Kind.merge or
           proposed_state is Kind.beige):
            return True
    elif current_state is Kind.red:
        if proposed_state is Kind.green:
            return True
    elif (current_state is Kind.green or
          current_state is Kind.refactor or
          current_state is Kind.merge or
          current_state is Kind.beige):
        if (proposed_state is Kind.refactor or
           proposed_state is Kind.red or
           proposed_state is Kind.merge or
           proposed_state is Kind.beige):
            return True
    return False
