def normalize(data):
    _max = max(data)
    divide_by_max = lambda x: x / _max
    return list(map(divide_by_max, data))
