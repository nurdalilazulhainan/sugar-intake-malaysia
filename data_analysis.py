# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample DataFrame for sugar intake by age group
data = pd.DataFrame({
    'age_group': ['0-18', '19-35', '36-50', '51+'],
    'sugar_intake': [30, 50, 40, 20]  # Sample average sugar intake in grams
})

# Display the data
print(data)

# Create a bar plot for sugar intake by age group
plt.figure(figsize=(10, 6))
sns.barplot(x='age_group', y='sugar_intake', data=data, ci=None)
plt.title('Average Sugar Intake by Age Group in Malaysia')
plt.xlabel('Age Group')
plt.ylabel('Average Sugar Intake (grams)')
plt.show()
