import matplotlib.pyplot as plt

class grid():
    def __init__(self, n):
        self.n = n

    def createGrid(self):    
        s = range(self.n + 1)

        plt.xticks(s)
        plt.yticks(s)

        plt.xlim([0, self.n + 1])
        plt.ylim([0, self.n + 1] )
        plt.grid(True)

        plt.plot()
        plt.savefig("grid.png")