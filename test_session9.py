#----- tests for session9.py----------
from session9 import generate_profile,evaluation,stock_market,create_stocks
from random import randint
#import re
import pytest
from decimal import Decimal


#--------tests for question 1 & 2
dict_list,tuple_list = generate_profile()
def test_generate_profile():
    """ This function tests the output of generate_profile function"""
    for i in range(10):
        number =randint(0,100)
        assert dict_list[number]['birthdate'] == tuple_list[number].birthdate, "generate function is messed up!!!!!"
        assert dict_list[number]['blood_group'] == tuple_list[number].blood_group, "generate function is messed up!!!!!"
        assert dict_list[number]['current_location'] == tuple_list[number].current_location, "generate function is messed up!!!!!"

def test_type_of_generate_profile_output():
    """ This function tests the type of output of generate_profile"""

    assert isinstance(dict_list[0], dict) == True, "this should have been a dictionary"
    assert type(dict_list)==list, "this should have been a list!!!"
    assert isinstance(tuple_list[0], tuple) == True,"this should have been a namedtuple type"
    assert type(tuple_list)==list, "this should have been a list!!!"


def test_number_of_profiles_created():
    """ This function tests if it has 10000 profiles"""

    assert len(dict_list) == 10000, "not satisfying the question requirements"
    assert len(tuple_list) == 10000, "not satisfying the question requirements"

def test_evaluation():
    """this function tests the number of outputs of evaluation function for a namedtuple and dict"""

    assert len(evaluation(tuple_list)) == 4 ,"evaluation is not completed...."
    assert len(evaluation(dict_list)) == 4 ,"evaluation is not completed...."


def test_outputs_check():
    """this function tests the outputs of evaluation function for a namedtuple and dict"""

    assert evaluation(tuple_list) == evaluation(dict_list) , "evaluation is messed!!!"


def test_output_types_tuples():
    """ This function tests the outputs types of evaluation funtion for namedtuple"""

    assert type(evaluation(tuple_list)[0]) == int , "age should be integer"
    assert type(evaluation(tuple_list)[1]) == int , 'average age should also be integer'
    assert type(evaluation(tuple_list)[2]) == str, 'blood group should be a string'
    assert isinstance(evaluation(tuple_list)[3][0],Decimal), 'mean of current location should be decimal'
    assert isinstance(evaluation(tuple_list)[3][1],Decimal), 'mean of current location should be decimal'

def test_output_types_dictionary():
    """ This function tests the outputs types of evaluation funtion for dictionary"""

    assert type(evaluation(dict_list)[0]) == int , "age should be integer"
    assert type(evaluation(dict_list)[1]) == int , 'average age should also be integer'
    assert type(evaluation(dict_list)[2]) == str, 'blood group should be a string'
    assert isinstance(evaluation(dict_list)[3][0],Decimal), 'mean of current location should be decimal'
    assert isinstance(evaluation(dict_list)[3][1],Decimal), 'mean of current location should be decimal'


def test_validation_output_blood_group():
    """ this function tests the validation of ouputs(blood group) of evaluation function"""
    blood_type =['A-','A+','B-','B+','AB-','AB+','O-','O+']
    assert evaluation(tuple_list)[2] in blood_type, "blood group is invalid"
    assert evaluation(dict_list)[2] in blood_type, "blood group is invalid"

def test_validation_oldest_person_age_output():
    """ this function tests the validation of ouputs(oldest person age) of evaluation function"""

    #122 is the oldest person's age till known

    assert evaluation(tuple_list)[0] < 130, "humans can't live for ever"
    assert evaluation(dict_list)[0] < 130, "humans can't live for ever"


def test_evaluation_for_type_errors():
    """this function tests the evaluation function for typeerror message for invalid input"""

    with pytest.raises(TypeError, match=r".*Invalid input*"):
        evaluation('list of tuples')



######-----------tests for stock market--------

stock_list = create_stocks()

def test_stock_market_invalid_input():
    """this function tests the stock market function for typeerror message for invalid input"""

    with pytest.raises(TypeError, match=r".*Invalid input*"):
        stock_market('list')


def test_stock_market_len():
    """ This function tests for the length of ouput of stock market"""


    assert len(stock_market(stock_list)) == 3, "not satisfying the question requirement..."


def test_stock_market_output_type():
    """This function tests the output types of stock market"""


    assert type(stock_market(stock_list)[0]) == float, "stock start is not right"
    assert type(stock_market(stock_list)[1]) == float, "stock start is not right"
    assert type(stock_market(stock_list)[2]) == float, "stock start is not right"


def test_create_stocks():
    """ This function checks the type of output of create stocks"""
    assert isinstance(stock_list[0], tuple) == True, "the list is invalid"


def test_create_stocks_invalid_input():
    """this function tests the create stock function for typeerror message for invalid input"""

    with pytest.raises(TypeError, match=r".*Invalid input*"):
        stock_market('number')


def test_create_stocks_len():
    """ This function tests the create stocks function"""

    assert len(create_stocks(100)) == 100, "not satisfying the question requirement..."

def test_highest_value():
    """This function tests if highest is really high"""

    assert max([i.high for i in stock_list]) <= stock_market(stock_list)[2], " high is not really yhe highest"

def test_open_high():
    """This function tests if open is greater than high"""

    assert any([i.high>=i.open for i in stock_list]), "high should be the highest value"

def test_close_high():
    """This function tests if close is greater than high"""

    assert any([i.high>=i.close for i in stock_list]), "high should be the highest value"


def test_fields():
    """this function tests the fields of the stock"""

    assert stock_list[0]._fields