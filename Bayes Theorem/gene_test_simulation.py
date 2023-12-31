# %% Imports
import numpy as np
import seaborn as sns

# %% Setting variables for scenario parameters
population = 1000000  # size of the population to simulate
prevalence = 0.02  # 2% of the population has the gene
sensitivity = 0.95  # true positive rate
specificity = 0.90  # true negative rate

# %% Simulating the population
# True for individuals with the gene, False for those without
gene = np.random.rand(population) < prevalence

# %% Simulating test results
# True for a positive test, False for a negative test
positive_test_given_gene = np.random.rand(population) < sensitivity
negative_test_given_no_gene = np.random.rand(population) < specificity

# True positive: gene and positive test
# False positive: no gene but positive test
positive_test = (gene & positive_test_given_gene) | (
    ~gene & ~negative_test_given_no_gene
)

# %% Final probability
# Calculating the probability of having the gene given a positive test result
probability_gene_given_positive_test = np.mean(gene[positive_test])

print(f"Probability of having the gene, given a positive test: {probability_gene_given_positive_test}")
