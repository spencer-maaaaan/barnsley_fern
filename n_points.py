"""
auth spencer tenney
desc plots a barnsely fern with n points, then opens the plot for viewing
"""
import barnsley_generator
import matplotlib.pyplot as plt
from matplotlib import style

#setting n, the number of points to be calculated
n = 10000000

# setting dark style to save my eyes
style.use("dark_background")

# creating the plot
fig = plt.figure()
ax = fig.add_subplot()
X = []; Y = []

# planting fern
fern = barnsley_generator.Fern()

# plotting all the points
for i in range(1,n+1):
    x,y = next(fern)
    X.append(x)
    Y.append(y)

    #monitoring progress
    if i % 1000 == 0:
        print("plotting points: n = {0} {1:.1%}".format(i, i/n), end="\r")

# making and opening plot
print("\nopening plot...")

ax.scatter(X,Y, s=0.1, alpha=.2, c="green")
ax.annotate("n = "+str(len(X)), xy=(0.01,0.99), xycoords="axes fraction", ha="left", va="top")
plt.show()
