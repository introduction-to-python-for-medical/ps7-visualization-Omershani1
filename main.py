import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='wine', version=1, as_frame=True)

features = df.columns
selected_features = [features[1], features[2], features[7], features[9], features[10]]

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))
for ax, f in zip(axs, selected_features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)
  ax.set_ylabel(reference_feature)
  ax.set_title(f"{reference_feature} vs {f}")
else:
  ax.axis('off')
  plt.show()

reference_feature = selected_features[0]
comparison_feature = selected_features [4]
plt.figure(figsize=(8,6))
plt.scatter(df[reference_feature)
plt.ylabel(comparison)feature)
plt.savefig('correlation_plot.png')
plt.show()
