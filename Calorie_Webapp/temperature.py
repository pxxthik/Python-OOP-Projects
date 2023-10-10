class Temperature:
    """
    Represents a temperature value extracted from the timeanddate.com/weather webpage.
    """

    def __init__(self, country, city):
        self.city = city
        self.country = country

    def get(self):
        # code for web scraping

        return float(18)


if __name__ == "__main__":
    temperature = Temperature(country='usa', city='san francisco')
    print(temperature.get())
