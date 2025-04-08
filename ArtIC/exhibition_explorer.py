'''Paste in the LLM output.
import requests
import sys

def search_exhibitions(term: str) -> list[int]:
    '''Make a request to exhibitions/search for the search term,
    using Elasticsearch `exists` option to only return results where the `artwork_titles` field is not empty
    Process the result and return a list of exhibitions IDs.
    '''
    url = "https://api.artic.edu/api/v1/exhibitions/search"

    # Query to search for the term and ensure artwork_titles exists
    query = {
        "q": term,
        "query": {
            "bool": {
                "must": [
                    {"exists": {"field": "artwork_titles"}}
                ]
            }
        },
        "size": 20  # Limit results to 20 exhibitions
    }

    try:
        response = requests.get(url, params=query)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        exhibitions = data.get("data", [])

        # Return a list of exhibition IDs
        exhibition_ids = []
        for exhibition in exhibitions:
            exhibition_ids.append(exhibition["id"])

        return exhibition_ids

    except requests.exceptions.RequestException as e:
        print(f"Error searching exhibitions: {e}")
        return []

def get_exhibition_artworks(exhibition_id: int) -> list[str]:
    '''Using the provided exhibition id, return a list of artwork titles from `artwork_titles` field'''
    url = f"https://api.artic.edu/api/v1/exhibitions/{exhibition_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        exhibition_data = data.get("data", {})

        # Check for artwork titles
        artwork_titles = exhibition_data.get("artwork_titles", [])

        return artwork_titles

    except requests.exceptions.RequestException as e:
        print(f"Error fetching exhibition {exhibition_id}: {e}")
        return []

def main():
    print("Welcome to the Art Institute of Chicago Exhibition Search")
    print("Enter 'exit' at any time to quit the program")

    while True:
        # Get search term from user
        search_term = input("\nEnter a search term for exhibitions: ")
        if search_term.lower() == 'exit':
            print("Goodbye!")
            sys.exit(0)

        # Search for exhibitions
        print(f"Searching for exhibitions matching '{search_term}'...")
        exhibition_ids = search_exhibitions(search_term)

        if not exhibition_ids:
            print("No exhibitions found with that search term.")
            continue

        # Get exhibition details to show the user
        print(f"\nFound {len(exhibition_ids)} exhibitions with artwork titles.")

        for i, exhibition_id in enumerate(exhibition_ids, 1):
            url = f"https://api.artic.edu/api/v1/exhibitions/{exhibition_id}"
            try:
                response = requests.get(url)
                exhibition_data = response.json().get("data", {})
                print(f"{i}. {exhibition_data.get('title', 'Unknown Title')}")
            except:
                print(f"{i}. Exhibition ID: {exhibition_id}")

        # Prompt for which exhibitions to view
        while True:
            try:
                num_to_view = input("\nHow many exhibitions would you like to view? (Enter a number, or 'back' to search again): ")
                if num_to_view.lower() == 'exit':
                    print("Goodbye!")
                    sys.exit(0)
                if num_to_view.lower() == 'back':
                    break

                num_to_view = int(num_to_view)
                if num_to_view < 1:
                    print("Please enter a positive number.")
                    continue

                num_to_view = min(num_to_view, len(exhibition_ids))
                break
            except ValueError:
                print("Please enter a valid number.")

        if num_to_view == 'back':
            continue

        # Display artwork titles for selected exhibitions
        for i in range(num_to_view):
            exhibition_id = exhibition_ids[i]
            url = f"https://api.artic.edu/api/v1/exhibitions/{exhibition_id}"

            try:
                response = requests.get(url)
                exhibition_data = response.json().get("data", {})
                exhibition_title = exhibition_data.get("title", "Unknown Exhibition")

                print(f"\n--- Exhibition: {exhibition_title} ---")

                artwork_titles = get_exhibition_artworks(exhibition_id)

                if not artwork_titles:
                    print("No artwork titles found for this exhibition.")
                else:
                    print("Artworks in this exhibition:")
                    for idx, artwork in enumerate(artwork_titles, 1):
                        if isinstance(artwork, dict):
                            # Check if artwork is a dictionary containing title or alt_titles
                            if "title" in artwork:
                                print(f"  {idx}. {artwork['title']}")
                            elif "alt_titles" in artwork and artwork["alt_titles"]:
                                print(f"  {idx}. {', '.join(artwork['alt_titles'])}")
                            else:
                                print(f"  {idx}. [Title not available]")
                        else:
                            # Assume artwork is directly a title string
                            print(f"  {idx}. {artwork}")

            except requests.exceptions.RequestException as e:
                print(f"Error fetching exhibition {exhibition_id}: {e}")

if __name__ == "__main__":
    main()


Does it work?''
#Yes this code works,but it has issues filtering out exhibitions with no artwork titles. Capt Yarbrough looked at out code
#and said that the actual code is correct and there might be issues on the backend and that our code is good to submit.
