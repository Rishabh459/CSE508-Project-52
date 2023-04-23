# TweetPress - News Recommendation System

### CSE508 Project
### Group Number- 52
### Group Members - Kartik Jain, Manas Agarwal, Rishabh Oberoi, Uttkarsh Singh, Darsh Parikh

### Problem Statement-
Reading the news online has exploded as the web provides access to millions of news sources worldwide. The sheer volume of articles can be overwhelming to readers.
A key challenge of a news service website is to help users find news articles that match their interests. Personalised News Recommendation is advantageous to both users and the news service, as the user can quickly find what he or she needs, and this helps the news service retain and increase the customer base.
Twitter shows us trending news based on demographics and trends because of this it has become the main news source for many people. The problem with this type of recommendation is that the recommendations are not personalised to the user.
Another problem with current news platforms is that they tend to show polarised news articles which prevents people to know about the other side of the story as well before coming to any conclusion about something.

### Proposed Solution-
Creating a personalised news recommendation system that considers users' interests based on their tweets and recommends relevant articles. Most users use Twitter to get daily updates on what is happening, and our model helps them get personalised news articles that they might like or might be looking for. For the model, we consider different factors like keyword extraction, similarity matching and sentiment analysis. Based on all the above mentioned, we shortlist the list of relevant news articles for a user and show him the top ‘k’ relevant articles of both parities to produce a non-polarised result.

### Workflow of our Model-
We take TwitterID, Number of News articles (X), the Weighting Scheme and the Keyword Extraction Method from the user. After applying the models based on the weighting scheme mentioned by the user we give the output as top X articles. If the user has chosen a keyword extraction method then we use that specific method and sentiment analysis to retrieve X different news articles of both similar opinion as the user (according to the user's tweets) and X news articles of the opposite opinion.

*Workflow:*

<a href="images/images/workflow.jpg"><img src="https://github.com/Rishabh459/CSE508-Project-52/blob/main/images/images/workflow.jpg" align="center" height="300" width="400" ></a>


### How does TweetPress look like?
*Home Page:*

<a href="images/images/Home Screen.png"><img src="https://github.com/Rishabh459/CSE508-Project-52/blob/main/images/images/Home%20Screen.png" align="center" height="300" width="600" ></a>

*Search News Page:*

<a href="images/images/search_news_page.png"><img src="https://github.com/Rishabh459/CSE508-Project-52/blob/main/images/images/search_news_page.png" align="center" height="300" width="600" ></a>

### Sample Outputs-
*Sample Output 1:*

<a href="images/images/sample_output_1.png"><img src="https://github.com/Rishabh459/CSE508-Project-52/blob/main/images/images/sample_output_1.png" align="center" height="300" width="600" ></a>

*Sample Output 2:*

<a href="images/images/sample_output_2.png"><img src="https://github.com/Rishabh459/CSE508-Project-52/blob/main/images/images/sample_output_2.png" align="center" height="300" width="600" ></a>

*Sample Output 3:*

<a href="images/images/sample_output_3.png"><img src="https://github.com/Rishabh459/CSE508-Project-52/blob/main/images/images/sample_output_3.png" align="center" height="300" width="600" ></a>

-----
