## intent:affirm
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- Thanks
- going good

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hola

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bengaluru](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [bengaluru](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- find me hotels in [bhiwandi](location)
- [Dombivali](location)
- [khopoli](location)
- Find me some [Italian](cuisine) restaurants in [shelu](location)
- Find me [Italian](cuisine) restaurants in [Shelu](location)
- Find me [italian](cuisine) restaurants in [kopar](location)
- dhaba in [dombivali](location)
- [kalwa](location) restaurants
- [Diva](location) Hotels
- find me hotel in [sion](location)
- [north indian](cuisine) restaurants in [sion](location)
- [south indian](cuisine) restaurants
- [delhi]{"entity": "location", "value": "Delhi"}
- [italia](cuisine) resto in [manpada](location)
- [bangalore](location)
- [Dadar](location) restaurants
- [mira](location) road hotel
- nearby [thane](location)
- find me places to eat near [bhiwandi](location)
- [Bandra](location)
- [south](cuisine) restraints near [hubli-dharwad](location)
- [south](cuisine) restraints near [hubli](location)-[dharwad](location)
- [south indian](cuisine) resto in [south](location)
- [chines]{"entity": "cuisine", "value": "chinese"} restraints in [Airoli](location)
- [italian](cuisine) resto in [vasai](location)
- show me a hotel nearby [vasai](location)-[virar](location) city
- can you understand this [acbhdscbyusjd37qw3yr](location)
- [chinese](cuisine) resto
- [bengaluru](location)
- [Italian](cuisine) dish near [warangal](location)
- [kolkata](location)
- i want something to eat in [italian](cuisine) near [mumbai](location)
- [aurangabad](location)
- [Borivali](location)
- hello bot i am hungry can you search a [north indian](cuisine) restaurant in [bIkaNer](location) ?
- list a few restaurants in chandni [nagar](location)
- hi can you find me [north indian](cuisine) resto in [bhubaneswar](location)
- can you find me something [mexican](cuisine) to eat in [chennai](location) and send mail to [akki@jio.com](email)
- [low](price)
- [mid](price)
- [high](price)
- [cheap]{"entity": "price", "value": "low"}
- [affordable]{"entity": "price", "value": "low"}


## intent:send_mail
- [sdhyg@gmail.com](email)
- [AkkihY89@yahoo.com](email)
- [voila@hotmail.com](email)
- [akkiSh@gmail.com](email)
- [aks@gmailcom](email)
- [fvjn3.gcom](email)
- [akki123@bing.com](email)
- [xyz@sth.edu](email)
- [jddk.2jmd@kdl.co.in](email)
- [akkiSh@gmail.edu](email)
- [akkiSh@gmail.ai](email)
- [akkiSh@gmail.co.in](email)

## synonym:kolkata
- calcutta
- kalkata
- kalcutta
- Calcutta
- Kalkata
- Kalcutta

## synonym:indore
- Indor
- Indur
- indor
- indur

## synonym:pune
- poona
- Poona

## synonym:4
- four

## synonym:Delhi
- New Delhi
- delhi
- Dilli

## synonym:vadodara
- Baroda
- barodara

## synonym:bengaluru
- bengaluru
- Bengaluru
- Banglor
- bengalore
- Bengalore
- Bangalore

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:italian
- italia
- Italian

## synonym:american
- American

## synonym:mexican
- Mexican
- mexica
- mexicn

## synonym:hubli–dharwad
- hubli
- dharwad
- Hubli
- Dharwad

## synonym:mid
- moderate
- medium

## synonym:low
- cheap
- affordable

## synonym:mumbai
- bambai
- bombay
- Bombay
- Bambai

## synonym:thiruvananthapuram
- Trivandrum
- trivandrum
- trivandum
- Trivandum

## synonym:kozhikode
- calicut
- Calicut

## synonym:guwahati
- Gauhati
- gauhati

## synonym:jabalpur
- jubulpur
- jabulpur

## synonym:thanjavur
- Tanjore
- tanjore

## synonym:varanasi
- banaras
- banarus
- Banaras
- Banarus

## synonym:visakhapatnam
- vishakapatnum
- Vishakapatnum
- 
## synonym:chennai
- madras
- Madras

## synonym:kochi
- Cochin
- cochin

## synonym:prayagraj
- Allahabad 
- allahabad 
- Prayagraj

## synonym:vasai-virar city
- virar
- vasai
- Vasai
- Virar

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
