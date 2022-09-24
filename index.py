import os
import requests
import json
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from dotenv import load_dotenv

load_dotenv()

# Twilio API secret
accountSID=os.environ.get('accountSID')
authToken=os.environ.get('authToken')

#NASA API secret
nasaKey=os.environ.get('NASA_API_KEY')

nasaAPOD_URL="https://api.nasa.gov/planetary/apod"
params={'api_key': nasaKey}


client=Client(accountSID, authToken)

try:
    res = requests.get(nasaAPOD_URL, params=params)
    if res.ok:
        response = json.loads(res.text)
        title = response["title"]
        explanation = response["explanation"]
        message = client.messages.create(
            to="+16476745050",
            from_="+16306426546",
            body= f'Today\'s picture is of: {title}! \n\n Description of Photo:\n{explanation}',
            media_url= response["hdurl"]
        )
        print(message.sid)
except TwilioRestException as err:
    print(err)  
except requests.exceptions.RequestException as err:
    print(err)
 