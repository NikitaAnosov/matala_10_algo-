def elect_next_budget_item(votes: list[set[str]],
                           balances: list[float],
                           costs: dict[str, float]) -> None:
    def compute_payments(supporters: list[int], cost: float):
        # total funds available from supporters
        total_available = sum(balances[i] for i in supporters)
        if total_available < cost:
            # not enough funds — this project is not viable
            return None, float('inf')

        payments = {i: 0.0 for i in supporters}
        remaining = cost
        active = set(supporters)

        while True:
            # equal share among remaining active supporters
            share = remaining / len(active)
            # identify supporters who cannot afford the current share
            poor = [i for i in active if balances[i] < share]

            if not poor:
                # everyone can pay the equal share
                for i in active:
                    payments[i] += share
                threshold = share
                break

            # those who can't pay contribute all they have, then are removed
            for i in poor:
                payments[i] += balances[i]
                remaining -= balances[i]
                active.remove(i)

        return payments, threshold

    thresholds = {}
    all_payments = {}

    # 1. Compute payments and thresholds for each project
    for project, cost in costs.items():
        supporters = [idx for idx, ballot in enumerate(votes) if project in ballot]
        if not supporters:
            continue
        pays, thresh = compute_payments(supporters, cost)
        if pays is None:
            # skip projects that cannot be funded
            continue
        thresholds[project] = thresh
        all_payments[project] = pays

    if not thresholds:
        print("No project can be funded with the current balances.")
        return

    # 2. Choose the project with the lowest threshold
    next_proj = min(thresholds, key=lambda p: thresholds[p])

    # 3. Deduct payments and update balances
    print(f'Round 1: "{next_proj}" is elected.')
    for i in sorted(all_payments[next_proj]):
        pay = all_payments[next_proj][i]
        balances[i] -= pay
        print(f"Citizen {i+1} pays {pay:.2f} and has {balances[i]:.2f} remaining.")

if __name__ == "__main__":
    # Example 1: all supporters can pay equally
    votes    = [{"A","B"}, {"A","C"}, {"B","C"}]
    balances = [1.0,       1.0,        1.0]
    costs    = {"A": 2.0, "B": 1.5,    "C": 3.0}

    elect_next_budget_item(votes, balances, costs)
    # Expected:
    # Round 1: "B" is elected.
    # Citizen 1 pays 0.75 and has 0.25 remaining.
    # Citizen 3 pays 0.75 and has 0.25 remaining.

    # Example 2: one supporter can't afford its share
    votes    = [{"X"}, {"X"}, {"X"}]
    balances = [0.3,     1.0,     1.0]
    costs    = {"X": 1.5}

    elect_next_budget_item(votes, balances, costs)
    # Expected:
    # Round 1: "X" is elected.
    # Citizen 1 pays 0.30 and has 0.00 remaining.
    # Citizen 2 pays 0.60 and has 0.40 remaining.
    # Citizen 3 pays 0.60 and has 0.40 remaining.

