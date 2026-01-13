import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv("dataset.csv")

# Encode categorical data
le_proto = LabelEncoder()
le_flag = LabelEncoder()
df['protocol_type'] = le_proto.fit_transform(df['protocol_type'])
df['flag'] = le_flag.fit_transform(df['flag'])
df['label'] = df['label'].map({'normal':0, 'attack':1})

X = df.drop('label', axis=1)
y = df['label']

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save model and encoders
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(le_proto, open("proto.pkl", "wb"))
pickle.dump(le_flag, open("flag.pkl", "wb"))

print("✅ Model Trained Successfully")
