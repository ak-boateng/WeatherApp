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
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
            return None

    except Exception as e:
        # Handle exceptions, such as network errors
        print(f"Error: {e}")
        return None


html_data = get_data("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")

soup = BeautifulSoup(html_data, "html.parser")

pretty_html = soup.prettify()

print(pretty_html)

current_temp = soup.find_all("span",

                             class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")

chances_rain = soup.find_all("div",

                             class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

temp = (str(current_temp))

temp_rain = str(chances_rain)

result = "current_temp " + temp[128:-9] + "  in Sunyani, Ghana" + "\n" + temp_rain[131:-14]



n.show_toast("Weather update", result, duration = 10)
