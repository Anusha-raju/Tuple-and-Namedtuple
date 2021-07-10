import datetime
from faker import Faker
from random import uniform
from collections import namedtuple
from collections import Counter
from statistics import mean
fake = Faker()

def generate_profile(number:int = 10000)->tuple:
    ''' This function creates profiles using the fake method and stores as a list of namedtuple and list of dictionaries'''

    if type(number) != int:
        raise TypeError("Invalid input:number of number should be integer!!!")

    profile_tuple = []
    profile_dict = []
    profile_ = namedtuple('profile_',fake.profile().keys())

    #-----docstrings--
    profile_.birthdate.__doc__ = " This is a birthday in format year month day"
    profile_.current_location.__doc__ = "this is the x and y coordinates of the present location"
    profile_.blood_group.__doc__ = "this is the blood group"

    for _ in range(number):
        data = fake.profile() # creates fake profile
        profile_dict.append(data)
        profile_tuple.append(profile_(**data))

    return profile_dict,profile_tuple



def evaluation(profile_list: 'list')->tuple:
    """ this is a function used to calculate the average age, oldest person
        largest blood type, mean of current location
        INPUT : profile_list: list: a list which contains the profiles in either a namedtuple or dictionary
        OUTPUT : tuple : oldest person age, average age, largest blood type, mean of current location
    """
    today = datetime.date.today()

    #age is a function which calculate the age until the current day
    age = lambda x:today.year - x.year - \
         ((today.month, today.day) <\
         (x.month, x.day))
    if isinstance(profile_list[0], tuple) == True:
        birthdate_ = [_.birthdate for _ in profile_list]
        oldest_person = age(min(birthdate_))

        average = int(sum([age(_) for _ in birthdate_])/len(birthdate_))
        blood_type = max(Counter([_.blood_group for _ in profile_list]))

        mean_x = mean([_.current_location[0] for _ in profile_list])
        mean_y = mean([_.current_location[1] for _ in profile_list])

        return oldest_person, average, blood_type, (mean_x,mean_y)



    elif isinstance(profile_list[0], dict) == True:

        birthdate_ = [x['birthdate'] for x in profile_list]
        oldest_person_age = age(min(birthdate_))

        average = int(sum([age(_) for _ in birthdate_])/len(birthdate_))
        blood_type = max(Counter([x['blood_group'] for x in profile_list]))

        mean_x = mean([x['current_location'][0] for x in profile_list])
        mean_y = mean([x['current_location'][1] for x in profile_list])

        return oldest_person_age,average, blood_type, (mean_x,mean_y)

    else:
        raise TypeError(" Invalid input:please send proper input: input should be a list of namedtuple or dictionary")

def create_stocks(number:int = 100)->'list':
    """ This function creates the stocks of {number} companies"""

    if type(number) != int:
        raise TypeError("Invalid input:number of stocks should be integer!!!")
    companies = []
    stock = namedtuple('stock', 'name symbol open close high weight ')

    #----docstring--
    stock.name.__doc__ = "this is the name of the company"
    stock.symbol.__doc__ = 'this is the symbol of the company'
    stock.open.__doc__ = 'this is the value of the company at the starting of the trade'
    stock.close.__doc__ = 'this is the value of the company at the ending of the trade'
    stock.high.__doc__ = 'this is the highest value of the company during the day'
    stock.weight.__doc__ = "this is the weight assigned to the company"

    for _ in range(number):
         name = fake.company()
         symbol = name.upper()[0:3]

         open_ = round(uniform(10,30000),4)
         close = round(open_ * (uniform(-10,100)/100),4)
         high = round(uniform(open_, (open_+close)),4) if open_>close else close

         weight = round(uniform(10,85),4)

         companies.append(stock(name,symbol,open_,close,high,weight))

    return companies

def stock_market(companies:'list')->tuple:
    """
    This is a function which calculates the value the stock market started at,the highest value during the day, and end value.

    Output: tuple: value the stock market started at,the highest value during the day, and end value.
    """
    if isinstance(companies[0],tuple)!= True:
        raise TypeError("Invalid input:the input should be a list of tuples!!!")

    stock_start = sum([x.open*x.weight for x in companies])
    stock_end = sum([x.close*x.weight for x in companies])
    stock_highest = max([x.high*x.weight for x in companies])

    return stock_start,stock_end,stock_highest
