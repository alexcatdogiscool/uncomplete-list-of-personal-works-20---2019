import math
import numpy as np

def norm(arr):
    return (arr[0]**2 + arr[1]**2 + arr[2]**2)**0.5

def normalize(arr):
    s = (arr[0]**2 + arr[1]**2 + arr[2]**2)**0.5
    n = np.array([arr[0]/s, arr[1]/s, arr[2]/s])
    return n

def deg2rad(deg):
    return deg * math.pi/180

def rad2deg(rad):
    return rad * 180/math.pi

def spheredst(raypos, spherepos, rad):
    return norm((raypos % 1) - (spherepos)) - rad

def planedst(raypos, planey):
    return abs(raypos[0] - planey)