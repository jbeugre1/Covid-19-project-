import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

covid = pd.read_csv('CDC Covid-19 Death Progression.csv')

plt.figure(figsize=(8, 5))
plt.title('CDC Covid-19 Death Progression')

plt.plot(covid['End Week'], covid['Total Deaths'], label='')
plt.plot(covid['End Week'], covid['COVID Deaths'], label='')

print(covid.Date[::15])

plt.xticks(covid.Date[::3])

plt.xlabel('Date')
plt.ylabel('COVID-19 Cases')

plt.legend()

plt.show()
