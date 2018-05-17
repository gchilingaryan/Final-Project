# encoding=utf8
import json, urllib, urllib2

API_KEY = 'AIzaSyBAG6CASjfND1ApXO65d7mtpuP8Cty4fdc'

def PlaceData():
    search = ''.join(raw_input('Please, input the name of place you want to search ').split())
    while True:
        url = urllib2.urlopen('https://maps.googleapis.com/maps/api/place/textsearch/json?query=yerevan+{}&key={}'.format(search, API_KEY))
        data = json.load(url)
        if data['status'] == 'ZERO_RESULTS':
            search = ''.join(raw_input('Something went wrong, try again ').split())
        else:
            break
    return data, search

def PlaceId(data):
    result = data.get('results')
    places_id = []
    for elem in result:
        place_id = elem['place_id']
        places_id.append(place_id)
    return places_id

def PlaceDetails(places_id, search):
    for i in range(len(places_id)):
        url = urllib2.urlopen('https://maps.googleapis.com/maps/api/place/details/json?placeid={}&key={}'.format(places_id[i], API_KEY))
        data = json.load(url)

        result = data.get('result')
        print('The phone number of ' + result['name'] + ' is ' + result['international_phone_number'])
        print('The address of ' + result['name'] + ' is ' + result['formatted_address'])
        print
        for i in result['reviews']:
            print i['author_name'] + "'s feedback is: " + i['text'] + " And rating is " + str(i["rating"])
            print
        print 'Overall rating is ' + str(result['rating'])

def Weather():
    user_answer = raw_input('Want to know weather in Yerevan? ').lower()
    if user_answer == 'yes':
        url = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select item.condition from weather.forecast where woeid = 2214662 and u = 'Unit.CELSIUS'"
        yql_url = url + urllib.urlencode({'q': yql_query}) + "&format=json"
        result = urllib2.urlopen(yql_url).read()
        data = json.loads(result)

        temp = data['query']['results']['channel']['item']['condition']['temp']
        condition =  data['query']['results']['channel']['item']['condition']['text']
        if condition == 'Showers':
            print "Looks like it's going to rain today, the temperature is " + temp + u'°C'
        elif condition == 'Cloudy':
            print "It's cloudy today, the temperature is " + temp + u'°C'
        elif condition == 'Scattered Thunderstorms':
            print "Better to stay at home it's storming, the temperature is " + temp + u'°C'
        elif condition == 'Sunny':
            print "It's sunny today, the temperature is " + temp + u'°C'
        else:
            print "The temperature is " + temp + u'°C' + " Have a great day!"
    else:
        print 'Have a great day!'
def main():
    data, search = PlaceData()
    places_id = PlaceId(data)
    PlaceDetails(places_id, search)
    Weather()


main()
