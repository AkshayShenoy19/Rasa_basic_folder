from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import re
import pandas as pd
import os
import smtplib
import imghdr
from email.message import EmailMessage

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "e556cab022363342ab67be69f38554f7"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        priceRange = tracker.get_slot('price')

        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)

        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30, 'italian': 55, 'biryani': 7, 'north indian': 50,
                         'south indian': 85}

        results1 = zomato.modrestaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 0, 20)
        d11 = json.loads(results1)
        df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d11['restaurants']])

        results2 = zomato.modrestaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20, 20)
        d12 = json.loads(results2)
        df2 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d12['restaurants']])

        results3 = zomato.modrestaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 40, 20)
        d13 = json.loads(results3)
        df3 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d13['restaurants']])

        results4 = zomato.modrestaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 60, 20)
        d14 = json.loads(results4)
        df4 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d14['restaurants']])

        results5 = zomato.modrestaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 80, 20)
        d15 = json.loads(results5)
        df5 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d15['restaurants']])

        frames = [df1, df2, df3, df4, df5]
        df = pd.concat(frames).reset_index(drop=True)

        emailClass = EmailRestaurants()
        response = emailClass.filterprice(priceRange,df,5)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]

def check_if_string_in_file(string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open('MyFile.txt', 'r') as CityNames:
        # Read all lines in the file one by one
        for line in CityNames:
            # For each line, check if line contains the string
            if re.match(string_to_search, line):
                if len(string_to_search) == len(line.strip()):
                    #print(line, string_to_search)
                    return True
        CityNames.close()
    return False


class CheckLocation(Action):

    def name(self):
        return 'check_location'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')

        check = check_if_string_in_file(loc.lower())
        #print(check)

        if check:
            return [SlotSet('check_op', True)]
        else:
            return [SlotSet('check_op', False)]


class CheckEmail(Action):

    def name(self):
        return 'check_email'

    def run(self, dispatcher, tracker, domain):
        e = tracker.get_slot('email')

        if re.match(r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+', e):
            return [SlotSet('flag_email', True)]
        if re.match(r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+\.[a-z]+', e):
            return [SlotSet('flag_email', True)]
        if re.match(r'[a-zA-Z0-9]+\.[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+\.[a-z]+',e):
            return [SlotSet('flag_email', True)]
        else:
            return [SlotSet('flag_email', False)]


class SendEmail(Action):

    def name(self):
        return 'send_email'

    def run(self, dispatcher, tracker, domain):

        e = tracker.get_slot('email')
        p = tracker.get_slot('price')

        config = {"user_key": "e556cab022363342ab67be69f38554f7"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)

        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30, 'italian': 55, 'biryani': 7, 'north indian': 50,
                         'south indian': 85}

        results1 = zomato.modrestaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 0, 20)
        d11 = json.loads(results1)
        df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d11['restaurants']])

        results2 = zomato.modrestaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20, 20)
        d12 = json.loads(results2)
        df2 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d12['restaurants']])

        results3 = zomato.modrestaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 40, 20)
        d13 = json.loads(results3)
        df3 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d13['restaurants']])

        results4 = zomato.modrestaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 60, 20)
        d14 = json.loads(results4)
        df4 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d14['restaurants']])

        results5 = zomato.modrestaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 80, 20)
        d15 = json.loads(results5)
        df5 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d15['restaurants']])

        frames = [df1, df2, df3, df4, df5]
        df = pd.concat(frames).reset_index(drop=True)

        mailClass = EmailRestaurants()
        mailClass.mail(p, e, df)

        dispatcher.utter_message("-----" + 'List of restaurants has been send to ' + e)

class EmailRestaurants:

    def mail(self, x, y, dataFrame):
        EMAIL_ADDRESS = 'dellinteli58@gmail.com'
        EMAIL_PASSWORD = '@password123'

        msg = EmailMessage()
        msg['Subject'] = 'List of top restaurants'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = y

        msg.set_content(self.filterprice(x, dataFrame,10))
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

    def filterprice(self, pricerange, dataFrame, lim):
        if pricerange == 'low':
            x = dataFrame[dataFrame['budget_for2people'] <= 300]
        elif pricerange == 'mid':
            x = dataFrame[(dataFrame['budget_for2people'] > 300) & (dataFrame['budget_for2people'] <= 700)]
        elif pricerange == 'high':
            x = dataFrame[dataFrame['budget_for2people'] > 700]

        x = x.sort_values(by=['restaurant_rating']).head(lim)
        restaurant_name = x['restaurant_name'].tolist()
        restaurant_rating = x['restaurant_rating'].tolist()
        restaurant_address = x['restaurant_address'].tolist()
        budget_for2people = x['budget_for2people'].tolist()

        line = zip(restaurant_name, restaurant_rating, restaurant_address, budget_for2people)
        line = list(line)

        if len(restaurant_name) == 0:
            return "No Restaurants Found..!!!"
        else:
            resp = ""
            for v in line:
                r = ""
                r = r + str(v[0]) + ' in ' + str(v[2]) + ' and Average price for two people is: ' \
                    + str(v[3]) + ' also Zomato user rating is ' + str(v[1]) + '\n' + '\n'
                resp = resp + r
            return resp