from __future__ import print_function
import unittest
import gridpp
import numpy as np


def get_grid(coordinate_type):
    lons, lats = np.meshgrid([0, 1], [0, 1, 2])
    if coordinate_type == gridpp.Geodetic:
        factor = 1
    else:
        factor = 111000
    return gridpp.Grid(lats * factor, lons * factor, lons * 0, lons * 0, coordinate_type)

def get_points(coordinate_type):
    lats = np.array([0, 1, 2])
    lons = np.array([0, 0, 0])
    if coordinate_type == gridpp.Geodetic:
        factor = 1
    else:
        factor = 111000
    return gridpp.Points(lats * factor, lons * factor, lons * 0, lons * 0, coordinate_type)

coordinate_types = {gridpp.Geodetic: 1, gridpp.Cartesian: 111000}

class Test(unittest.TestCase):
    def test_point_to_grid(self):
        for coordinate_type in coordinate_types:
            grid = get_grid(coordinate_type)
            points = get_points(coordinate_type)
            radius = 120000
            output = gridpp.count(points, grid, radius)
            np.testing.assert_array_equal(output, ((2,1), (3,1), (2,1)))

    def test_grid_to_grid(self):
        for coordinate_type in coordinate_types:
            igrid = get_grid(coordinate_type)
            ogrid = get_grid(coordinate_type)
            radius = 120000
            output = gridpp.count(igrid, ogrid, radius)
            np.testing.assert_array_equal(output, ((3,3), (4,4), (3,3)))

    def test_grid_to_point(self):
        for coordinate_type in coordinate_types:
            grid = get_grid(coordinate_type)
            points = get_points(coordinate_type)
            radius = 120000
            output = gridpp.count(grid, points, radius)
            np.testing.assert_array_equal(output, [3, 4, 3])

    def test_point_to_point(self):
        for coordinate_type in coordinate_types:
            ipoints = get_points(coordinate_type)
            opoints = get_points(coordinate_type)
            radius = 120000
            output = gridpp.count(ipoints, opoints, radius)
            np.testing.assert_array_equal(output, [2, 3, 2])


if __name__ == '__main__':
    unittest.main()
