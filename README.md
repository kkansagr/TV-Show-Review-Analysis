# TV-Show-Review-Analysis

Analysis of tweets for different TV Shows, compared with critics reviews from IMDb and Rotten Tomatoes to give an overall view of each show. Used Twitter API, web scraping, Naive Bayes classifier, and Python with Pandas, Bokeh, and NLTK. <br>
<br>
<b>Info:</b>
1) imdbrtoverall.py generates the rtv.csv files which contains the overall imdb and rotten tomatoes ratings of the selected TV shows.<br>
2) twitter.py generates the twitterdata.csv file which contains reviews of TV shows collected from twitter and their classification into positive and negative.<br>
3) seasonepiinfo.py generates the season.csv file which contains season-wise and episode-wise ratings of the selected TV show.<br>

These .csv files are pre-generated and are ready to use.<br><br>

<b>Running the Code </b><br>

The main.py file is the one that generates the visualization. To run this file,<br>
1) Make sure the bokeh package is installed on your device.<br>
2) Open the python terminal within your IDE. Ideally if using Jupyter Notebooks, goto New > Terminal.<br>
3) Set your path to the current folder where all the files and the main.py file is.<br>
4) Type the command "bokeh serve --show main.py" without the double quotes.<br>

The visualization will open up in a new browser window.<br><br>

![Overall ratings](Visualizations/Untitled.png)

![Season ratings](Visualizations/Untitled1.png)

![Episodic ratings](Visualizations/Untitled2.png)
