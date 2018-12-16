# PUBG
PUBG: Team's Winning Placement Prediction

1) Download the training dataset from the given link
https://www.kaggle.com/c/pubg-finish-placement-prediction/data
Change the path of training dataset in dataset.py 
2) To install all the dependencies, type the following command in the terminal 
pip install -r requirements.txt
3) For training the model, type the following command in the terminal
Python pubg.py
This process will take time as the dataset is very large. 
The models are trained using Random Forest Algorithm.
Two models will be created for Squad and Duo teams. 
4) Launch the application by following command
python app.py
The server is running on http://127.0.0.1:5000/
Go to the link in the browser http://127.0.0.1:5000/
The website will redirect to the homepage after 5 seconds. 
5) Click on choose file.
Select an input file from verification data folder as per the numbers in the team, duo for 2 players, squad for 4 player and click Predict.
6) Repeat step 6 for different inputs. 
 
