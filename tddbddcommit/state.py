from tddbddcommit import Kind


def allowed(current_state, proposed_state):
    if not current_state:
        allowed = _allowed_from_start(proposed_state)
    elif current_state is Kind.initial:
        allowed = _allowed_from_initial(proposed_state)
    elif current_state is Kind.red:
        allowed = _allowed_from_red(proposed_state)
    elif (current_state is Kind.green or
          current_state is Kind.refactor or
          current_state is Kind.merge or
          current_state is Kind.beige):
        allowed = _allowed_from_green_refactor_merge_beige(proposed_state)
    return allowed


def _allowed_from_start(proposed_state):
    if proposed_state is Kind.initial:
        return True
    else:
        return False


def _allowed_from_initial(proposed_state):
    if (proposed_state is Kind.red or
       proposed_state is Kind.merge or
       proposed_state is Kind.beige):
        return True
    else:
        return False


def _allowed_from_red(proposed_state):
    if proposed_state is Kind.green:
        return True
    else:
        return False


def _allowed_from_green_refactor_merge_beige(proposed_state):
    if (proposed_state is Kind.refactor or
       proposed_state is Kind.red or
       proposed_state is Kind.merge or
       proposed_state is Kind.beige):
        return True
    else:
        return False
