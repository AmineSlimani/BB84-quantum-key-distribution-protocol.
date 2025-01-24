import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

N_list = [10, 20, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800,  40, 80, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200,102400]
Bits_List = [0, 1]
Perror_list = []

def BB84(N):
    bits_a, bases_a = [], []
    bits_b, bases_b = [], []
    shifted_key = []
    for _ in range(N):
        bits_a.append(np.random.choice(Bits_List))
        bases_a.append(np.random.choice(Bits_List))
    for _ in range(N):
        bases_b.append(np.random.choice(Bits_List))
    for i in range(N):
        if bases_a[i] == bases_b[i]:
            bits_b.append(bits_a[i])
            shifted_key.append(bits_a[i])
        else:
            bits_b.append(1 - bits_a[i])
    Perror = 1 - (len(shifted_key) / N)
    Perror_list.append(Perror)
    print("-" * 50)

for N in N_list:
    BB84(N)
    print(f"BB84 started for N = {N}")

print(f"N = {N_list}")
print(f"Perror = {Perror_list}")

plt.figure(figsize=(8, 5))
sorted_data = sorted(zip(N_list, Perror_list), key=lambda x: x[0]) 
N_list_sorted, Perror_list_sorted = zip(*sorted_data)
plt.plot(N_list_sorted, Perror_list_sorted, marker='o', linestyle='-', color='b', label='$P_{\\text{error}}$')
plt.axhline(y=0.5, color='r', linestyle='--', label='Theoretical $P_{\\text{error}}$')
plt.xlabel('length of random String ($N$)')
plt.ylabel('Error Probability ($P_{\\text{error}}$)')
plt.title('Error Probability vs length of random String')
plt.grid(True)
plt.legend()
plt.show()