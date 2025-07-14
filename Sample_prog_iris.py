import h2o
from h2o.frame import H2OFrame
from h2o.estimators import H2ORandomForestEstimator

# Connect to the H2O cluster
h2o.init(ip="172.20.252.53", port=54323)

# Check if both nodes are in the cluster
print(h2o.cluster_status())

# Load a small dataset (Iris dataset)
df = h2o.import_file("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Convert target column to categorical
df["species"] = df["species"].asfactor()

# Split into train and test sets
train, test = df.split_frame(ratios=[0.8], seed=1234)

# Define a Random Forest model
rf_model = H2ORandomForestEstimator(ntrees=50, max_depth=10, nfolds=5)

# Train the model
rf_model.train(x=df.columns[:-1], y="species", training_frame=train)

# Evaluate performance
performance = rf_model.model_performance(test_data=test)
print(performance)

h2o.cluster().shutdown()



