import math
import numpy
from pyquaternion import Quaternion

from vector3 import *

def spherical2cartesian(sph):
    d = sph[0]
    ra = math.radians(sph[1])
    dec = math.radians(sph[2])
    
    x = d * math.cos(dec) * math.cos(ra)
    y = d * math.cos(dec) * math.sin(ra)
    z = d * math.sin(dec)
    
    return vec3(x, y, z)

# rotate an orientation matrix
def rotate_matrix(orientation_matrix, rotation):
    # orientation matrix is a 3x3 matrix, rotation is a list of three angles in degrees
    orientation_matrix = numpy.array(orientation_matrix)
        
    if rotation[0]:
        rotator = Quaternion(axis=orientation_matrix[0], angle=math.radians(rotation[0]))
        orientation_matrix = (numpy.array([rotator.rotate(orientation_matrix[0]), rotator.rotate(orientation_matrix[1]), rotator.rotate(orientation_matrix[2])]))

    if rotation[1]:
        rotator = Quaternion(axis=orientation_matrix[1], angle=math.radians(rotation[1]))
        orientation_matrix = (numpy.array([rotator.rotate(orientation_matrix[0]), rotator.rotate(orientation_matrix[1]), rotator.rotate(orientation_matrix[2])]))

    if rotation[2]:
        rotator = Quaternion(axis=orientation_matrix[2], angle=math.radians(rotation[2]))
        orientation_matrix = (numpy.array([rotator.rotate(orientation_matrix[0]), rotator.rotate(orientation_matrix[1]), rotator.rotate(orientation_matrix[2])]))

    return orientation_matrix.tolist()
