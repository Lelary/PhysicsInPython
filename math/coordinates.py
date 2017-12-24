import math


def cartesian_to_polar(x, y):
    r_square = x*x + y*y
    r = math.sqrt(r_square)
    theta = math.atan2(y, x)
    return r, theta

def polar_to_cartesian(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

def cartesian_to_cylindrical(x, y, z):
    r, theta = cartesian_to_polar(x, y)
    return r, theta, z

def cylindrical_to_cartesian(r, theta, z):
    x, y = polar_to_cartesian(r, theta)
    return x, y, z

def cartesian_to_spherical(x, y, z):
    d, theta = cartesian_to_polar(x, y)
    r, phi = cartesian_to_polar(z, d)
    return r, theta, phi

def spherical_to_cartesian(r, theta, phi):
    z, d = polar_to_cartesian(r, phi)
    x, y = polar_to_cartesian(d, theta)
    return x, y, z

