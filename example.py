import pyweatherreport.main as pwr
weather = pwr.WeatherReport("Chennai")
weatherconditions = {
  "Temperature":weather.Temperature(inkelvin=False),
  "Humidity":weather.Humidity(),
  "Pressure":weather.Pressure(),
  "Wind Speed":weather.WindSpeed(),
  "Wind Degree":weather.WindDegree()
}
print(weatherconditions)
  
