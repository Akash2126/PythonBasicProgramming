
# A widely used libary for basic visualization.

#matplotlib
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]

# plt.plot(x, y, marker='o', label='Line Plot')
# plt.title('Simple Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()
# plt.show()

#seaborn- built on matplotlib it offers advanced aesthetically pleasing visualization.

# import seaborn as sns
# import matplotlib.pyplot as plt

# data = [8, 6, 9, 10, 6, 7, 8]
# sns.histplot(data, kde=True, color='blue')
# plt.title('Histogram with KDE')
# plt.show()

#plotly - interactive visualization libary for creating dynamics plots.


# import plotly.express as px

# data = {'City': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata'],
#         'Population': [30, 20, 15, 10]}
# fig = px.bar(data, x='City', y='Population', title='City Population')
# fig.show()

#pandas- Simple plotting directly from Pandas DataFrames.

# import pandas as pd
# import matplotlib.pyplot as plt

# data = {'Days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday'],
#         'Sales': [200, 220, 250, 300]}
# df = pd.DataFrame(data)

# df.plot(x='Days', y='Sales', kind='line', marker='o', title='Sales Over Days')
# plt.show()

#altair 

# import altair as alt
# import pandas as pd

# data = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': [10, 20, 30, 40]})
# chart = alt.Chart(data).mark_line().encode(x='X', y='Y', tooltip=['X', 'Y'])
# chart.show()

# line chart

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y, marker='o', label='Sales Trend')
plt.title('Line Chart Example')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.legend()
plt.show()




