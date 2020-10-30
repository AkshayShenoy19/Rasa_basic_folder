## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location    
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}    
    - action_search_restaurants   
    - utter_if_user_wants_email
* send_mail{"receive_email": true}  
    - slot{"receive_email": true}
    - utter_ask_email   
* send_mail{"email": "sdhyg@gmail.com"}   
    - slot{"email": "sdhyg@gmail.com"}
    - check_email
    - slot{"flag_email": true}
    - send_email
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
      
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}    
    - action_search_restaurants
    - utter_if_user_wants_email
* send_mail{"receive_email": true}
    - slot{"receive_email": true}       
    - utter_ask_email
* send_mail{"email": "akki_S89gmail.com"}    
    - slot{"email": "akki_S89gmail.com"}
    - check_email
    - slot{"flag_email": false}
    - utter_if_user_wants_email
* send_mail{"receive_email": "No"}    
    - slot{"receive_email": "No"}  
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"} 
    - action_search_restaurants
    - utter_if_user_wants_email
* send_mail{"receive_email": true}    
    - slot{"receive_email": true}    
    - utter_ask_email
* send_mail{"email": "AkkihY89@yahoo.com"}    
    - slot{"email": "AkkihY89@yahoo.com"}
    - check_email
    - slot{"flag_email": true}
    - send_email 
    - utter_goodbye
    - export

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    
* restaurant_search{"location": "ajmer"}
    - slot{"location": "ajmer"}
    - check_location
    - slot{"check_op": true} 
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"} 
    - action_search_restaurants

    - utter_if_user_wants_email
* send_mail{"receive_email": true}     
    - slot{"receive_email": true}     
    - utter_ask_email
* send_mail{"email": "akki_S89gmail.com"}     
    - slot{"email": "akki_S89gmail.com"}
    - check_email
    - slot{"flag_email": false}
    - utter_incorrect_email
    - utter_if_user_wants_email
* send_mail{"receive_email": true}     
    - slot{"receive_email": true}
    - utter_ask_email
* send_mail{"email": "sdhyg@gmail.com"}     
    - slot{"email": "sdhyg@gmail.com"}
    - check_email
    - slot{"flag_email": true}    
    - send_email
* goodbye
    - utter_goodbye
    - export

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}    
    - action_search_restaurants

    - utter_if_user_wants_email
* send_mail{"receive_email": true}     
    - slot{"receive_email": true}     
    - utter_ask_email
* send_mail{"email": "akki_l.com"}     
    - slot{"email": "akki_l.com"}
    - check_email
    - slot{"flag_email": false}
    - utter_incorrect_email
    - utter_if_user_wants_email 
* send_mail{"receive_email": true}     
    - slot{"receive_email": true}   
    - utter_ask_email
* send_mail{"email": "akki_l@bing.com"}       
    - slot{"email": "akki_l@bing.com"}
    - check_email
    - slot{"flag_email": true}  
    - send_email
    - utter_goodbye
    
    - export


## interactive_story_1A
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"check_op": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}    
    - action_search_restaurants
    - utter_if_user_wants_email
* send_mail{"receive_email": false}    
    - slot{"receive_email": false}     
    - utter_goodbye
    - export


## interactive_story_1B
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"check_op": true} 
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}    
    - action_search_restaurants
    - utter_if_user_wants_email
* send_mail{"receive_email": false}   
    - slot{"receive_email": false}     
    - utter_goodbye
    
    - export

## interactive_story_1C
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op": true} 
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}    
    - action_search_restaurants
    - utter_if_user_wants_email
* send_mail{"receive_email": true}    
    - slot{"receive_email": true}
    - utter_ask_email
* send_mail{"email": "sdhyg@gmail.com"}    
    - slot{"email": "sdhyg@gmail.com"}
    - check_email
    - slot{"flag_email": true}
    - send_email
    - utter_goodbye
    

    - export
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}    
    - action_search_restaurants
    - utter_if_user_wants_email
* send_mail{"receive_email": true}     
    - slot{"receive_email": true}
    - utter_ask_email
* send_mail{"email": "sdhyg@gmail.com"}    
    - slot{"email": "sdhyg@gmail.com"}
    - check_email
    - slot{"flag_email": true}
    - send_email

    - utter_goodbye
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
    
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}    
    - action_search_restaurants
    - utter_if_user_wants_email
* send_mail{"receive_email": true}    
    - slot{"receive_email": true}
    - utter_ask_email
* send_mail{"email": "sdhyg@gmail.com"}    
    - slot{"email": "sdhyg@gmail.com"}
    - check_email
    - slot{"flag_email": true}
    - send_email
    

    - utter_goodbye
    - export

## complete Not availaible
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - slot{"location": "Khopoli"}
    - check_location
    - slot{"check_op": false}

	- utter_we_dont_operate

* goodbye
    - utter_goodbye
    - export   
    
## complete Not availaible 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Dombivali"}   
    - slot{"location": "Dombivali"}
    - check_location
    - slot{"check_op": false} 
	- utter_we_dont_operate

* goodbye
    - utter_goodbye
    - export      
    

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Dombivali"}
    - slot{"location": "Dombivali"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
    - export

## interactive_story_2
* greet
    - utter_greet    
* restaurant_search{"location": "khopoli"}
    - slot{"location": "khopoli"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
    - export
    

## interactive_story_3
* greet
    - utter_greet       
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "khopoli"}    
    - slot{"location": "khopoli"}  
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
    - export
 
 
## interactive_story_4
* greet
    - utter_greet    
* restaurant_search{"cuisine": "Italian", "location": "Shelu"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Shelu"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
    - export

## interactive_story_5
* greet
    - utter_greet    
* restaurant_search{"cuisine": "italian", "location": "kopar"}
    - slot{"cuisine": "italian"}
    - slot{"location": "kopar"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
    - export
    
## interactive_story_6
* greet
    - utter_greet    
* restaurant_search{"location": "dombivali"}
    - slot{"location": "dombivali"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye    
    - export
    
    
    
## interactive_story_6a
* greet
    - utter_greet  
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}   
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true} 
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}    
    - action_search_restaurants    
    
    - utter_if_user_wants_email
* send_mail{"receive_email": true}     
    - slot{"receive_email": true}     
    - utter_ask_email
* send_mail{"email": "akki_S89@gmail.com"}     
    - slot{"email": "akki_S89@gmail.com"}
    - check_email
    - slot{"flag_email": true}
    - send_email
    - utter_goodbye   
    

    - export
    
    
 
## interactive_story_6b
* greet
    - utter_greet  
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"} 
    - utter_ask_location  
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true} 
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}    
    - action_search_restaurants    
    - utter_if_user_wants_email
* send_mail{"receive_email": true}     
    - slot{"receive_email": true}     
    - utter_ask_email
* send_mail{"email": "akki_S89@gmail.com"}     
    - slot{"email": "akki_S89@gmail.com"}
    - check_email
    - slot{"flag_email": true}    
    - send_email

    - utter_goodbye
    - export
        

## interactive_story_b
* greet
    - utter_greet                
* restaurant_search{"location": "sion"}
    - slot{"location": "sion"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
    
    
## interactive_story_c
* greet
    - utter_greet     

* restaurant_search{"cuisine": "north indian", "location": "sion"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "sion"}
    - check_location
    - slot{"check_op": false}
    - utter_goodbye
   
    
## interactive_story_62b
* greet
    - utter_greet     
    
    
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
    
    
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}    
    - action_search_restaurants
    - utter_if_user_wants_email
* send_mail{"receive_email": true}     
    - slot{"receive_email": true}     
    - utter_ask_email
* send_mail{"email": "akkiSh@gmail.com"}     
    - slot{"email": "akkiSh@gmail.com"}
    - check_email
    - slot{"flag_email": true}
    - send_email

    - utter_goodbye
    
    
## interactive_story_62b1
* greet
    - utter_greet     
    
* restaurant_search{"cuisine": "italia", "location": "manpada"}
    - slot{"cuisine": "italia"}
    - slot{"location": "manpada"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye

## interactive_story_62b1da
* greet
    - utter_greet  
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}    
    - action_search_restaurants
    - utter_if_user_wants_email
* send_mail{"receive_email": false}     
    - slot{"receive_email": false}     
    
    - utter_goodbye
    
## interactive
* greet
    - utter_greet      
    
* restaurant_search{"location": "Dadar"}
    - slot{"location": "Dadar"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
    

    
#jhg kj
* greet
    - utter_greet
* restaurant_search{"location": "mira"}
    - slot{"location": "mira"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
    
    
#jhg jf    
* restaurant_search{"location": "thane"}
    - slot{"location": "thane"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
    
#jhg    
* greet
    - utter_greet
* restaurant_search{"location": "bhiwandi"}
    - slot{"location": "bhiwandi"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}    
    - action_search_restaurants
    - utter_if_user_wants_email
* send_mail{"receive_email": false}     
    - slot{"receive_email": false}     
    - utter_goodbye
    
 
## hgf 
    
* greet
    - utter_greet    
* restaurant_search{"location": "Bandra"}
    - slot{"location": "Bandra"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
## hgfj
* greet
    - utter_greet
* restaurant_search{"cuisine": "south", "location": "dharwad"}
    - slot{"cuisine": "south"}
    - slot{"location": "dharwad"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}    
    - action_search_restaurants
    - slot{"location": "dharwad"}
    - utter_if_user_wants_email
* send_mail{"receive_email": false}     
    - slot{"receive_email": false}     
    - utter_goodbye
## adh
   
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "south"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "south"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
## htf
* greet
    - utter_greet    
* restaurant_search{"cuisine": "chinese", "location": "Airoli"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Airoli"}
    - check_location
    - slot{"check_op": false}
    - utter_we_dont_operate
    - utter_goodbye
#jhgu
* greet
    - utter_greet    
* restaurant_search{"cuisine": "italian", "location": "vasai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "vasai"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}    
    - action_search_restaurants
    
    - utter_if_user_wants_email
* send_mail{"receive_email": false}     
    - slot{"receive_email": false}    
    - utter_goodbye
