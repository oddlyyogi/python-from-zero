def running_balance(opening, amounts):
    balance = opening
    history = []
    for amount in amounts:
        balance += amount
        history.append(balance)
    assert len(history) == len(amounts), "history must have one entry per amount"
    return history


print(running_balance(100.0, [-4.5, -20.0, 30.0]))
