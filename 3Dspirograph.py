import numpy as np
import bpy
import hashlib
from scipy.spatial import distance

def create_spherical_spiral(radius, loops_theta, loops_phi, loops_psi, samples=1000, location=(0,0,0)):
    """
    Function to create a 3D spherical spiral in the Blender scene.
    Generates a unique hash identifier for each spirograph based on input parameters.
    Returns the created spirograph object and the points forming the spiral.
    """
    # Generate an array of samples
    u = np.linspace(0, 2 * np.pi, samples)
    # Calculate theta, phi, and psi values
    theta = loops_theta * u
    phi = loops_phi * u
    psi = loops_psi * u

    # Compute x, y, and z coordinates for the spiral
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(phi) * np.sin(psi)
    z = radius * np.cos(psi)

    # Create a list of points for the spiral
    points = list(zip(x, y, z))
   
    # Create a new curve for the spiral
    spiral_curve = bpy.data.curves.new('SphericalSpiral', type='CURVE')
    spiral_curve.dimensions = '3D'
    spiral_curve.resolution_u = 2
    polyline = spiral_curve.splines.new('POLY')
    polyline.points.add(len(points) - 1)
    for idx, coord in enumerate(points):
        polyline.points[idx].co = (*coord, 1)

    # Create a new object for the spiral
    spiral_object = bpy.data.objects.new('SphericalSpiral', spiral_curve)
    bpy.context.collection.objects.link(spiral_object)
    spiral_object.location = location

    # Generate a unique hash identifier for the spiral
    spirograph_params = f"Radius: {radius}, Loops Theta: {loops_theta}, Loops Phi: {loops_phi}, Loops Psi: {loops_psi}"
    hashed_params = hashlib.sha256(spirograph_params.encode()).hexdigest()

    # Assign the hash identifier to the object and curve data
    spiral_object.name = hashed_params
    spiral_curve.name = hashed_params

    return spiral_object, points

def decode_spherical_spiral(points, parameter_space):
    """
    Function to decode a 3D spherical spiral.
    Computes the Euclidean distance between the points of the original spiral 
    and a spiral generated with parameters from a provided parameter space.
    Returns the parameters that result in the minimal total distance.
    Throws an exception if no parameters from the parameter space can decode the spiral.
    """
    min_params = ()
    min_distance = float('inf')

    # Iterate over all parameter combinations in the parameter space
    for params in parameter_space:
        radius, loops_theta, loops_phi, loops_psi = params
        u = np.linspace(0, 2 * np.pi, len(points))
        theta = loops_theta * u
        phi = loops_phi * u
        psi = loops_psi * u

        # Compute x, y, and z coordinates for the spiral
        x = radius * np.sin(theta) * np.cos(phi)
        y = radius * np.sin(phi) * np.sin(psi)
        z = radius * np.cos(psi)

        # Create a list of points for the spiral
        spiral_points = list(zip(x, y, z))
        # Compute the total distance between the original and generated spiral points
        total_distance = np.sum(distance.cdist(points, spiral_points))

        # Update the minimum distance and corresponding parameters
        if total_distance < min_distance:
            min_distance = total_distance
            min_params = params

    # Throw an exception if no parameters could decode the spiral
    if min_params == ():
        raise Exception('Could not decode the spiral with the provided parameter space. \
                        Try expanding the parameter space or increasing the number of samples.')

    return min_params

# Create a spherical spiral
radius = 1
loops_theta = 2
loops_phi = 3
loops_psi = 4
curve_object, points = create_spherical_spiral(radius, loops_theta, loops_phi, loops_psi, samples=1000, location=(0,0,0))

# Decode the spherical spiral
param_space = [(radius, loops_theta, loops_phi, loops_psi)]
try:
    decoded_params = decode_spherical_spiral(points, param_space)
    print(decoded_params)
except Exception as e:
    print('Decoding failed with error:', str(e))