import numpy as np
import matplotlib.pyplot as plt

epoch=(np.arange(1,11 ))
loss=(np.linspace(0.90,0,10))
noise=np.random.normal(0,0.02,10)
loss+=noise

plt.figure(figsize=(5,5))
plt.plot(epoch, loss, marker="^")
plt.title("Line Plot")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

plt.figure(figsize=(5,5))
plt.scatter(epoch, loss)
plt.title("Scatter Plot")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

models=["Model A","Model B","Model C"]
error=[0.85,0.90,0.88]

plt.figure(figsize=(5,5))
plt.bar(models,error)
plt.title("Bar Plot")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.show()