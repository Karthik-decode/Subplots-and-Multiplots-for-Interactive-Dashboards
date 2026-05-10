import squarify
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("ecommerce_customer_behavior_dataset.csv")

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# 1. Sales by Category
sns.barplot(data=df, x='Product_Category', y='Total_Amount', ax=axs[0,0])
axs[0,0].set_title("Sales by Category")

# 2. Payment Method Distribution
sns.countplot(data=df, x='Payment_Method', ax=axs[0,1])
axs[0,1].set_title("Payment Methods")

# 3. City Sales Trend
city_sales = df.groupby('City')['Total_Amount'].sum().reset_index()
axs[1,0].bar(city_sales['City'], city_sales['Total_Amount'])
axs[1,0].set_title("Sales Trend")

# 4. Customer Ratings
sns.countplot(data=df, x='Customer_Rating', ax=axs[1,1])
axs[1,1].set_title("Customer Ratings")

plt.tight_layout()
plt.show()

# Interactive Bar Chart
fig = px.bar(df,
             x='Product_Category',
             y='Total_Amount',
             color='Payment_Method',
             title="Interactive Sales by Category")

fig.show()

# Interactive Treemap
fig = px.treemap(df,
                 path=['Product_Category', 'Payment_Method'],
                 values='Total_Amount',
                 title="Interactive Treemap")

fig.show()

#scatter plot
sns.scatterplot(data=df,
                x='Session_Duration_Minutes',
                y='Total_Amount',
                hue='Device_Type')

plt.title("User Behavior vs Spending")
plt.show()