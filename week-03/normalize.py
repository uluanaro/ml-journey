"""Нормализация и анализ табличных данных на чистом NumPy."""
import numpy as np


def zscore_normalize(X):
    """Z-нормализация: центрирует признаки в 0 и приводит std к 1."""
    means = X.mean(axis=0)
    stds = X.std(axis=0)
    return (X - means) / stds


def select_above_mean(X_norm, feature_idx):
    """Возвращает объекты, где признак feature_idx выше среднего (>0)."""
    mask = X_norm[:, feature_idx] > 0
    return X_norm[mask]


def predict(X, weights):
    """Линейное предсказание для каждого объекта: X @ weights."""
    return X @ weights


if __name__ == "__main__":
    X = np.array([[1.0,  50.0,  1000.0],
                  [2.0,  40.0,  3000.0],
                  [3.0,  60.0,  2000.0],
                  [4.0,  55.0,  5000.0],
                  [5.0,  45.0,  4000.0]])

    X_norm = zscore_normalize(X)
    print("Нормализованные данные:\n", X_norm)
    print("Среднее после:", X_norm.mean(axis=0))
    print("Std после:   ", X_norm.std(axis=0))

    selected = select_above_mean(X_norm, 0)
    print("Объекты с признаком 0 выше среднего:\n", selected)

    w = np.array([0.5, 1.0, 2.0])
    print("Предсказания:", predict(X_norm, w))