import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("ecommerce_customer_behavior_dataset.csv")

# Convert date
df['Date'] = pd.to_datetime(df['Date'])

# Create Month column
df['Month'] = df['Date'].dt.to_period('M').astype(str)

monthly = df.groupby('Month').agg({
    'Total_Amount': 'sum',
    'Order_ID': 'count',
    'Delivery_Time_Days': 'mean'
}).reset_index()

fig, ax = plt.subplots(3, 1, figsize=(10, 8))

# Sales
ax[0].plot(monthly['Month'], monthly['Total_Amount'])
ax[0].set_title("Monthly Sales")

# Orders
ax[1].plot(monthly['Month'], monthly['Order_ID'])
ax[1].set_title("Number of Orders")

# Delivery Time
ax[2].plot(monthly['Month'], monthly['Delivery_Time_Days'])
ax[2].set_title("Avg Delivery Time")

plt.tight_layout()
plt.show()