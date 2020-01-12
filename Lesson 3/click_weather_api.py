from requests import get
import click
import sys

URL = 'http://api.weatherstack.com/current'


@click.command()
@click.option('--token', 'weather_access_key')
@click.option('--city', 'city_name')
@click.option('--T', 'degree_type')
def main(weather_access_key, degree_type, city_name):
    if degree_type.lower() == 'fahrenheit':
        unit = 'f'
        temperature_scale = 'Fahrenheit'
    elif degree_type.lower() == 'celsius':
        unit = 'm'
        temperature_scale = 'Celsius'
    else:
        print('SyntaxError: The chosen measure unit is invalid, please use "Celsius" or "Fahrenheit" ')
        sys.exit()

    city_list = city_name.split(',')
    for city in city_list:
        response = get(URL+'?access_key=%s&query=%s&units=%s' % (weather_access_key, city, unit))
        response_json = response.json()
        if 'error' in response_json:
            if 'invalid_access_key' in response_json['error']['type']:
                print('TokenValidationError: Your token is invalid, please verify you are using a valid token, and try'
                      ' again')
            elif 'request_failed' in response_json['error']['type']:
                print('''
    Error: The city chosen could not be found, please check if you spelled the name correctly, or try on of these:
    * London
    * Paris
    * Berlin
                ''')
            sys.exit()
        else:
            weather = response_json['current']['temperature']
            print(
                'The weather in %s is %s %s' % (city, weather, temperature_scale))


if __name__ == '__main__':
    main()
