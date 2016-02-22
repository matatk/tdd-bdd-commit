from tddbddcommit import Kind


def allowed(current_state, proposed_state):
    if not current_state:
        return proposed_state is Kind.initial
    if current_state is Kind.initial:
        return proposed_state in [Kind.red, Kind.merge, Kind.beige]
    if current_state is Kind.red:
        return proposed_state is Kind.green
    return proposed_state not in [Kind.initial, Kind.green]
