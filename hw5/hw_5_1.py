#!/usr/bin/env python
# coding: utf-8


import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

from sklearn.svm import SVC

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score

random_state = 42

class Builder:
    def __init__(self, X_train: np.ndarray, y_train: np.ndarray):
        self.X_train = X_train
        self.y_train = y_train

    def get_sample(self, df_share: int):
        """
        1. Copy train dataset
        2. Shuffle data (don't miss the connection between X_train and y_train)
        3. Return df_share %-subsample of X_train and y_train
        """
        X = self.X_train.copy()
        y = self.y_train.copy()

        X, y = shuffle(X, y, random_state=random_state)

        num = int(len(y) * df_share / 100.0)

        return X[:num, :], y[:num]

if __name__ == "__main__":

    """
    1. Load iris dataset
    2. Shuffle data and divide into train / test.
    """
    train_size = 0.7

    X, y = load_iris(return_X_y=True)
    X, y = shuffle(X, y, random_state=random_state)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size, random_state=random_state)

    # print(f"Train size = {len(y_train)}, Test size = {len(y_test)}")

    clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))

    pattern_item = Builder(X_train, y_train)
    for df_share in range(10, 101, 10):
        curr_X_train, curr_y_train = pattern_item.get_sample(df_share)

        clf.fit(curr_X_train, curr_y_train)

        y_pred = clf.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)

        print(f"df_share = {df_share}%, accuracy = {accuracy}")

    """
    1. Preprocess curr_X_train, curr_y_train in the way you want
    2. Train Linear Regression on the subsample
    3. Save or print the score to check how df_share affects the quality
    """



