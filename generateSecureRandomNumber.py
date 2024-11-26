import secrets
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode

random_byte_size = 2048

random_bytes = secrets.token_bytes(random_byte_size)

array = np.frombuffer(random_bytes, dtype=np.uint8)

mean_val = np.mean(array)
std_dev = np.std(array)
median_val = np.median(array)
mode_val, mode_count = mode(array)
min_val = np.min(array)
max_val = np.max(array)

print("Array Statistics:")
print(f"- Mean: {mean_val:.2f}")
print(f"- Standard Deviation: {std_dev:.2f}")
print(f"- Median: {median_val:.2f}")
print(f"- Mode: {mode_val.mode[0]} (appears {mode_count[0]} times)")
print(f"- Minimum Value: {min_val}")
print(f"- Maximum Value: {max_val}")

output_file = "random_data_python.bin"
array.tofile(output_file)
print(f"Random data written to '{output_file}' successfully!")

plt.figure(figsize=(10, 5))
plt.hist(array, bins=50, color='blue', alpha=0.7)
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
