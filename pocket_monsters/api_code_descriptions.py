# separate file to house api codes, their status and descriptions.
# use this dictionary as a CONSTANT variable for the poke_builder.py
# this should aid in debugging api errors

api_dict = {
    200: {'status': 'OK', 
            'description': 'The request was completed.'},
    201: {'status': 'Created', 
            'description': 'A new resource was successfully created.'},
    400: {'status': 'Bad Request', 
            'description': 'The request was invalid.'},
    401: {'status': 'Unauthorized', 
            'description': 'The request did not include an authentication token or the authentication token was expired.'},
    403: {'status': 'Forbidden', 
            'description': 'The client did not have permission to access the requested resource.'},
    404: {'status': 'Not Found', 
            'description': 'The requested resource was not found.'},
    405: {'status': 'Method Not Allowed', 
            'description': 'The HTTP method in the request was not supported by the resource. For example, the DELETE method cannot be used with the Agent API.'},
    409: {'status': 'Conflict', 
            'description': 'The request could not be completed due to a conflict. For example, POST ContentStore Folder API cannot complete if the given file or folder name already exists in the parent location.'},
    500: {'status': 'Internal Server Error', 
            'description': 'The request was not completed due to an internal error on the server-side.'},
    503: {'status': 'Service Unavailable', 
            'description': 'The server was unavailable.'}
    }


"""
Get the data from somewhere (Scraping, API calls, extisting database), transform it (Python, Spark, dbt), load it (local DB, online Data Warehouse, Data Lake)...


Scrape api data from pokemon api
	which tables are needed to review battle data?
	table1, 2, 3, 4, 5, 6 etc.
List out the relevant api url's needed
Class needs to pull from each url, and store in a combined data set or multiple datasets

Can perform data analysis with just the above (KP)

BUT for DE practice, I should...

	pull in all this data.

	create new dataframes that combine certain tables together

	load that data into a data warehouse

	pull that data into a dashboard?
"""