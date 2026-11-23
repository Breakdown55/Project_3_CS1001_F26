from data import CountyDemographics

"""
Purpose: Compute the total population in a list of counties
Inputs: A list of CountyDemographics objects
Output: The sum of the counties populations'
Return Type: int
"""
def population_total(counties: list[CountyDemographics]) -> int:
    total = 0
    for county in counties:
        total += county.population['2014 Population']

    return total

"""
Purpose: Filter a list of counties by state code
Inputs: A list of CountyDemographics objects, a 2-letter state code
Output: A list of CountyDemographics objects with a state code equal to the state code passed in
Return Type: A list of CountyDemographics objects
"""
def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    matches = []
    for county in counties:
        if county.state == state:
            matches.append(county)

    return matches

"""
Purpose: Calculate the total population in a list of counties that match an education criteria
Inputs: A list of CountyDemographics objects, a key for education
Output: The total population in the given list that has the given education requirement 
Return Type: float 
"""
def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    if len(counties) == 0 or key not in counties[0].education:
        return 0
    
    total = 0

    for county in counties:
        proportion = county.education[key] / 100
        county_pop = county.population['2014 Population']

        total += county_pop * proportion

    return total

"""
Purpose: Calculate the total population in a list of counties that match a given ethnicity
Inputs: A list of CountyDemographics objects, an ethnicity key
Output: The total population that matches the ethnicity key
Return Type: float
"""
def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    if len(counties) == 0 or key not in counties[0].ethnicities:
        return 0
    
    total = 0

    for county in counties:
        proportion = county.ethnicities[key] / 100
        county_pop = county.population['2014 Population']

        total += county_pop * proportion

    return total

"""
Purpose: Calculate the total population under the poverty level in a list of counties
Inputs: A list of CountyDemographic objects
Output: The total population under the poverty level
Return Type: float
"""
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = 0

    for county in counties:
        total += county.income["Persons Below Poverty Level"] * (county.population['2014 Population'] / 100)

    return total

"""
Purpose: Calculate the percent of people who meet a provided education level in a list of counties
Inputs: A list of counties, the education key
Output: The percent of people who meet the provided education level
Return Type: float
"""
def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    if len(counties) == 0:
        return 0.0
    
    subtotal = population_by_education(counties, key)
    total = population_total(counties)

    return 100 * (subtotal / total)

"""
Purpose: Calculate the percent of people who match a provided ethnicity in a list of counties
Inputs: A list of counties, the ethnicity key
Output: The percent of people who meet the provided ethnicity
Return Type: float
"""
def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    if len(counties) == 0:
        return 0.0
    
    subtotal = population_by_ethnicity(counties, key)
    total = population_total(counties)

    return 100 * (subtotal / total)

"""
Purpose: Calculate the percent of people who are below the poverty level in a list of counties
Inputs: A list of counties
Output: The percent of people who are below the poverty level
Return Type: float
"""
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    if len(counties) == 0:
        return 0.0
    
    subtotal = population_below_poverty_level(counties)
    total = population_total(counties)

    return 100 * (subtotal / total)


"""
Purpose: Find the counties that have a proportion of the given level of education higher than the given threshold
Inputs: A list of CountyDemographics objects, a key, a threshold
Output: A list of CountyDemographics objects that match the education criteria
Return Type: A list of CountyDemographics objects
"""
def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matches = []
    if len(counties) == 0 or key not in counties[0].education:
        return []
    
    for county in counties:
        if county.education[key] > threshold:
            matches.append(county)

    return matches


"""
Purpose: Find the counties that have a proportion of the given level of education less than the given threshold
Inputs: A list of CountyDemographics objects, a key, a threshold
Output: A list of CountyDemographics objects that match the education criteria
Return Type: A list of CountyDemographics objects
"""
def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matches = []
    if len(counties) == 0 or key not in counties[0].education:
        return []
    
    for county in counties:
        if county.education[key] < threshold:
            matches.append(county)

    return matches


"""
Purpose: Find the counties that have a proportion of the given ethnicity higher than the given threshold
Inputs: A list of CountyDemographics objects, a key, a threshold
Output: A list of CountyDemographics objects that match the ethnicity criteria
Return Type: A list of CountyDemographics objects
"""
def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matches = []
    if len(counties) == 0 or key not in counties[0].ethnicities:
        return []
    
    for county in counties:
        if county.ethnicities[key] > threshold:
            matches.append(county)

    return matches

"""
Purpose: Find the counties that have a proportion of the given ethnicity less than the given threshold
Inputs: A list of CountyDemographics objects, a key, a threshold
Output: A list of CountyDemographics objects that match the ethnicity criteria
Return Type: A list of CountyDemographics objects
"""
def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matches = []
    if len(counties) == 0 or key not in counties[0].ethnicities:
        return []
    
    for county in counties:
        if county.ethnicities[key] < threshold:
            matches.append(county)

    return matches


"""
Purpose: Find the counties that have a proportion of poverty level greater than the given threshold
Inputs: A list of CountyDemographics objects, a threshold
Output: A list of CountyDemographics objects that match the poverty level threshold
Return Type: A list of CountyDemographics objects
"""
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    matches = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] > threshold:
            matches.append(county)

    return matches


"""
Purpose: Find the counties that have a proportion of poverty level less than the given threshold
Inputs: A list of CountyDemographics objects, a threshold
Output: A list of CountyDemographics objects that match the poverty level threshold
Return Type: A list of CountyDemographics objects
"""
def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    matches = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] < threshold:
            matches.append(county)

    return matches
