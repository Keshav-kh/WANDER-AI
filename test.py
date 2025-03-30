import requests

def test_google_hotels():
    # Google Hotels API endpoint via SerpApi
    url = "https://serpapi.com/search.json"
    
    # Define the parameters for the hotel search
    params = {
        "engine": "google_hotels",
        "q": "Hotels in Austin",       # Modify the query as needed
        "check_in_date": "2025-03-27",  # Format: YYYY-MM-DD
        "check_out_date": "2025-03-28", # Format: YYYY-MM-DD
        "currency": "USD",
        "hl": "en",
        "api_key": "4e1c7c0180853cf4cbc16e0aad62e5e83b7f08e131407fe671a7e915e52c8fdf"       # Replace with your actual API key
    }
    
    # Make the GET request to the Hotels API
    response = requests.get(url, params=params)
    
    # Check for a successful response and print the JSON output
    if response.status_code == 200:
        print("Hotel API Response:")
        print(response.json())
    else:
        print("Error fetching hotel data:", response.status_code, response.text)

if __name__ == "__main__":
    test_google_hotels()
