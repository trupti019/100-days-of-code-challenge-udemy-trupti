import pandas as pd

data = pd.read_csv('Squirrel_data.csv')
fur_color_count= data['Primary Fur Color'].value_counts()

fur_color_count.to_csv('Fur_colour.csv', index=True, sep=',')


