import numpy as np
feature_values=np.array([10,20,30,40])
print(f"Orignal Values:{feature_values}")

mean=np.mean(feature_values)
print(f"Mean:{mean}")

std=np.std(feature_values)
print(f"Standard Deviation:{std}")

normalized=(feature_values-mean)/std
print(f"Normalized Data:{normalized}")

reshaped=feature_values.reshape(2,2)
print(f"Reshaped Data Shape:{reshaped.shape}")