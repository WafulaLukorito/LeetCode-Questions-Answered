

def optimal_building (facilities, houses):
    """Return the optimal building for each house in houses.

    The optimal building for a house is the facility that is closest to it.
    If there are multiple facilities that are all the same distance from a
    house, then any one of those facilities can be the optimal building.

    Arguments:
      facilities: a list of facilities
      houses: a list of houses

    Return value: a list of facilities, the same length as houses, where the
      i-th element is the optimal building for the i-th house.
    """
    optimal_buildings = []
    for house in houses:
        min_distance = float('inf')
        closest_facility = None
        for facility in facilities:
            distance = abs(facility - house)
            if distance < min_distance:
                min_distance = distance
                closest_facility = facility
        optimal_buildings.append(closest_facility)
    return optimal_buildings
    
  