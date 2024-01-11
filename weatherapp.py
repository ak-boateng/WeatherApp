import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()


def get_data(url):
    try:
        # Make a GET request to the specified URL
        r = requests.get(url)

        # Check if the request was successful (status code 200)
        if r.status_code == 200:
            # Return the content of the response
            return r.text
        else:
            # If the request was not successful, print an error message
            print(f"Error: Unable to fetch data. Status code: {r.status_code}")
            return None

    except Exception as e:
        # Handle exceptions, such as network errors
        print(f"Error: {e}")
        return None


# Get data from url by calling the get_data function and storing it in a variable
html_data = get_data("https://weather.com/en-GH/weather/today/l/GHXX0001:1:GH")

# parse data in html format using Beautiful Soup
soup = BeautifulSoup(html_data, "html.parser")

# format the parsed data
pretty_html = soup.prettify()


# Find the span with the current temperature
current_temp_span = soup.find("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")

# Find the div with chances of rain
chances_rain_div = soup.find("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

# Extract the text content
current_temp = current_temp_span.get_text(strip=True) if current_temp_span else "N/A"
chances_rain = chances_rain_div.get_text(strip=True) if chances_rain_div else "N/A"

# Construct the result string
result = f"Current temperature is {current_temp} in Accra, Ghana\nChances of rain: {chances_rain}"

n.show_toast("Weather update", result, duration = 10)
