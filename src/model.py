import csv
import tensorflow as tf
from sklearn.model_selection import train_test_split

with open("data/Dataset.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({

        })