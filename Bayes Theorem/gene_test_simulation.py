# %%
import numpy as np
import seaborn as sns

# %%
# Parameters for the scenario
population = 1000000  # size of the population to simulate
prevalence = 0.02  # 2% of the population has the disease
sensitivity = 0.95  # true positive rate
specificity = 0.90  # true negative rate

# Simulating the population
# True for individuals with the disease, False for those without
disease = np.random.rand(population) < prevalence

# Simulating test results
# True for a positive test, False for a negative test
positive_test_given_disease = np.random.rand(population) < sensitivity
negative_test_given_no_disease = np.random.rand(population) < specificity

# True positive: disease and positive test
# False positive: no disease but positive test
positive_test = (disease & positive_test_given_disease) | (~disease & ~negative_test_given_no_disease)

# Calculating the probability of having the disease given a positive test result
probability_disease_given_positive_test = np.mean(disease[positive_test])

probability_disease_given_positive_test

# %%
unique, counts = np.unique(disease[positive_test], return_counts=True)
print(unique, counts)

# %%



