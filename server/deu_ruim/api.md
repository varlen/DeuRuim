<Section: Introduction>
#API
This document describes the API functionality for the  *deu ruim* server   

Functionality will be given on the following format:
URL: domain.address:port/function/still-function/<argument1>/<argument2>
Method: Specifies the HTTP method to be used
Parameters: tells the user what to send on the request

<Section:Functionality>

#Get Stories
* Return the 50 stories that preceed the most recent one, given by <time>

* URL: server-url:port/stories/<time>
* Method: GET
* Parameters 
    time: Time for the most recent request the user wishes to receive
    * Can use time = now for most recent stories

#Create Story
* URL: server-url:port/stories
* Method: POST
* Parameters: 
    The request's data parameter should receive a JSON object that contains the following fields:
    * title       : String
    * description : String
    * location    : List<Int>
    * tags        : List<String>

#Search Stories
* URL: server-url:port/stories/search
* Method: POST
* Parameters:
    The request's data parameter should receive a JSON object that contains the following fields:
    * tags : List<String> 
    

#Disqualify Story
* URL: server-url:port/stories/disqualify
* Method: POST
* Parameters:  
    The request's data parameter should receive a JSON object that contains the following fields:
    * id : Int 
