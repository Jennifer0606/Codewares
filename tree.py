import matplotlib.pyplot as plt
import squarify
import pandas as pd

my_dpi = 96
plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)

squarify.plot(sizes=[13, 22, 35, 5], label=["group A", "group B", "group C", "group D"],
              color=["red", "green", "blue", "grey"], alpha=.4)
plt.axis('off')
plt.show()
