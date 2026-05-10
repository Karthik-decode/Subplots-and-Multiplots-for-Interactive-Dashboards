import squarify
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("ecommerce_customer_behavior_dataset.csv")

cat_data = df.groupby('Product_Category')['Total_Amount'].sum().reset_index()

plt.figure(figsize=(10,6))
squarify.plot(
    sizes=cat_data['Total_Amount'],
    label=cat_data['Product_Category'],
    alpha=0.8
)

plt.title("Sales by Product Category (Treemap)")
plt.axis('off')
plt.show()