# Restaurant-Success-Prediction-Data-Analysis-and-Model-Building

Zomato is an Online food ordering service, serving worldwide in which users can order food from the website or from mobile based applications. For this business problem, we are restricting only to the Bangalore region and Bangalore based restaurants. Dataset was created by extracting (web scraping) the information such as Approx. Price of food, Theme based restaurant or not, aggregate rating of each restaurant etc. about the existing established restaurants serving through Zomato and made available on Kaggle March 2019. The basic idea of analyzing the Zomato dataset is to get a fair idea about the factors affecting the establishment of different types of the restaurant at different places in Bangalore. While establishing a new restaurant some of the common questions such as • Location of the restaurant • Approx. Price of food etc. should be wisely answered to be successful in this industry. For the given historical data, to predict whether a new restaurant can be successful or not (positive or negative).

### Machine Learning Problem Formulation

The given problem can be solved either by binary classification problem (0 as failure or 1 as success), or Regression problem(for predicting scores) based on the given features.
• Approx. Price of food.
Theme based restaurant or not.
• Which locality of that city serves that cuisines with maximum number of restaurants.
The needs of people who are striving to get the best cuisine of the neighbourhood.
Is a particular neighbourhood famous for its own kind of food etc.
Here, the objective is to predict the success of a restaurant. Based on the prediction from the Model, a new investor can make the decision on whether to establish the restaurant or not.


### Performance Metric


Since we are solving this problem as a Binary classification task, where we need to predict whether a new restaurant will be successful of not, we will take classification metrics such as F1score/AUC into consideration.
