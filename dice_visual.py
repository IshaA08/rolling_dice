from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6
die = Die()

# Make some rolls and store the values
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x = x_values, y = frequencies)]

# Configure the axes
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
    title='Results of Rolling One D6 1000 Times',
    xaxis = x_axis_config,
    yaxis = y_axis_config
)

offline.plot(
    {'data': data, 'layout':my_layout},
    filename='d6.html'
)