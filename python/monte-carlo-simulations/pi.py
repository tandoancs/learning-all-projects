import math
import random


def estimate_pi(num_samples):

    inside_circle = 0

    for _ in range(num_samples):

        x = random.uniform(-1, 1)

        y = random.uniform(-1, 1)

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:

            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4

    return pi_estimate


# Run the simulation with 1,000,000 samples

num_samples = 1000000

pi_estimate = estimate_pi(num_samples)

print(f"Estimated value of Pi: {pi_estimate}")
