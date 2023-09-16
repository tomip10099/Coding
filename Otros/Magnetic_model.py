import numpy as np
import magpylib as magpy
import matplotlib.pyplot as plt

# Create monopole field
def mono_field(field, observers):
    """
    Monopole field 

    field: string, "B" or "H
        return B or H-field

    observers: array_like of shape (n,3)
        Observer positions
    
    Returns: np.ndarray, shape (n,3)
        Magnetic monopole field
    """
    if field=="B":
        Qm = 1          # unit mT
    else:
        Qm = 10/4/np.pi # unit kA/m
    obs = np.array(observers).T
    field = Qm * obs / np.linalg.norm(obs, axis=0)**3
    return field.T

# Create CustomSource with monopole field
mono = magpy.misc.CustomSource(
    field_func=mono_field
)

# Compute field
print(mono.getB((1,0,0)))
print(mono.getH((1,0,0)))


###################################################################

# Create two monopole charges
mono1 = magpy.misc.CustomSource(
    field_func=mono_field,
    position=(2,2,0)
)
mono2 = magpy.misc.CustomSource(
    field_func=mono_field,
    position=(-2,-2,0)
)

# Compute field on observer-grid
X, Y = np.mgrid[-5:5:40j, -5:5:40j].transpose((0, 2, 1))
grid = np.stack([X, Y, np.zeros((40, 40))], axis=2)
B = magpy.getB([mono1, mono2], grid, sumup=True)
normB = np.linalg.norm(B, axis=2)

# Plot field in x-y symmetry plane
cp = plt.contourf(X, Y, np.log10(normB), cmap='gray_r', levels=10)
plt.streamplot(X, Y, B[:, :, 0], B[:, :, 1], color='k', density=1)

plt.tight_layout()
plt.show()


############################################################################

# Load Sphere model
trace_pole = magpy.graphics.model3d.make_Ellipsoid(
    dimension=(.3,.3,.3),
    )

for mono in [mono1, mono2]:
    # Turn off default model
    mono.style.model3d.showdefault=False

    # Add sphere model
    mono.style.model3d.add_trace(trace_pole)

# Display models
magpy.show(mono1, mono2)