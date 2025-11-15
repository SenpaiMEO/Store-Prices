import matplotlib.pyplot as plt

Days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
Temperatures = [24, 26, 25, 23, 27, 28, 25] 

plt.figure(figsize=(10, 6))
plt.plot(Days, Temperatures, marker='o', color='black')

plt.title("Temperature Over a Week")
plt.xlabel("Day of the Week")
plt.ylabel("Temperature")

plt.show()