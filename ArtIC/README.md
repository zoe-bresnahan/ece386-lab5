# Art Institute of Chicago API

Prompt engineering to have a LLM make a Python script to query exhibitions.

***Student**, Complete below.*

## Stats

### How many different prompts did you have to try before it worked?
about 10, LLM had a hard time understanding what I meant by filtering out exhibitions with no artwork names

### How well did the final produced script work?
it worked fairly well, but still had issues with filtering out exhibitions with no artwork names. Captain Yarbrough said that the code was right and good to submit and likely having backend issues with 'exists'

### What are some of the artwork titles from the exhibition "Ink on Paper: Japanese Monochromatic Prints (2009)"
"The Monkey Bridge in Winter" and "Tanabata Dance" are two artwork titles in this exhibition

## Prompt
### Share the conversation URL
https://claude.ai/share/6b14754c-23c4-406f-8787-8c2a977cce0b
## Paste your prompt here
Give an entire Python script that with no edits does the following:
1.	Accepts a search term from the user.
2.	Searches the ArtIC API for exhibitions matching that term and that have artwork titles.
Make sure that an exhibition is not included if there are not artwork titles listed (only return results where the `artwork_titles` field is not empty)
3.	Prompts the user for a number of exhibitions they would like to view.
4.	Display the titles of the artwork for the exhibition to the user.		
When you display the titles use the `title` string or the `alt_titles` array to show the user the name of the artworks that are in the exhibition
5.	Loops until user exit.

Here is a search example from the Art Institute of Chicago API documentation:
>GET /exhibitions/search
Search exhibitions data in the aggregator.
#Available parameters:
•	q - Your search query
•	query - For complex queries, you can pass Elasticsearch domain syntax queries here
•	sort - Used in conjunction with query
•	from - Starting point of results. Pagination via Elasticsearch conventions
•	size - Number of results to return. Pagination via Elasticsearch conventions
•	facets - A comma-separated list of 'count' aggregation facets to include in the results.
``` {
    "preference": null,
    "pagination": {
        "total": 6505,
        "limit": 10,
        "offset": 0,
        "total_pages": 651,
        "current_page": 1
    },
    "data": [
        {
            "_score": 1,
            "api_model": "exhibitions",
            "api_link": "https://api.artic.edu/api/v1/exhibitions/1352",
            "id": 1352,
            "title": "Artful Alphabets: Five Picture Book Artists",
            "timestamp": "2022-05-08T23:17:42-05:00"
        },
        {
            "_score": 1,
            "api_model": "exhibitions",
            "api_link": "https://api.artic.edu/api/v1/exhibitions/1357",
            "id": 1357,
            "title": "June Wayne's Narrative Tapestries: Tidal Waves, DNA, and the Cosmos",
            "timestamp": "2022-05-08T23:17:42-05:00"
        },
        {
            "_score": 1,
            "api_model": "exhibitions",
            "api_link": "https://api.artic.edu/api/v1/exhibitions/1374",
            "id": 1374,
            "title": "Jindrich Heisler: Surrealism under Pressure",
            "timestamp": "2022-05-08T23:17:42-05:00"
        }
    ],
    "info": {
        "license_text": "The data in this response is licensed under a Creative Commons Zero (CC0) 1.0 designation and the Terms and Conditions of artic.edu.",
        "license_links": [
            "https://creativecommons.org/publicdomain/zero/1.0/",
            "https://www.artic.edu/terms"
        ],
        "version": "1.13"
    },
    "config": {
        "iiif_url": "https://www.artic.edu/iiif/2",
        "website_url": "http://www.artic.edu"
    }
}```


Use the requests library instead of the builtin HTTP library by doing `import requests`

Use the following function definitions to guide you:

```def search_exhibitions(term: str) -> list[int]:
    '''Make a request to exhibitions/search for the search term,
    using Elasticsearch `exists` option to only return results where the `artwork_titles` field is not empty
    Process the result and return a list of exhibitions IDs.
    '''
```

```def get_exhibition_artworks(exhibition_id: int) -> list[str]:
	'''using the provided exhibition id use the return a list of artwork titles from `artwork_titles` field

# TODO: main function that repeatedly prompts the user for a search term, then calls the search_exhibitions function and prints the list of exhibition titles, then calls the get_exhibition_artworks function and prints the artwork titles, then reprompts the user for a new search term
