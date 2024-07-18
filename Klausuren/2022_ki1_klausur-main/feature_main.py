from feature_generate import generate_in_order
from feature_compute import compute_feature, good_threshold

# Generate some examples
numberIs = 4
numberOs = numberIs
examples = generate_in_order(numberIs, numberOs, show=True)

# Compute features and classify
results = []
for ex in examples:
    feature = compute_feature(ex)
    if feature < good_threshold():
        results.append(1)
    else:
        results.append(0)

# Evaluate the result
errorIs = numberIs - sum(results[:numberIs])
errorOs = sum(results[numberIs:])
correctPercentage = (len(examples) - errorIs - errorOs) / len(examples) * 100
print("Correctly classified ", correctPercentage, "% of all examples with theshold ", good_threshold())
