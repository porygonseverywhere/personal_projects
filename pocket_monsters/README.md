
# Which Type of Pokemon Trainer Would be the Hardest to Battle?

If you played any of the Pokemon games, you know that there are always annoying Trainers scattered along the routes who interrupt you while you're trying to explore.

These Trainers tend to only have Pokemon of a certain "type", i.e. "Bugcatcher Ryan" only has grass type Pokemon. I'm curious if there is one type that is more advantageous than the others. If you were to encounter one of these Trainers, which type would be the hardest to defeat? 

# The Process

## Extract, Transform, Load

### API Source, Python, PostgreSQL

Before we start answering the "Business Question", we need to gain access to this data. There is a wonderfully put together API source "https://pokeapi.co/" that contains all the Pokemon data we could ask for. 

So what I'd like to do is create a simple pipeline that establishes a connection to the API endpoints of interest, pulls or *extracts* that information, *transforms* the semi-structured JSON data into various, structured tables that are then stored on or *loaded* to PostgreSQL.


## Roadmap

- Automate the API call and determine if any new datapoints were added. 
    - for example: New Pokemon Games are routinely released, and with that come new types, stats, and even Pokemon. If there is new data that could impact the analysis, then we want to make sure we have that.

- Analyze the data and answer the original Business Question

- Code is functional, but identify and resolve and weakspots in security, memory usage, functionality, etc.

