# AddressFormatting

## Introduction

## Steps to run
Clone the repo and resolve dependencies.

1. Run command ```python app.py``` and the server will start on ```http://localhost:5000/```
2. The endpoint of API is ```/address```

## About the API
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

2. The content type of API is application/json. It returns JSON with merged fields (if required).
  
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
  The API is deployed on heroku. The url is : ```https://brute-force-address.herokuapp.com/```. The endpoint is ```/address```
