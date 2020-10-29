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
		config={ "user_key":"48aabec2941e2e007813b7b9b01f32fc"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]
    
    
def check_if_string_in_file(string_to_search):
    
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open('MyFile.txt', 'r') as CityNames:
        # Read all lines in the file one by one
        for line in CityNames:
            # For each line, check if line contains the string
            if re.match(string_to_search,line):
                if len(string_to_search)==len(line.strip()):
                    print(line,string_to_search)
                    return True
        CityNames.close()    
    return False    


   
        





class CheckLocation(Action):
    
	def name(self):
		return 'check_location'
		
	def run(self, dispatcher, tracker, domain):              
         loc = tracker.get_slot('location') 
         
         
         check = check_if_string_in_file(loc.lower())
         print(check)
         
         if check:
            return [SlotSet('check_op',True)]
         else:
            return [SlotSet('check_op',False)]  


        


class CheckEmail(Action):
    
    
	def name(self):
		return 'check_email'
		
    
	def run(self, dispatcher, tracker, domain):             
         e = tracker.get_slot('email')   
        
         if re.match(r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+',e):
             return [SlotSet('flag_email',True)]
         else:
             return [SlotSet('flag_email',False)]
        
           
class SendEmail(Action):
    
    def name(self):
        return 'send_email'
    

    def run(self, dispatcher, tracker, domain):
        
        e = tracker.get_slot('email') 
        p = tracker.get_slot('price') 
        
        config={ "user_key":"48aabec2941e2e007813b7b9b01f32fc"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20)
        d1=json.loads(results)
        def filterprice(pricerange):
            if pricerange=='low':
                d = d1['restaurants']
                df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'], 'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                                     'restaurant_address': x['restaurant']['location']['address'],'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d])
                x=df1[df1['budget_for2people']<=300].sort_values(by=['restaurant_rating']).head(10)
                restaurant_name=x['restaurant_name'].tolist()
                restaurant_rating=x['restaurant_rating'].tolist()
                restaurant_address=x['restaurant_address'].tolist()
                budget_for2people=x['budget_for2people'].tolist()
                r=" "
                zip(restaurant_name,restaurant_rating,restaurant_address,budget_for2people)
                for v in zip(restaurant_name,restaurant_rating,restaurant_address,budget_for2people):
                    r=r+" Resto_Name "+str(v[0])+' Resto_Rating '+str(v[1])+' Resto_Address '+str(v[2])+' Resto_Price '+str(v[3])+'\n'
                return r
            
            if pricerange=='mid':               
                
                d = d1['restaurants']
                df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'], 'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                                     'restaurant_address': x['restaurant']['location']['address'],'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d])
                x=df1[(df1['budget_for2people']>300) & (df1['budget_for2people']<=700)].sort_values(by=['restaurant_rating']).head(10)
                restaurant_name=x['restaurant_name'].tolist()
                restaurant_rating=x['restaurant_rating'].tolist()
                restaurant_address=x['restaurant_address'].tolist()
                budget_for2people=x['budget_for2people'].tolist()
                r=" "
                zip(restaurant_name,restaurant_rating,restaurant_address,budget_for2people)
                for v in zip(restaurant_name,restaurant_rating,restaurant_address,budget_for2people):
                    r=r+" Resto_Name "+str(v[0])+' Resto_Rating '+str(v[1])+' Resto_Address '+str(v[2])+' Resto_Price '+str(v[3])+'\n'
                return r
            
            if pricerange=='high':               
                
                d = d1['restaurants']
                df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'], 'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                                     'restaurant_address': x['restaurant']['location']['address'],'budget_for2people': x['restaurant']['average_cost_for_two']} for x in d])
                x=df1[df1['budget_for2people']>700].sort_values(by=['restaurant_rating']).head(10)
                restaurant_name=x['restaurant_name'].tolist()
                restaurant_rating=x['restaurant_rating'].tolist()
                restaurant_address=x['restaurant_address'].tolist()
                budget_for2people=x['budget_for2people'].tolist()
                r=" "
                zip(restaurant_name,restaurant_rating,restaurant_address,budget_for2people)
                for v in zip(restaurant_name,restaurant_rating,restaurant_address,budget_for2people):
                    r=r+" Resto_Name "+str(v[0])+' Resto_Rating '+str(v[1])+' Resto_Address '+str(v[2])+' Resto_Price '+str(v[3])+'\n'
                return r
        
        def mail(x,y):
            EMAIL_ADDRESS = 'Enter your email'
            EMAIL_PASSWORD = 'Enter your email pass'

            

            msg = EmailMessage()
            msg['Subject'] = 'list of top restaurants'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = y

            msg.set_content(filterprice(x))
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            
        mail(p,e)
        
        dispatcher.utter_message("-----"+'list of restaurants has been send to '+e) 
         
          
        

    
    
