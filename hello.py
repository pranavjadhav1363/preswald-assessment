from preswald import connect, get_df
from preswald import query
from preswald import table, text
from preswald import plotly
import plotly.express as px
connect()  # Initialize connection to preswald.toml data sources
df = get_df("data/weather.csv")  # Load data
print(df)



sql = "SELECT * FROM data/weather.csv WHERE  CAST(wind AS DOUBLE) > 2"
filtered_df = query(sql, "data/weather.csv")

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")


fig = px.scatter(df, x="precipitation", y="temp_min", color="weather")
plotly(fig)