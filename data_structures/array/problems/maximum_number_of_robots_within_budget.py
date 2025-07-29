from collections import deque

class Solution:
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        L = 0  # left end of the sliding window
        max_charge = deque()  # stores indices of chargeTimes in decreasing order
        max_k = 0  # tracks the max window size within budget
        window_cost = 0  # running sum of runningCosts within the window

        for R in range(len(chargeTimes)):
            # Maintain deque: remove all smaller chargeTimes from the back
            while max_charge and chargeTimes[R] > chargeTimes[max_charge[-1]]:
                max_charge.pop()
            max_charge.append(R)

            # Add current running cost to the window total
            window_cost += runningCosts[R]

            # Shrink window from the left if total cost exceeds budget
            while chargeTimes[max_charge[0]] + (R - L + 1) * window_cost > budget:
                # Remove leftmost index from deque if it's leaving the window
                if max_charge[0] == L:
                    max_charge.popleft()
                window_cost -= runningCosts[L]
                L += 1

            # Update max window size if current window is valid
            max_k = max(max_k, R - L + 1)

        return max_k

