'''
This module performs string operations in order to return values to the 
educational tutoring assistant

Version: 0.0.1

Functions Avaliable:
    return_string_from_list(input_list) -> String
    split_string(input_string) -> List
    keyword_split(input_list) -> List
    get_equations(input_list) -> List
    build_response(path_list) -> String
'''

def return_string_from_list(input_list):
    
    ret = ''.join(input_list)
    
    return ret

def split_string(input_string):
    '''String -> List
    
    This functin takes an input string, and returns a 
    list of the keywords for further processing
    '''
    ret_list = []
    ret = input_string.split(" ")
    ret_list += ret
    
    return ret_list

def keyword_split(input_list):
    '''List -> List
    
    This function takes the list from the split_string() function
    and returns a list of the keywords
    '''
    
    keywords = ['mass']
    ret_list = []
    
    for item in input_list:
        if item in keywords:
            ret_list.append(item)
        else:
            pass
        
        '''
        try:
            int(item)
        except ValueError:
            pass
        '''
        
    return ret_list

def get_equations(input_list):
    '''List -> List
    
    This function takes the list from the keyword_split() function
    It uses those words to return the names of the functions to be used'''
    
    for item in input_list:
        if item == "mass":
            pass
        elif item == "velocity":
            pass
        else:
            pass
    
    ret_list = None
    return ret_list

def build_response(path_list):
    ''' List -> String
    
    This function takes a list of inputs from the path creation function
    to create the string that will appear to the user.
    '''
    stra = 'mass'
    strb = 'physics'
    a = 'First you must use {}.  Then you must use {}'.format(stra, strb)
    return a 
    for item in path_list:
        pass
    
    ret_string = None
    return ret_string  