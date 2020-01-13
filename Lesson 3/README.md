# opsschool5-coding

In order to use this script run 'click_weather_api.py --token <my_token> --city <city_seperated_by_comma> --T <Measure_unit>'

my_token - Your https://weatherstack.com/ API access key
city_seperated_by_comma - At least one (valid) city name (see example below)
Measure_unit - Celsius or Fahrenheit

Example usage: click_weather_api.py --token 12345609876 --city tokyo --T Celsius

Please replace the access key with a valid one before executing the script.  
Use quotation mark, for cities with whitespace in their name.  

Example:  
New York, should be converted to "New York"
