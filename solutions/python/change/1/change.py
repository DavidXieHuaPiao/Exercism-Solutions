def find_fewest_coins(coins, target):
    """
    Determines the fewest number of coins to give a customer to sum up to the target amount.

    Args:
        coins (list): A list of available coin denominations (integers).
        target (int): The target amount of change to be made (integer).

    Returns:
        list: A list of coin denominations that sum up to the target,
              using the fewest possible coins. The list will be sorted.

    Raises:
        ValueError: If the target amount is negative or if the target
                    cannot be made with the given coins.
    """

    # 1. Handle edge cases and input validation
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return [] # No coins needed for a target of 0

    # Sort coins in ascending order. This helps in consistent processing
    # and can sometimes lead to minor optimizations in the loop.
    coins.sort()

    # 2. Initialize dynamic programming array
    # dp[i] will store the list of coins that sum up to amount 'i' with the fewest coins.
    # Initialize with None to indicate that an amount is not yet reachable.
    dp = [None] * (target + 1)
    
    # Base case: 0 coins are needed to make an amount of 0.
    dp[0] = []

    # 3. Fill the dp array
    # Iterate through each possible amount from 1 up to the target.
    for amount in range(1, target + 1):
        min_coins_for_amount = None

        # For each amount, iterate through the available coin denominations.
        for coin in coins:
            # If the current coin is greater than the current amount,
            # it cannot be used to make this amount, so skip it.
            if coin > amount:
                continue

            # Calculate the remaining amount needed after using the current coin.
            prev_amount = amount - coin

            # Check if the 'prev_amount' was reachable (i.e., dp[prev_amount] is not None).
            if dp[prev_amount] is not None:
                # Construct a candidate solution by adding the current coin
                # to the solution for 'prev_amount'.
                current_solution = dp[prev_amount] + [coin]

                # If this is the first solution found for 'amount', or if
                # this solution uses fewer coins than the best one found so far,
                # update min_coins_for_amount.
                if min_coins_for_amount is None or \
                   len(current_solution) < len(min_coins_for_amount):
                    min_coins_for_amount = current_solution
        
        # Store the best solution found for the current 'amount'.
        dp[amount] = min_coins_for_amount

    # 4. Check the final result
    # If dp[target] is still None, it means the target amount cannot be made
    # with the given coin denominations.
    if dp[target] is None:
        raise ValueError("can't make target with given coins")
    
    # Sort the final list of coins for consistent output, as per examples.
    return sorted(dp[target])

# --- Examples from the instructions ---

print("--- Valid Change Scenarios ---")
# Example 1: Amount 15, Coins [1, 5, 10, 25, 100] -> [5, 10]
coins1 = [1, 5, 10, 25, 100]
target1 = 15
print(f"Target {target1} with coins {coins1}: {find_fewest_coins(coins1, target1)}")

# Example 2: Amount 40, Coins [1, 5, 10, 25, 100] -> [5, 10, 25]
coins2 = [1, 5, 10, 25, 100]
target2 = 40
print(f"Target {target2} with coins {coins2}: {find_fewest_coins(coins2, target2)}")

# Example from introduction: Amount 12, Coins [10, 5, 2] -> [2, 10]
coins3 = [10, 5, 2]
target3 = 12
print(f"Target {target3} with coins {coins3}: {find_fewest_coins(coins3, target3)}")

# Another example: Target 7, Coins [1, 3, 4] -> [3, 4]
coins4 = [1, 3, 4]
target4 = 7
print(f"Target {target4} with coins {coins4}: {find_fewest_coins(coins4, target4)}")

print("\n--- Invalid Change Scenarios (Expected Errors) ---")
# Example: Target 3, Coins [2] -> ValueError
try:
    coins_err1 = [2]
    target_err1 = 3
    print(f"Target {target_err1} with coins {coins_err1}: {find_fewest_coins(coins_err1, target_err1)}")
except ValueError as e:
    print(f"Error for target {target_err1} with coins {coins_err1}: {e}")

# Example: Negative target -> ValueError
try:
    coins_err2 = [1, 5]
    target_err2 = -5
    print(f"Target {target_err2} with coins {coins_err2}: {find_fewest_coins(coins_err2, target_err2)}")
except ValueError as e:
    print(f"Error for target {target_err2} with coins {coins_err2}: {e}")

# Example: Target 0, Coins [5] -> []
coins5 = [5]
target5 = 0
print(f"Target {target5} with coins {coins5}: {find_fewest_coins(coins5, target5)}")

