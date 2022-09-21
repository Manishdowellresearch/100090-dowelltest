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


### reports
- api to get names:
    `https://100055.pythonanywhere.com/api/report/candidate_name/`
- api to get task :
    `https://100055.pythonanywhere.com/api/jobs/get_tasks/`
    -  product subproduct name title description

- collection(need to complete)
```json
{
    "name":"divya",
    "Product":"hr-hiring",
    "sub-product":"hring",
},
{
    "name":"Ayoo",
    "Product":"hr-hiring",
    "sub-product":"hring",
},
{
    "name":"Manish",
    "project":"hr-hiring",
    "sub-product":"community",
},
```

- product : Hr-hiring

    - hiring
        - divya
        - ayoo


