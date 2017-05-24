# Physics 91SI
# Spring 2017
# Lab 8
#!/anaconda/bin/python
import numpy as np

class Particle:
    """Stores information about a particle with mass, position, and velocity."""
    
    def __init__(self, Position, M):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.pos = Position   # Sets position
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,))
        self.acc = np.zeros((2,))
    
class Molecule:
    
    def __init__(self,p1,p2,k,L0):
        self.p1=p1
        self.p2=p2
        self.k=k
        self.Lo=L0

    def get_displ(self):
        return (self.p2.pos- self.p1.pos)
    
    def get_force(self):
        initialVector=(self.p2.pos[0]-self.p1.pos[0])**2 + (self.p2.pos[1]-self.p1.pos[1])**2
        initialDisplacement=np.sqrt(initialVector)
        displacement=self.Lo-initialDisplacement
        force=-self.k* displacement
        displ=self.get_displ()
        print(displ[0])
        return np.array([(force * displ[0]/initialDisplacement),(force *displ[1]/initialDisplacement)])

        
