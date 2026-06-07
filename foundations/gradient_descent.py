class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        for _ in range(iterations):
            init = init - learning_rate * (2*init)

        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        return round(init, 5)
