import numpy as np
np.random.seed(7)
readings = np.random.randint(20, 41, size=(6, 3))
print(readings)
mean = readings.mean(axis=0)
print("Mean per sensor:", mean)
std = readings.std(axis=0)
normalized = (readings - mean) / std
print("Normalized column means:", np.round(normalized.mean(axis=0), 10))
print("Hour of max per sensor:", readings.argmax(axis=0))
new_readings = np.vstack([readings, mean])
print(new_readings.shape)
np.random.seed(7)
new_data = np.random.randint(20, 41, size=(6, 3))
print("Reproducible:", np.array_equal(readings, new_data))

