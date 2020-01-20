from numpy import arccos, array, dot, pi, cross, linspace, arange
from numpy.linalg import det, norm

class Octagon():
    def __init__(self, size, intercept):
        self.size = size
        self.intercept = intercept

    def in_out_border(self, x, y, r):
            #creating arrays for further use - distance calculation and fuel cell position determination in relation to octagon borders
            p = array([x,y])
            a1 = array([self.intercept-self.size, self.size])
            a2 = array([self.size, self.intercept-self.size])
            a3 = array([self.size, self.size-self.intercept])
            a4 = array([self.intercept-self.size, -1*self.size])
            a5 = array([self.size-self.intercept, -1*self.size])
            a6 = array([-1*self.size, self.size-self.intercept])
            a7 = array([-1*self.size, self.intercept-self.size])
            a8 = array([self.size-self.intercept, self.size])
            oct_pts = [a1, a2, a3, a4, a5, a6, a7, a8]
            #calculating the distance between fuel cell center and individual octagon borders
            for oct_pt in range(8):
                if all(oct_pts[oct_pt] == p) or all(oct_pts[(oct_pt+1)%8] == p):
                    distance = 0
                elif arccos(dot((p - oct_pts[oct_pt]) / norm(p - oct_pts[oct_pt]), (oct_pts[(oct_pt+1)%8] - oct_pts[oct_pt]) / norm(oct_pts[(oct_pt+1)%8] - oct_pts[oct_pt]))) > pi / 2:
                    distance = norm(p - oct_pts[oct_pt])
                elif arccos(dot((p - oct_pts[(oct_pt+1)%8]) / norm(p - oct_pts[(oct_pt+1)%8]), (oct_pts[oct_pt] - oct_pts[(oct_pt+1)%8]) / norm(oct_pts[oct_pt] - oct_pts[(oct_pt+1)%8]))) > pi / 2:
                    distance = norm(p - oct_pts[(oct_pt+1)%8])
                else:
                    distance = norm(cross(oct_pts[oct_pt]-oct_pts[(oct_pt+1)%8], oct_pts[oct_pt]-p))/norm(oct_pts[(oct_pt+1)%8]-oct_pts[oct_pt])
                #comparing the distance with radius of fuel cell
                if abs(distance) <= r:
                    return 'BORDER'
            if  (
                    -1*self.size < x < self.size and -1*self.size < y < self.size and
                    #comparing fuel coordinates with vertical and horizontal borders of octagon
                    cross(p-a1, a2-a1) > 0 and cross(p-a3, a4-a3) > 0 and cross(p-a5, a6-a5) > 0 and cross(p-a7, a8-a7) > 0
                    #comparing fuel coordinates with diagonal borders of octagon by finding out if they are below or above the border 
                ):
                return 'IN'
            else:
                return 'OUT'