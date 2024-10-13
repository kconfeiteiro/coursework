import matplotlib.pyplot as plt

def plotsol(u, xmin, xmax, ymin, ymax, first=False):
    """Plot the solution u(x,y) at the current time step."""
    plt.clf()
    plt.imshow(
        u, extent=[xmin, xmax, ymin, ymax], origin='lower', cmap='hot', interpolation='nearest'
    )
    plt.colorbar()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Heat distribution')
    if first:
        plt.ion()
        plt.show()
    else:
        plt.draw()
        plt.pause(0.001)
