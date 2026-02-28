import numpy as np
np.random.seed(42)

data=np.random.rand(100,3)
print(f"Origanl Data Shape:{data.shape}")

mean=np.mean(data,axis=0)
print(f"Mean Data Shape:{mean.shape}")

std=np.std(data,axis=0)

normalized=(data-mean)/std
total_rows =normalized.shape[0]
index=int(total_rows*0.8)
training_set=normalized[0:index,:]
print(f"Training Data Shape: {training_set.shape}")

testing_set=normalized[index:,:]
print(f"Testing Data Shape:{testing_set.shape}")

training_set[0,0]=99
print(f"Note:Modifying the Slice afftected the origanl array")