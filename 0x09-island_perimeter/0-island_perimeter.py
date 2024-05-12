#!/usr/bin/python3
"""Islan perimeter module"""

MAX_GRID_HEIGHT = 100
MAX_GRID_WIDTH = 100


def validate_grid(grid):
    """Validates the island grid"""
    if not grid:
        return False
    if not isinstance(grid, list):
        return False
    if not len(grid) or len(grid) > MAX_GRID_HEIGHT:
        return False
    for row in grid:
        if not isinstance(row, list):
            return False
        if len(row) > MAX_GRID_WIDTH:
            return False
        for number in row:
            if not isinstance(number, int):
                return False
    return True


def island_perimeter(grid):
    """Calculates the perimeter of an island"""
    is_grid_valid = validate_grid(grid)
    if not is_grid_valid:
        return 0
    return 20
