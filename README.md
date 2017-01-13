# Summary

this repository is a short explanatory analysis of the data of the passengers of the titanic, it's aim is to show how people
normally react when facing a catastrophy, to do so I created three visualisations of the variables I found more interesting,
using Dimple.js and D3.js

# Design

To better represent my point of view I choosed to plot bar charts based on different variables:

1- a bar plot for the Survivors by passenger's class and by Sex, this way the reader can see the total number of survivors
on each class and it's proportion based on Sex

2- a bar plot for the deads by passenger's class and by sex, the difference in the first plot between classes and Sex wasn't 
too important, this plot comes to strengthen the assumption of the difference between those variables

3- a bar plot of the Survivors and deads by ranges of Age, after doing some data wrangling using python and pandas I generated 
the 2 csv files that I plotted, this one is to show that the old people had less chances of surviving and that young children were
more likely to be rescued

# Feedback

after showing the first sketches of the plots to my colleagues, They pointed out the misleading of the colors and advised the use
of blue for male and Red for female.

the other point corrected based on the feedback is on the last plot, I was at first plotting age in a raw format without grouping 
it by ranges and thus having a lot of unwanted values like 0.75 and so on.

# Ressources

The data comes from the Kaggle website : https://www.kaggle.com/c/titanic
Dimple.js : http://dimplejs.org/
D3.js : https://d3js.org/
StackOverflow : http://stackoverflow.com/
