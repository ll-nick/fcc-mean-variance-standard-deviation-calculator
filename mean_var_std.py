import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(list).reshape(3, 3)

    calculations = {
        "mean": mean(arr),
        "variance": variance(arr),
        "standard deviation": standard_deviation(arr),
        "max": max(arr),
        "min": min(arr),
        "sum": sum(arr)
    }
    
    return calculations

def mean(arr):
    return compute_metric(arr, np.mean)

def variance(arr):
    return compute_metric(arr, np.var)

def standard_deviation(arr):
    return compute_metric(arr, np.std)

def max(arr):
    return compute_metric(arr, np.max)

def min(arr):
    return compute_metric(arr, np.min)

def sum(arr):
    return compute_metric(arr, np.sum)
    
def compute_metric(arr, metric):    
    return [metric(arr, axis=0).tolist(), metric(arr, axis=1).tolist(), metric(arr)]