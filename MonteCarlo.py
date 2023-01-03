import random

# Number of simulations
n = 500

# Lists to store the durations for each activity and the total duration
durations_a = []
durations_b = []
durations_c = []
durations_total = []

# Loop over the number of simulations
for i in range(n):
    # Sample from the triangular distribution for each activity
    duration_a = random.triangular(8, 10, 12)
    duration_b = random.triangular(10, 12, 14)
    duration_c = random.triangular(12, 14, 16)
    
    # Add the durations to get the total duration
    duration_total = duration_a + duration_b + duration_c
    
    # Store the durations in the lists
    durations_a.append(duration_a)
    durations_b.append(duration_b)
    durations_c.append(duration_c)
    durations_total.append(duration_total)

# Compute the frequency of each duration range
range_30_35 = len([d for d in durations_total if d >= 30 and d < 35])
range_36_38 = len([d for d in durations_total if d >= 36 and d < 38])
range_39_42 = len([d for d in durations_total if d >= 39 and d <= 42])

# Compute the likelihood of completion for each range
likelihood_30_35 = range_30_35 / n
likelihood_36_38 = range_36_38 / n
likelihood_39_42 = range_39_42 / n

# Print the results in the form of a table
print("Duration (in days) \t Likelihood of Completion")
print("30 - 35 \t\t\t {:.2f}".format(likelihood_30_35))
print("36 - 38 \t\t\t {:.2f}".format(likelihood_36_38))
print("39 - 42 \t\t\t {:.2f}".format(likelihood_39_42))