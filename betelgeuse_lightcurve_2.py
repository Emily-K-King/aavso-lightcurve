# Using edited csv file 
import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file
data = pd.read_csv("star_data_edited.csv")

# Extract columns
jd = data["JD"]
magnitude = data["Magnitude"].astype(float)

# Create plot
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
