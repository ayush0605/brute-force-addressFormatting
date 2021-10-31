# AddressFormatting

## Introduction


## Steps to run
Clone the repo and resolve dependencies.

1. Run command ```python app.py``` and the server will start on ```http://localhost:5000/```
2. The endpoint of API is ```/address``` and ```/addressLang```.

## About the API
The API has two POST method one with ```/address``` as endpoint and other with ```/addressLang``` as endpoint. The ```/addressLang``` endpoint Formats the address for the input by considering language code as well (It expects langcode in JSON. If langcode is not provided then it considers it as english). 

1. The API has POST method with ```/address``` as endpoint. It takes JSON input as given below:
    ```
    {
     "house": "#15b new gangama chart street",
     "street": "mothi nagar",
     "landmark": "",
     "locality": "mothinagar",
     "vtc": "Bangalore North",
     "district": "Bangalore",
     "state": "Karnataka",
     "pincode": "1",
     "sub district": ""
    }
  ```
  ```
2. The API has POST method with ```/addressLang``` as endpoint. It takes JSON input as given below:
    ```
    {
        "house": "#15बी नया गंगामा चार्ट स्ट्रीट",
        "street": "मोती नगर",
        "landmark": "",
        "locality": "मोतीनगर",
        "vtc": "बैंगलोर उत्तर",
        "district": "बैंगलोर",
        "state": "कर्नाटक",
        "pincode": "1",
        "sub district": "",
        "langcode": "06"
    }
    
  ```  

3. The content type of API is application/json. It returns JSON with merged fields (if required).
  
  ```
  ```
  {
    "district": "Bangalore",
    "house": "#15b new gangama chart street",
    "landmark": "",
    "locality": "",
    "pincode": "1",
    "state": "Karnataka",
    "street": "mothi nagar",
    "subdistrict": "",
    "vtc": "Bangalore North"
  }
  ```
  
  ## Deployed API
  The API is deployed on heroku. The url is : ```https://brute-force-address.herokuapp.com/```. The endpoint is ```/address``` and ```/addressLang```.
  
  ## addressLang API
  The below images shows input and output for the addressLang API tested using postman.
  
  Input to addressLang API. 
  ![image](https://user-images.githubusercontent.com/40767716/139588037-82d8235c-24a3-47c1-a5f6-fb7bdea2d775.png)

  Output 
  ![image](https://user-images.githubusercontent.com/40767716/139588064-43d1f62c-1648-40c4-a467-ab371fcdb6eb.png)

