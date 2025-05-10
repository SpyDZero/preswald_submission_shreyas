import pandas as pd
import plotly.express as px

df = pd.read_csv('data/sample.csv')
fig = px.scatter(df, x='quantity', y='value', text='item',
                 title='Quantity vs. Value',
                 labels={'quantity': 'Quantity', 'value': 'Value'})

fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
fig.update_layout(template='plotly_white')

# Displays
import preswald

preswald.text("# Lets understand carbon emissions!🌎")
preswald.text("This is Shreyas's first app. 🎉")
preswald.text("Email: sdarade.andrew.cmu.edu")
# preswald.plotly(fig)
# preswald.table(df)

preswald.text("The average person in the U.S. emits over 16 metric tons of CO₂ per year, more than 4 times the global average. Yet, most people have no clear idea which of their daily choices matter most.")

preswald.text("If just 10% of people reduced their emissions by 1 metric ton per year through smarter travel, energy use, or diet, that alone could save over 330 million metric tons of CO₂ globally every year. That’s equivalent to taking 70 million cars off the road. **Amazing right?!**")

from preswald import connect, get_df

connect()  # Initialize connection to preswald.toml data sources
df = get_df("data/CarbonEmission.csv")  # Load data
preswald.text("## This is our table (Understanding our data):")
preswald.text("Our dataset consists of 10,000 rows and 15+ features (including the target variable), covering a wide range of behavioral and lifestyle attributes that influence an individual’s carbon footprint.")
preswald.table(df)

from preswald import query
preswald.text("Test Filtered the data to Male")
sql = "SELECT * FROM data/CarbonEmission.csv WHERE Sex = 'male'"
filtered_df = query(sql, "data/CarbonEmission.csv")
preswald.table(filtered_df)

preswald.text("Filtered the data to Carbon Emssion > 1000")
sql2 = "SELECT * FROM data/CarbonEmission.csv WHERE CarbonEmission > '1000'"
filtered_df2 = query(sql2, "data/CarbonEmission.csv")
preswald.table(filtered_df2)

from preswald import plotly
import plotly.express as px

preswald.text("Box plot")
# fig = px.scatter(df, x="transport", y="carbonemission", color="vehicletype")
# plotly(fig)
fig = px.box(df, x="Transport", y="CarbonEmission", color="Vehicle Type")
fig.show()
preswald.plotly(fig)

preswald.text("Bar plot")
fig2 = px.bar(df, x="Transport", y="CarbonEmission", color="Vehicle Type")
fig2.show()
preswald.plotly(fig2)

preswald.text("Due to time constraint of the assessment was able to reach this far only, happy to deep dive into something more meaningful with the data!")
