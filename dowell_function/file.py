import json
from multiprocessing import connection
import requests
import pprint
from population import targeted_population
from connections import connection

#print(connection("dowell is a company"))
print(targeted_population('hr_hiring','accounts_view', ['application_details'],"life_time"))
#productname,subproduct,name
#manish
