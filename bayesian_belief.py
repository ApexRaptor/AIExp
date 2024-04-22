# Define conditional probabilities
p_rain_true = 0.2
p_sprinkler_true_given_rain_true = 0.8
p_sprinkler_true_given_rain_false = 0.1

# Prompt user for input
rain_input = input("Is it raining? (yes/no): ")

# Convert user input to boolean value
is_raining = True if rain_input.lower() == "yes" else False

# Compute joint probabilities and marginal probabilities
if is_raining:
    p_rain = p_rain_true
    p_sprinkler_true_given_rain = p_sprinkler_true_given_rain_true
else:
    p_rain = 1 - p_rain_true
    p_sprinkler_true_given_rain = p_sprinkler_true_given_rain_false

p_sprinkler_true = p_rain * p_sprinkler_true_given_rain

# Compute conditional probability of Sprinkler=True given user input
p_sprinkler_true_given_input = p_sprinkler_true / p_rain
print("Probability of Sprinkler=True given the input:", p_sprinkler_true_given_input)
