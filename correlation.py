from __future__ import division

def dot(v1, v2):
    return sum(v1_i * v2_i for v1_i, v2_i in zip(v1, v2))

def mean(x):
    return sum(x) / len(x)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def sum_of_squares(v):
    return dot(v, v)

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    import math
    return math.sqrt(variance(x))

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0
    
def rank_simple(vector):
    return sorted(range(len(vector)), key=vector.__getitem__)

def rank(v):
    v_i = list(range(len(v)))
    v_i.sort(key=lambda x: v[x])
    result = [0] * len(v_i)
    for i, v_i in enumerate(v_i):
        result[v_i] = i
    return result

def ranked_correlation(x, y):
    ranked_x = rank(x)
    ranked_y = rank(y)
    return correlation(ranked_x, ranked_y)
    
juice_popularity = [10, 9.8, 8, 7.8, 7.7, 7, 6, 5, 4, 2]
juice_price = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]
print correlation(juice_popularity, juice_price)
print ranked_correlation(juice_popularity, juice_price)
