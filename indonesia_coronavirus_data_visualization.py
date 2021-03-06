# -*- coding: utf-8 -*-
"""Indonesia Coronavirus Data Visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1roMShRNRiIKIkH9L0FSmXDiWB0Qznzlk
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

!wget https://raw.githubusercontent.com/rizkarifda/Data-Analysis-Using-Python-Programming/master/covid_19_indonesia_time_series_all.csv

indo_corona_data = pd.read_csv('covid_19_indonesia_time_series_all.csv')

indo_corona_data

jatim = indo_corona_data[indo_corona_data['Province']=='Jawa Timur']
jatim

jatim = indo_corona_data[indo_corona_data['Province']=='Jawa Timur']
fig,ax = plt.subplots(figsize=(18,8))
sns.lineplot(x="Date",
             y = "New Cases",
             data = jatim,
             palette = "bright")



jatim1 = jatim.tail(14)

fig,ax = plt.subplots(figsize=(25,7))
sns.lineplot(x="Date",
             y = "New Cases",
             data = jatim1,
             palette = "bright")

indo_corona_data = pd.read_csv('covid_19_indonesia_time_series_all.csv').sort_values("Total Cases", ascending=False)
indo_corona_data.head()

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

# Plot the total crashes
sns.set_color_codes("pastel")
sns.barplot(x="Total Cases", y="Province", data=indo_corona_data,
            label="Total Cases", color="b")

# Plot the crashes where alcohol was involved
sns.set_color_codes('muted')
sns.barplot(x="Total Deaths", y="Province", data=indo_corona_data,
            label="Total Deaths", color="b")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 7600), ylabel="",
       xlabel="Which province have suffered the most total deaths?")
sns.despine(left=True, bottom=True)

fig,ax = plt.subplots(figsize=(20,10))
sns.lineplot(x="Date",
             y = "Total Cases",
             data = indo_corona_data,
             palette = "bright",
             hue = "Province")

fig,ax = plt.subplots(figsize=(20,10))
sns.lineplot(x="Date",
             y = "Total Deaths",
             data = indo_corona_data,
             palette = "bright",
             hue = "Province")

fig,ax = plt.subplots(figsize=(20,10))
sns.lineplot(x="Date",
             y = "New Cases",
             data = indo_corona_data,
             palette = "bright",
             hue = "Province")









































































































