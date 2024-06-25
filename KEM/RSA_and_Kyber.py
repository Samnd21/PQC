import time
import matplotlib.pyplot as plt
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from kyber import Kyber512, Kyber768, Kyber1024


# RSA Key Generation
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048  # Adjust the key size as needed
    )
    public_key = private_key.public_key()
    return private_key, public_key

# ML-KEM Key Generation (Using Kyber as an example)
def generate_mlkem_keys(kyber_class):
    public_key, secret_key = kyber_class.keygen()
    return secret_key,public_key

# Measure key generation time and size
def measure_key_generation(algorithm_name, generate_keys_func, *args):
    start_time = time.time()
    keys = generate_keys_func(*args)
    end_time = time.time()
    if algorithm_name == "RSA":
        private_key_pem = keys[0].private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_key_pem = keys[1].public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        key_sizes = [len(private_key_pem), len(public_key_pem)]
    else:
        key_sizes = [len(key) for key in keys]
    generation_time = end_time - start_time
    return key_sizes, generation_time

# Measure RSA key sizes and generation time
rsa_key_sizes, rsa_gen_time = measure_key_generation("RSA", generate_rsa_keys)

# Measure Kyber key sizes and generation times
kyber512_key_sizes, kyber512_gen_time = measure_key_generation("Kyber512", generate_mlkem_keys, Kyber512)
kyber768_key_sizes, kyber768_gen_time = measure_key_generation("Kyber768", generate_mlkem_keys, Kyber768)
kyber1024_key_sizes, kyber1024_gen_time = measure_key_generation("Kyber1024", generate_mlkem_keys, Kyber1024)

# Visualization of key sizes
key_sizes = {
    "RSA": rsa_key_sizes,
    "Kyber512": kyber512_key_sizes,
    "Kyber768": kyber768_key_sizes,
    "Kyber1024": kyber1024_key_sizes
}

key_gen_times = {
    "RSA": rsa_gen_time,
    "Kyber512": kyber512_gen_time,
    "Kyber768": kyber768_gen_time,
    "Kyber1024": kyber1024_gen_time
}

# Plot key sizes
labels = list(key_sizes.keys())
private_sizes = [sizes[0] for sizes in key_sizes.values()]
public_sizes = [sizes[1] for sizes in key_sizes.values()]

x = range(len(labels))

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(x, private_sizes, width=0.4, label='Private Key Size', color='b', align='center')
plt.bar(x, public_sizes, width=0.4, label='Public Key Size', color='r', align='edge')
plt.xlabel('Algorithm')
plt.ylabel('Key Size (bytes)')
plt.title('Key Sizes of RSA and Kyber Variants')
plt.xticks(x, labels)
plt.legend()

# Plot key generation times
gen_times = list(key_gen_times.values())

plt.subplot(1, 2, 2)
plt.bar(x, gen_times, width=0.6, color='g')
plt.xlabel('Algorithm')
plt.ylabel('Generation Time (seconds)')
plt.title('Key Generation Times of RSA and Kyber Variants')
plt.xticks(x, labels)
plt.savefig("saved_image.jpg")
plt.tight_layout()
plt.show()
