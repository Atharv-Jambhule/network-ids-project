import pandas as pd

df = pd.read_csv("traffic_dataset.csv")

threshold = 1500

suspicious = df[df["packet_length"] > threshold]

print("Suspicious packets detected:")

print(suspicious)