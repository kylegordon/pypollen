"""
Returns the pollen count for a specified location
"""

import requests
import datetime

today = datetime.datetime.now().strftime('%Y-%m-%d')

class Pollen(object):
    """Pollen object with lat and long"""

    def __init__(self, latitude, longitude):
        """Initialize with a latitude and longitude"""

        self.latitude = latitude
        self.longitude = longitude

    @property
    def pollencount(self):
        """Returns pollen count for requested location"""

        request = requests.get('https://socialpollencount.co.uk/api/forecast?location=[%s,%s]' % (self.latitude, self.longitude))
        if request.status_code == 200:
            forecast = request.json()['forecast']
            try:
                for counter, element in enumerate(forecast):
                    if today in element['date']:
                        todays_pollen_level = element['pollen_count']
                        todays_temperature = element['temperature']
                        todays_weather = element['weather']
                        return todays_pollen_level
            except ValueError:
                raise RuntimeError("Unexpected response")
        else:
            raise IOError("Failure downloading from API")
