# Method of Equal Shares 

## Overview

The script defines a function:

```python
elect_next_budget_item(votes: list[set[str]],
                       balances: list[float],
                       costs: dict[str, float]) -> None
```

* **votes**: A list of ballots, where each ballot is a `set` of project names that the citizen supports.
* **balances**: A list of floating-point numbers representing each citizen’s available budget.
* **costs**: A dictionary mapping each project name to its total cost.

The function performs these steps:

1. **Viability check**: For each project, verifies if the total available balances of its supporters cover its cost. Projects that cannot be fully funded are skipped.
2. **Threshold computation**: For viable projects, computes the minimal per-supporter payment (threshold) needed to cover the cost. Citizens who cannot pay the full share contribute all they have; the remainder is redistributed among the others.
3. **Selection**: Elects the project with the lowest threshold.
4. **Payment**: Deducts each supporter’s payment from their balance and prints the results.

## Usage

1. **Clone the repository** (or copy the script file).
2. **Ensure you have Python 3.7+** installed.
3. **Import and call** the function in your script or run the examples below.

## Example 1: All supporters can pay equally

```python
if __name__ == "__main__":
    votes    = [{"A","B"}, {"A","C"}, {"B","C"}]
    balances = [1.0,       1.0,        1.0]
    costs    = {"A": 2.0, "B": 1.5,    "C": 3.0}

    elect_next_budget_item(votes, balances, costs)
    # Expected output:
    # Round 1: "B" is elected.
    # Citizen 1 pays 0.75 and has 0.25 remaining.
    # Citizen 3 pays 0.75 and has 0.25 remaining.
```

## Example 2: One supporter cannot afford their share

```python
if __name__ == "__main__":
    votes    = [{"X"}, {"X"}, {"X"}]
    balances = [0.3,     1.0,     1.0]
    costs    = {"X": 1.5}

    elect_next_budget_item(votes, balances, costs)
    # Expected output:
    # Round 1: "X" is elected.
    # Citizen 1 pays 0.30 and has 0.00 remaining.
    # Citizen 2 pays 0.60 and has 0.40 remaining.
    # Citizen 3 pays 0.60 and has 0.40 remaining.
```

## Credits
chatGPT - [Link](https://chatgpt.com/share/68376415-e134-800b-8a75-e3dfba029ed6)
