# Data-Science
This repository contains projects that I have done in data science both academic and extra curricular

1) Markov Model of Natural Language

The project is based on the Markov Models of Natural Language which when seeded with a small amount of text, create a large corpus of text similar to the seed text. Here I use first 10 chapters of Jane Austins book "Emma" to create a much simpler language model to generate text. I create an nth - order Markov Model which generates a string of text one letter at a time based on the most recent n block of letters. The model then adds the last letter of the n+1 block of text based on its probability of occurrence in the entire text( first 10 chapters of Jane Austins book "Emma").

2) Page Rank 

This project is based on the page rank algorithm to rank individual elements in a complex system. Here I impliment a similar algorithm on the "Hamilton" dataset to count the number of time a user surfs over a webpage considering references between characters as links between webpages. Based on a set limit of iterations, calculated the page rank which is essentialy the frequency of reference of each link.

3) n-dimensional Random Walk

Implimented a d - dimensional random walk based on n number of steps. User randomly moves in any direction on each iteration. In 2D it moves along the x-y direction and in 3D we include the z axis as well. Visualized this random walk both in 2D and 3D.

4) Graphs and Time - series 

Plotted a time - series graph for COVID-19 cases and the DOW JONES Industrial Average index to see any possibel correlation in stock fluctuation due to Covid. Furthermore, in this project I learned to use matplotlib to plot histograms and scatter plots. Visulaize corelation between Happiness Score, GDP per capita and social suppprt in each country using a scatterplot matrix. 

5) Regression and plots

Learned how to use seaborn library to visualize gapminder data containing information about the socioeconomic global world which include detailed statistics on life expectancy, population, and GDP.Created scatter plots, bar plots and box plots to represent data and visualize correaltions present in it between different variables. Also got introduction to logistic regression which we used to figure out in an email was spam or not based on the modelled probability, 1 indicating spam and 0 otherwise.

6) Algorithmic Bias Detection

Performed data analysis to find the amount of artwork by Female artists that has increased overtime as a fraction of all art work in the Tate art museum. Furthered this analysis by also focuisng on indiviual art form and its represenattion. Following this I trained a linear regression model to test the cause of racial bias in the algorithm used to enroll people in "high -r isk care management" programs. Produced scatter plots for each recorded case that  effectively shows an inherant bias in the algorithm which leads to white patients being reffered to high risk - care management programs more as compared to their black counterparts. This disparity is present for both males and females in respective races. The sourse of disparity was represented by the difference in costs of both races. White people have a higher spending on medical costs anualy and therefore get referred more to such programms.

7) Penguin Species Prediction 

Working in a team of 3, performed predictive analysis of penguin species in Antarctica. Independently performed data cleaning and feature slection to determine the set of variables higly predictive of a penguin's species. Performed exploratory analysis, offering summary statistics and visualizations about the relationships between chosen variables. Finally trained a multinomial logistic regression model with 97% accuracy to predict penguin species and visualized its decision region along with a confusion matrix. 

8) Algorithmic trading project 

Created a python script that will accept the value of your portfolio and determine the number of stocks that can be bought for each constituent of the S&P 500 index fund for an equal weight version of the index. For this I used IEX cloud API token and performed batch API calls to extract relevant data and customized the data into excel files using xlsxwriter library in python for better visualization. 

9) Lattice Boltzmann Fluid Simulation

Created a python script to simulate the lattice Boltzmann method for fluid flow using navier stokes equation. Used numpy and matplotlib to generate the same using help from online resources.
