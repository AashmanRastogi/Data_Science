#dependencies
import numpy as np 
from matplotlib import pyplot

plot_every = 100 # plotting after every set number of iterations

def distance(x1,y1,x2,y2):
    return np.sqrt((y2-y1)**2 + (x2-x1)**2)

# initial conditions 
def main():
    tau = 0.53  # kinematic viscocity 
    Nx = 400    # points about x axis
    Ny = 100    # points abvout y axis
    Nt = 10000  # number of iterations
    Nl = 9      # number of lattice points 

    
    # Lattice speeds and weights 

    """
    1/36  1/9  1/36       (-1,1)    (0,1)     (1,1)
     1/9  4/9  1/9   =    (-1,0)    (0,0)     (1,0)
    1/36  1/9  1/36       (-1,-1)   (0,-1)   (1,-1) 
     """

    cxs = np.array([0, 0, 1, 1, 1, 0,-1,-1,-1])         # x values of our discrete velocities
    cys = np.array([0, 1, 1, 0,-1,-1,-1, 0, 1])         # y values of our discrete velocities
    weights = np.array([4/9, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36])


    # defining our misoscopic vel => velocity in every cell in each one of nodes

    # 3rd dimension represents the velocities to be stored for each point
    F = np.ones([Ny, Nx, Nl]) + 0.01 * np.random.randn(Ny, Nx, Nl)  

    """
    We want our fluid to follow initialy to the right in each of the 3rd node of the lattice
    """

    F[:,:,3] = 2.3

    # Define the cylinder

    """
    creates an array mapping to every point in the lattice 
    where false implies empty space and if true that point represents an obstacle
    """
    cylinder = np.full((Ny, Nx),False)

    for y in range(0, Ny):
        for x in range(0, Nx):
            if (distance(Nx//4, Ny//2, x, y) < 13):
                cylinder[y][x] = True

    # Main Loop 

    for it in range(Nt):
        print(it)

        """
        setting values at the very end of the right wall to the value right next to it 
        so that they cancel each other out
        """
        F[:,-1,[6, 7, 8]] = F[:,-2,[6 ,7, 8]] 
        F[:,0,[2, 3, 4]] = F[:,1,[2 ,3, 4]]

        """
        setting our streaming velocity where each point will pass on its velocity to its neighbour 
        in the direction of its discrete velocity
        """

        for i, cx, cy in zip(range(Nl), cxs, cys):
            F[:, :, i] = np.roll(F[:, :, i], cx, axis = 1)
            F[:, :, i] = np.roll(F[:, :, i], cy, axis = 0)

        # Caluclating collisons with the cylinder

        """
        getting all the points where velocity is inside our cylinder and inverting the velocity at each of these points
        """
        boundry = F[cylinder, :]
        boundry = boundry[:, [0, 5, 6, 7, 8, 1, 2, 3, 4]]

        # Calculating fluid variables
        rho = np.sum(F, 2)            # Density , axis = 2 implies 3rd dimension 
        ux = np.sum(F * cxs, 2)/rho   # Momentum 
        uy = np.sum(F * cys, 2)/rho   # Momentum

        # applying boundry on cylinder  

        """
        setting all lattice cells and velocities within the cylinder to teh opposites we have calculated
        """
        F[cylinder, :] = boundry
        ux[cylinder] = 0   # all macroscopic velocities withing the cylinder are 0 
        uy[cylinder] = 0   # all macroscopic velocities withing the cylinder are 0

        # Collision 
        
        """
        Calculating thes F equilibrium 
        """  

        Feq = np.zeros(F.shape)
        for i , cx, cy, w in zip(range(Nl), cxs, cys, weights):
            Feq[:, :, i] = rho * w * (
                1 + 3 * (cx*ux + cy*uy) + 9 * (cx*ux + cy*uy)**2 / 2 - 3 * (ux**2 + uy**2)/2
            ) 

        F = F + -(1/tau) * (F - Feq)

        if (it%plot_every == 0):
            '''dfydx = ux[2:, 1:-1] - ux[0:-2, 1:-1]
            dfxdy = uy[1:-1, 2:] - uy[1:-1, 0:-2]
            curl = dfydx - dfxdy
            pyplot.imshow(curl,cmap = "plasma")'''
            pyplot.imshow(np.sqrt(ux**2 + uy**2)) # magnitude of momentum
            pyplot.pause(0.01)                     # giving sometime to view the graph
            pyplot.cla()                           # clearing it afterwards 


if __name__ == "__main__":
    main()
