import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker

times = []
download = []
upload = []

with open("internet_speed.csv", mode="r") as csvfile:
    plots = csv.reader(csvfile, delimiter=",")
    next(csvfile)   # Skip headers
    for row in plots:
        times.append(str(row[0]))
        download.append(float(row[1]))
        upload.append(float(row[2]))

print(times, "\n", download, "\n", upload)

#plt.figure(30, 30)
plt.plot(times, download, label="download", color="r")
plt.plot(times, upload, label="upload", color="b")
plt.xlabel("Time")
plt.ylabel("Speed in Mb/s")
plt.title("Internet Speed")
plt.legend()
#plt.savefig("Internet_Speed_Graph.jpg", bbox_inches="tight")
#plt.savefig("Internet_Speed_Graph.jpg")
plt.show()