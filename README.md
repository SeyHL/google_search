This app was created as part of my first job interview. The assignment was to create HTML website with one input for keyword. Entered keyword is searched on Google
and only organic results from the first page of search are shown. It should have been possible to download these results in machine-readable format. In this case, 
I decided to use csv format.
The application was created in Django using HTML, CSS, JavaScript and Python. SerpApi was used for Google Search.

INSTRUCTIONS OF USE:
1. Use following command to copy the repository to your local machine.
	git clone https://github.com/SeyHL/google_search.git
2. Install following modules on your computer:
	a) Django: pip install django
	b) dotenv: python -m pip install python-dotenv
	c) SerpApi: pip install google-search-results
3. Register on https://serpapi.com/ to get API Key
	- Create an account, then sign in. From the menu on the left choose Api Key, click "Generate API Key" and copy it.
	- The key is required for use of SerpApi.
4. In google_search_app folder create file named ".env". Assign copied key to "SERPAPI_KEY" variable.
	SERPAPI_KEY = "your API key".
5. In views.py specify parameters of search in params variable.
	- List of parameters can be found in the official documentation: https://serpapi.com/search-api
	- Specific code examples can be found there: https://serpapi.com/playground
