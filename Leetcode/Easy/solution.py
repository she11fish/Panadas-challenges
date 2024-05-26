import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world_with_big_countries = world[((world['area'] >= 3000000) | (world['population'] >= 25000000))]
    return world_with_big_countries[['name', 'area', 'population']]