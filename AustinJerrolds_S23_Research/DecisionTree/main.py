# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import metrics  # Import scikit-learn metrics module for accuracy calculation

from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

col_names = ['Total Time', 'Minus Jumps', 'Forward Jumps', 'Grade', 'Cheater']
# load dataset
pima = pd.read_csv("exams.csv", header=None, names=col_names)

print(pima)

pima.head()

# split dataset in features and target variable
feature_cols = ['Total Time', 'Minus Jumps', 'Forward Jumps', 'Grade']
X = pima[feature_cols]  # Features
y = pima.Cheater  # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # 70% training and 30% test

# Create Decision Tree classifier object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifier
clf = clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Precision score: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True, feature_names=feature_cols, class_names=['0', '1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('exams.png')
Image(graph.create_png())



