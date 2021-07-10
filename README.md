# Session9 

## TOPIC : Tuple and Namedtuple



#### ASSIGNMENT

1. Use the Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age (add proper doc-strings).  (including 5 test cases)
2. Do the same thing above using a dictionary. Prove that namedtuple is faster.  (including 5 test cases)
3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. 





#### SOLUTION

***generate_profile***: This function creates profiles using the fake method and stores as a list of namedtuple and list of dictionaries

```
def generate_profile(number:int = 10000)->tuple:
    ''' This function creates profiles using the fake method and stores as a list of namedtuple and list of dictionaries'''
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
```





***evaluation***: this is a function used to calculate the average age, oldest person largest blood type, mean of current location

```
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
```



***create_stocks***: This function creates the stocks of {number} companies.



Here ***stock*** is a ***namedtuple*** with fields **name**: name of the company, **symbol**:symbol of the company, **open**: starting value of the company at the start of trade,**close**: end value of the company at the end of the trade, **high** : highest value of the company during the day,**weight** :weight assigned to the company

```
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
```



***stock_market***: calculates the value the stock market started at --> **stock_start**,the highest value during the day--> **stock_highest**, and end value --> **stock_end**.



```
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

```





***Test cases***

|                  Tests                   |                        Functionality                         |
| :--------------------------------------: | :----------------------------------------------------------: |
|          test_generate_profile           | This function tests the output of generate_profile function  |
|   test_type_of_generate_profile_output   |  This function tests the type of output of generate_profile  |
|     test_number_of_profiles_created      |         This function tests if it has 10000 profiles         |
|             test_evaluation              | this function tests the number of outputs of evaluation function for a namedtuple and dict |
|            test_outputs_check            | this function tests the outputs of evaluation function for a namedtuple and dict |
|         test_output_types_tuples         | This function tests the outputs types of evaluation funtion for namedtuple |
|       test_output_types_dictionary       | This function tests the outputs types of evaluation funtion for dictionary |
|    test_validation_output_blood_group    | this function tests the validation of ouputs(blood group) of evaluation function |
| test_validation_oldest_person_age_output | this function tests the validation of ouputs(oldest person age) of evaluation function |
|     test_evaluation_for_type_errors      | this function tests the evaluation function for typeerror message for invalid input |
|     test_stock_market_invalid_input      | this function tests the stock market function for typeerror message for invalid input |
|          test_stock_market_len           | This function tests for the length of ouput of stock market  |
|      test_stock_market_output_type       |     This function tests the output types of stock market     |
|            test_create_stocks            |   This function checks the type of output of create stocks   |
|     test_create_stocks_invalid_input     | this function tests the create stock function for typeerror message for invalid input |
|          test_create_stocks_len          |        This function tests the create stocks function        |
|            test_highest_value            |        This function tests if highest is really high         |
|              test_open_high              |       This function tests if open is greater than high       |
|             test_close_high              |      This function tests if close is greater than high       |
|               test_fields                |         this function tests the fields of the stock          |



 *Author*

*Name*: **ANUSHA**