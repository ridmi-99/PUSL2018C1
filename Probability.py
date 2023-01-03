import random

def simulate():
    # Generate a list of three random integers, where 0 represents a boy and 1 represents a girl
    genders = [random.randint(0, 1) for _ in range(3)]
    
    # Check if at least one child is a girl and all three are girls
    at_least_one_girl = 1 in genders
    all_girls = genders == [1, 1, 1]
    return at_least_one_girl and all_girls

# Run the simulation 1000 times and count the number of times that at least one child is a girl and all three are girls
num_successes = 0
num_trials = 1000
for _ in range(num_trials):
    if simulate():
        num_successes += 1

# Calculate the probability and print the result
probability = num_successes / num_trials
print(f'Probability: {probability}')