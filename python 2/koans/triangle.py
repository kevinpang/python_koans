#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
	if a <= 0 or b <= 0 or c <= 0:
		raise TriangleError
	
	sorted_sides = sorted([a, b, c])
	
	if sorted_sides[0] + sorted_sides[1] <= sorted_sides[2]:
		raise TriangleError
	
	unique_sides = set([a, b, c])
	num_unique_sides = len(unique_sides)
	
	if num_unique_sides == 1:
		return 'equilateral'
	elif num_unique_sides == 2:
		return 'isosceles'
	else:
		return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
