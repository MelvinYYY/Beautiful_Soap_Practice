# Import module

import pandas as pd 
import numpy as np
import requests 
from bs4 import BeautifulSoup
import pickle
import gc
from time import sleep
import requests
import re

#len(websites)

# Define Function 
def unique_list(links): 
    '''
    Return a unique sub-list 
    '''
    # order preserving
    checked = []

    for link in links:
        if link not in checked:
            checked.append(link)

    return checked

# Retrun list from a website 

def get_list(web):
    '''
    Retrun an MRO list from a website 
    '''
    page = requests.get(str(web)) # Access to the web page 
   
    soup = BeautifulSoup(page.content, 'html.parser')  # Create a BeautifulSoup object
    
    # Return a list that contains all "a herf" object from the soup object
    company_list = soup.find_all("a", class_ = False, href=re.compile("/company/"), text = True)
   
    company_links = [a['href'].strip() for a in company_list] # Get all herf link
    
    company_links = unique_list(company_links) #Return a unique list 
    
    company_links = [link for link in company_links if not ('https' in link)] # Remove irrelevant website 

    return company_links

# # Retrun list from a website 

def get_company_info(web):
    '''
    Retrun company name and zip code from a website 
    '''
    web = 'https://mrolinks.mro-network.com'+str(web)
    page = requests.get(str(web)) # Access to the web page 
   
    soup = BeautifulSoup(page.content, 'html.parser')  # Create a BeautifulSoup object
    
    # Return a list that contains all "a herf" object from the soup object
    company_name = soup.find_all("h1", text = True)[0].text.strip()
    zipcode = soup.find_all("span", {'class': 'postal-code'}, text = True)[0].text.strip()
    
    return company_name, zipcode

