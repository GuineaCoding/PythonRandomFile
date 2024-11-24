import secrets
import numpy as np

random_bytes = secrets.token_bytes(2048)
array = np.frombuffer(random_bytes, dtype=np.uint8)
print("Array mean:", np.mean(array))
array.tofile("random_data_python.bin")