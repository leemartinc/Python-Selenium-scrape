#!/usr/bin/python36
from urllib.request import urlopen as uReq
import urllib.request
from bs4 import BeautifulSoup as soup

from selenium import webdriver
#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import itertools 

import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import time

#returns json


def DCBgogogo():

    url = "REDACTED"
    username = "aoc"
    password = "aoc"
    xpaths = { 'usernameTxtBox' : "//input[@name='j_username']",
            'passwordTxtBox' : "//input[@name='j_password']",
            'submitButton' :   "/html/body/div[2]/div/form/div[2]/button",
            'dcbPercentages': "/html/body/div[4]/div[3]/div/div[3]/div/div/div[6]"
            }

    mydriver = webdriver.Firefox()
    mydriver.get(url)
    #mydriver.maximize_window()

    
    #Clear Username TextBox if already allowed "Remember Me" 
    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

    #Write Username in Username TextBox
    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

    #Clear Password TextBox if already allowed "Remember Me" 
    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

    #Write Password in password TextBox
    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

    #Click Login button
    mydriver.find_element_by_xpath(xpaths['submitButton']).click()

    time.sleep(5)
    flumeHolder =  mydriver.find_element_by_xpath(xpaths['dcbPercentages'])
    for span in flumeHolder.find_elements_by_css_selector('span'):
        for (raw_title, raw_perecent) in zip(span.find_elements_by_css_selector('span'), span.find_elements_by_css_selector('strong')):
            title = raw_title.get_attribute('innerHTML')
            perecent = raw_perecent.get_attribute('innerHTML')

            print(title)
            print(perecent)


    mydriver.quit()
    print("DCB Script complete...")

def DCAgogogo():
    url = "REDACTED"
    username = "aoc"
    password = "aoc"
    xpaths = { 'usernameTxtBox' : "//input[@name='j_username']",
            'passwordTxtBox' : "//input[@name='j_password']",
            'submitButton' :   "/html/body/div[2]/div/form/div[2]/button",
            'dcaPercentages1' : "/html/body/div[4]/div[3]/div/div[3]/div/div[1]/div[6]",
            'dcaPercentages2' : "/html/body/div[4]/div[3]/div/div[3]/div/div[2]/div[6]",
            'dcaPercentages3' : "/html/body/div[4]/div[3]/div/div[3]/div/div[3]/div[6]"
            }

    mydriver = webdriver.Firefox()
    mydriver.get(url)
    #mydriver.maximize_window()

    
    #Clear Username TextBox if already allowed "Remember Me" 
    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

    #Write Username in Username TextBox
    mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

    #Clear Password TextBox if already allowed "Remember Me" 
    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

    #Write Password in password TextBox
    mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

    #Click Login button
    mydriver.find_element_by_xpath(xpaths['submitButton']).click()

    time.sleep(5)
    flumeHolder =  mydriver.find_element_by_xpath(xpaths['dcaPercentages1'])
    for span in flumeHolder.find_elements_by_css_selector('span'):
        for (raw_title, raw_perecent) in zip(span.find_elements_by_css_selector('span'), span.find_elements_by_css_selector('strong')):
            title = raw_title.get_attribute('innerHTML')
            perecent = raw_perecent.get_attribute('innerHTML')

            print(title)
            print(perecent)

    flumeHolder =  mydriver.find_element_by_xpath(xpaths['dcaPercentages2'])
    for span in flumeHolder.find_elements_by_css_selector('span'):
        for (raw_title, raw_perecent) in zip(span.find_elements_by_css_selector('span'), span.find_elements_by_css_selector('strong')):
            title = raw_title.get_attribute('innerHTML')
            perecent = raw_perecent.get_attribute('innerHTML')

            print(title)
            print(perecent)


    flumeHolder =  mydriver.find_element_by_xpath(xpaths['dcaPercentages3'])
    for span in flumeHolder.find_elements_by_css_selector('span'):
        for (raw_title, raw_perecent) in zip(span.find_elements_by_css_selector('span'), span.find_elements_by_css_selector('strong')):
            title = raw_title.get_attribute('innerHTML')
            perecent = raw_perecent.get_attribute('innerHTML')

            print(title)
            print(perecent)


    mydriver.quit()
    print("DCA Script complete...")

DCAgogogo()
DCBgogogo()
