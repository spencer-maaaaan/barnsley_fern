"""
auth spencer tenney
desc plots a barnsley fern in matplotlib in real time
"""
import barnsley_generator
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# setting dark style to save my eyes
style.use("dark_background")

# setting points rendered for each frame of the animation
# lower values increase time resolution but it will take longer to render a more complete fern
points_per_frame = 1000

# making plot
fig = plt.figure()
ax = fig.add_subplot()
X = []; Y = []

# planting fern
fern = barnsley_generator.Fern()

# defining animation
def animate(i):
    for j in range(points_per_frame):
        x,y = next(fern)
        X.append(x)
        Y.append(y)

    ax.clear()
    ax.scatter(X,Y, s=0.01, c="green")
    ax.annotate("n = "+str(len(X)), xy=(0.01,0.99), xycoords="axes fraction", ha="left", va="top")

# bringing the plot to life
anim = animation.FuncAnimation(fig, animate, interval=0)
plt.show()
