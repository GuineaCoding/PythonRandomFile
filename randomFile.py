import secrets
import numpy as np

random_byte_size = 2048

random_bytes = secrets.token_bytes(random_byte_size)

array = np.frombuffer(random_bytes, dtype=np.uint8)

print("Array Statistics:")
print(f"- Mean: {np.mean(array):.2f}")
print(f"- Standard Deviation: {np.std(array):.2f}")
print(f"- Median: {np.median(array):.2f}")

output_file = "random_data_python.bin"
array.tofile(output_file)
print(f"Random data written to '{output_file}' successfully!")