

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
    #*Create a dictionary of facilities and their coordinates
    facilities_dict = {facility: facility.coordinates for facility in facilities}
    
    #*Create a dictionary of houses and their coordinates
    houses_dict = {house: house.coordinates for house in houses}
    
    #*Create a dictionary of houses and their optimal building
    optimal_building_dict = {}
    
    #*Loop through the houses
    for house in houses_dict:
        #*Create a dictionary of distances between the house and each facility
        distance_dict = {facility: distance(houses_dict[house], facilities_dict[facility]) for facility in facilities_dict}
        
        #*Find the minimum distance
        min_distance = min(distance_dict.values())
        
        #*Find the facility that has the minimum distance
        for facility in distance_dict:
            if distance_dict[facility] == min_distance:
                optimal_building_dict[house] = facility
    
    #*Return the optimal building for each house
    return [optimal_building_dict[house] for house in houses_dict]
    
    #*Time Complexity: O(n^2)
    #*Space Complexity: O(n)
    
  