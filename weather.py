import urllib2
import json

key = '00f68345fb385b42'
zip = raw_input('enter name of city that you like to see the weather? ')
url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/PA/' + zip + '.json'
f = urllib2.urlopen(url)
json_string = f.read()
print json_string
parsed_json = json.loads(json_string)
#print parsed_json

weather = parsed_json['current_observation']['weather']
##########################################################################
"""if 'current_observation' in parsed_json:
    weather = parsed_json['current_observation']['weather']
else:
     a=parsed_json['response']['results']
     a=a[0]['city']
     print a
     url='http://api.wunderground.com/api/' + key +'/conditions'+ a +'.json'
     f = urllib2.urlopen(url)
     json_string = f.read()
     print json_string

     parsed_json = json.loads(json_string)
"""

##########################################################################

temp = parsed_json['current_observation']['temp_c']
city = parsed_json['current_observation']['display_location']['city']
state = parsed_json['current_observation']['display_location']['state']
humidity = parsed_json['current_observation']['relative_humidity']
windspeed = parsed_json['current_observation']['wind_mph']
obstime = parsed_json['current_observation']['observation_time']
print 'This weather is ' + weather.lower() + '!'
print str(temp) + ' degrees.'
print city + " , " + state
print " Humidity is " + humidity
print "Wind speed is" + str(windspeed)
print obstime

f.close()
