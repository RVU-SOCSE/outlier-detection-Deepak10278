import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {'Price': [50000, 52000, 51000, 53000, 100000, 50500, 49500]}
df = pd.DataFrame(data)

# Matplotlib Box Plot
plt.figure()
plt.boxplot(df['Price'])
plt.title("Box Plot using Matplotlib")
plt.ylabel("Price")
plt.show()

# Seaborn Box Plot
plt.figure()
sns.boxplot(x=df['Price'])
plt.title("Box Plot using Seaborn")
plt.show()
