## Database logic for permutation calculator :

### logic for saving data to db
- logic data
```json
{
    "eventId":"call event fuction", 
    "username": "get the user name from the login function",
    "permutation_data": {
        "value_of_n":{
            "eventId":"call event fuction",
            "n":"user input for n"
        },
        "value_of_r":{
            "eventId":"call event fuction",
            "r":"user input for r"
        },
        "selected_variable_for_pemutation":{
            "eventId":"call event fuction",
            "variable":"selected variable from keyboard"
        },
        "first_user_selection":{
            "eventId":"call event fuction",
            "first_variable":"the first variable that user select from the selected_variable_for_pemutation stage",
            "Permutation_result":"the first permutation result",
            "Result":"result"
        },
        "second_user_selection":{
            "eventId":"call event fuction",
            "second_variable":"the second variable that user select from the selected_variable_for_pemutation stage",
            "Permutation_result":"there will be two permutation",
            "user_selection_from_premutation_result":"what user will select from the two permutation from Permutation_result",
            "Result":"result"
        },
        "Result":{
            "eventId":"call event fuction",
            "Result":"final result"
        }
    }
}
```


-   let's assume `n=4` and `r=2`
-   example data
```json
{
    "eventId":"call event fuction", 
    "username": "Manish",
    "permutation_data": {
        "value_of_n":{
            "eventId":"call event fuction",
            "n":[
                "4"
            ]
        },
        "value_of_r":{
            "eventId":"call event fuction",
            "r":[
                "2"
            ]
        },
        "selected_variable_for_pemutation":{
            "eventId":"call event fuction",
            "variable":[
                "a",
                "b",
                "c",
                "4"
            ]
        },
        "first_user_selection":{
            "eventId":"call event fuction",
            "first_variable":[
                "a"
            ],
            "Permutation_result":[
                "a"
            ],
            "Result":[
                "a"
            ]
        },
        "second_user_selection":{
            "eventId":"call event fuction",
            "second_variable":[
                "4"
            ],
            "Permutation_result":[
                "a4",
                "4a"
            ],
            "user_selection_from_premutation_result":[
                "4a"
            ],
            "Result":[
                "4a"
            ]
        },
        "Result":{
            "eventId":"call event fuction",
            "Result":[
            "4a"
        ]
        }
    }
}
```


# Documentation for scale api :

##api
```python

@csrf_exempt
def scaleapi(request):
    if request.method == "POST":
        orientation = request.POST.get("orientation")
        numberrating= request.POST.get("numberrating")
        scalecolor= request.POST.get("scalecolor")
        roundcolor= request.POST.get("roundcolor")
        fontcolor= request.POST.get("fontcolor")
        fomat= request.POST.get("fomat")
        time= request.POST.get("time")
        template_name = request.POST.get("template_name")
        name= request.POST.get("name")
        text = request.POST.get("text")
        left = request.POST.get ("left")
        right = request.POST.get("right")
        center = request.POST.get("center") 
        scale_category = request.POST.get("scale_category")
        field ={
            "eventId":get_event_id(),
            "scale_data": {
                "orientation":orientation,"numberrating":numberrating,"scalecolor":scalecolor,
                "roundcolor":roundcolor,"fontcolor":fontcolor,"fomat":fomat,
                "time":time,"template_name":template_name,"name":name,
                "text":text, "left":left,"right":right,"center":center, 
                "scale-category": scale_category}
        }
        inserted_id= dowellconnection("dowellscale","dowellscale","scale_reports","scale_reports","1094","ABCDE","insert",field)
        return JsonResponse({
            "inserted_id": inserted_id,
            "status":"Inserted sucessfully" 
            })

#call dowellevenId and dowellconnection
```
##endpoint url

`https://100090.pythonanywhere.com/scaleapi/scaleapi/`

##api call

`orientation` `numberrating` `scalecolor` `roundcolor` `fontcolor` `fomat` `time` `template_name` `name` `text` `left` `right` `center` `scale-category`




