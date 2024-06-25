import matplotlib.pyplot as plt

# Data for Crystal Dilithium types
types = [
    "test_dilithium2",
    "test_dilithium3",
    "test_dilithium5",
    "test_dilithium2aes",
    "test_dilithium3aes",
    "test_dilithium5aes"
]

# Key bytes data
crypto_publickeybytes = [
    1312, 1952, 2592,
    1312, 1952, 2592
]

# Secret key bytes data
crypto_secretkeybytes = [
    2528, 4000, 4864,
    2528, 4000, 4864
]

# Keypair generation time (median) data in cycles/ticks
median_keypair_cycles_ticks = [
    184350, 346528, 502629,
    384757, 346528, 704285
]

# Verify time (median) data in cycles/ticks
median_verify_cycles_ticks = [
    196811, 325857, 527466,
    361270, 325857, 642448
]

# Speed (median sign time) data in cycles/ticks
median_sign_cycles_ticks = [
    791914, 1307357, 1589822,
    1059054, 1307357, 1837116
]

# Plotting
plt.figure(figsize=(18, 12))

# Plot 1: Key bytes comparison
plt.subplot(2, 2, 1)
plt.bar(types, crypto_publickeybytes, color='skyblue', label='Public Key Bytes')
plt.bar(types, crypto_secretkeybytes, color='lightgreen', label='Secret Key Bytes', alpha=0.7)
plt.plot(types, crypto_publickeybytes, color='blue', marker='o', label='Trend: Public Key Bytes')
plt.plot(types, crypto_secretkeybytes, color='green', marker='o', label='Trend: Secret Key Bytes')
plt.title('Key Bytes Comparison')
plt.xlabel('Crystal Dilithium Types')
plt.ylabel('Bytes')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Plot 2: Keypair generation time comparison
plt.subplot(2, 2, 2)
plt.bar(types, median_keypair_cycles_ticks, color='salmon', label='Keypair Generation Time')
plt.plot(types, median_keypair_cycles_ticks, color='red', marker='o', label='Trend: Keypair Generation Time')
plt.title('Keypair Generation Time Comparison')
plt.xlabel('Crystal Dilithium Types')
plt.ylabel('Median Keypair Generation Time (cycles/ticks)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Plot 3: Verify time comparison
plt.subplot(2, 2, 3)
plt.bar(types, median_verify_cycles_ticks, color='lightblue', label='Verify Time')
plt.plot(types, median_verify_cycles_ticks, color='blue', marker='o', label='Trend: Verify Time')
plt.title('Verify Time Comparison')
plt.xlabel('Crystal Dilithium Types')
plt.ylabel('Median Verify Time (cycles/ticks)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Plot 4: Median sign time comparison
plt.subplot(2, 2, 4)
plt.bar(types, median_sign_cycles_ticks, color='lightgreen', label='Sign Time')
plt.plot(types, median_sign_cycles_ticks, color='green', marker='o', label='Trend: Sign Time')
plt.title('Median Sign Time Comparison')
plt.xlabel('Crystal Dilithium Types')
plt.ylabel('Median Sign Time (cycles/ticks)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.suptitle('Comparison of Crystal Dilithium Types', y=1.02, fontsize=16)
plt.savefig("dilithium.png")
plt.show()
