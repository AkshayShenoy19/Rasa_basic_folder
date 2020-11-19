# Rasa Chatbot Case Study
 An Indian startup named 'Foodie' wants a conversational bot (chatbot) which can help 
 users discover restaurants across several Indian cities. 

# Roadmap
-[x] Installation of Rasa and supporting packages
-[x] Basic Running of the project
-[x] Complete City related requirements
-[ ] Complete Cuisine related requirements
-[ ] Complete budget related requirements
-[ ] Complete Email related requirements
-[ ] Complete Display Result related requirements
-[ ] Complete Email Result related requirements
-[ ] Total 40-50 stories with the every scenarios

-[x] Resolve the interpolation error
-[x] Change the Price Title
-[x] Add the two people price stuff in result
-[x] Change the email result function
-[x] Filtered top 5 restaurant on base of price display 
-[ ] Resolve the filtering restaurant function

# Problem Statement
The main purpose of the bot is to help users discover restaurants quickly and efficiently 
and to provide a good restaurant discovery experience. 

## Details
Following are the input taken from the users:
1. **City** 
2. **Cuisine Preference** 
3. **Average budget for two people** 
4. **Email** 

Following are the requirements to be considered:
1. **City:** Assume that Foodie works only in Tier-1 and Tier-2 cities. So other than those 
cities the bot should report that "We do not operate in that area yet".
2. **City:** The bot should be able to identify common synonyms of city names, such as Bangalore
/Bengaluru, Mumbai/Bombay etc.
3. **Cuisine Preference:** The bot should list out the following six cuisine categories (Chinese, 
Mexican, Italian, American, South Indian & North Indian) & the customer can select any one out of that.
4. **Average budget for two people:** Segment the price range (average budget for two people) into 
three price categories: lesser than 300, 300 to 700 and more than 700. Bot should ask the user to 
select one of the three price categories. 
5. **Email:** The bot should ask the user whether he/she wants the details of the top 10 
restaurants on email. If the user replies 'yes', the bot should ask for user’s email id and 
then send it over email. Else, just reply with a 'goodbye' message.
6. **Display Result:** While showing the results to the user, the bot should display the top 5 
restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 
5 being the highest). 
The format should be: {restaurant_name} in {restaurant_address} has been rated {rating}.
7. **Email Result:**  The mail should have the following details for each restaurant: 
-Restaurant Name -Restaurant locality address -Average budget for two people -Zomato user rating

# Conversation Example
User: Hola

Bot: Hi there! How may I help you?

User: I’m hungry. Looking out for some good restaurants

Bot: In what location?

User: bengaluru

Bot: What kind of cuisine would you like to have?
1. Chinese
2. Mexican
3. Italian
4. American
5. Thai
6. North Indian

User: I’ll prefer thai

Bot: What's the average budget for two people?
1. Lesser than Rs. 300
2. Rs. 300 to 700
3. More than 700

User: 300-700 range

Bot: Showing you top rated restaurants:
1. Restaurant 1 in Area 1. And the average price for two people here is: XXX
Rs
2. Restaurant 1 in Area 1. And the average price for two people here is: XXX
Rs
3. .
4. .
5. .

Bot: Should I send you details of all the restaurants on email?

User: yes. Please send it to ahbcdj@dkj.com

Bot: Sent

# Installation
Python==3.7
Rasa==2.0.0
Spacy==2.2.4
Other program installed version details can be found in the requirements.txt file.

# Authors 
Akshay Shenoy and Kalpesh 

# Issues
-[ ] Nagar is detecting as a city and Banglore location restaurants are showing.

