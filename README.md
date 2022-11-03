## Database logic for permutation calculator :

1. what is the value of n = 5
2. what is the value of r = 3
3. calculate the permutation = (?)
4. selcte n=5 variable from keyboard = ['a','b','2','e','%']
5. select r=3 variable from 4th step = ['a','2','%']
now main logic :

```json

{
    "Clicked_variable": ['a'],
    "Permutation_result":['a'],
    "final_result":['a']
}

{
    "Clicked_variable": ['%'],
    "Permutation_result":['a%','%a'], 
    "final_result":['a%']
}
Note :permutation_result will calculate with final_result

{
    "Clicked_variable": ['2'],
    "Permutation_result":['2a%','%2a','%a2], 
    "final_result":['%2a']
}
```


