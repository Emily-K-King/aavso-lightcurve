# Using edited csv file 

#import pandas as pd
#import matplotlib.pyplot as plt
import scipy.fftpack as fft
import numpy as np

# Read the csv file
data = pd.read_csv("star_data_edited.csv")

# Extract columns
jd = data["JD"]
magnitude = data["Magnitude"].astype(float)

# Perform Fourier Transform
# Convert magnitude to numpy array
mag = magnitude.to_numpy()
mag_fft = fft.fft(mag)
frequencies = fft.fftfreq(len(mag), jd[1] - jd[0])


# Create plot of the light curve
plt.figure(figsize=(10, 6))

plt.scatter(jd, magnitude, s=10)

# Labels

plt.xlabel("Julian Date")
plt.ylabel("Magnitude")
plt.title("Light Curve")
plt.gca().invert_yaxis()
plt.grid(True)
plt.savefig("Star_data_editedcsv.png")
#plt.show()


# Create plot of the Fourier Transform
plt.figure(figsize=(10, 6))
pos = frequencies >= 0
plt.plot(frequencies[pos], np.abs(mag_fft[pos]))
plt.xlabel("Frequency")
plt.ylabel("Power")
plt.title("Fourier Transform")
plt.grid(True)
plt.savefig("Fourier_Transform.png")
