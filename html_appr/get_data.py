# Importing requited libraries
from selenium import webdriver
import time
import os
import requests
from bs4 import BeautifulSoup

# Setting Chrome Browser User-Agent to avoid robot error.
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.2490.71 Safari/537.36"

# Loading selenium web driver for chrome
# browser = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), 'chromedriver'))
"""
URLs
{
"firm_url": "https://www.adviserinfo.sec.gov/Firm/105958",
"view_form_adv_section": "https://www.adviserinfo.sec.gov/IAPD/crd_iapd_AdvVersionSelector.aspx?ORG_PK=105958",
"form_adv": {
            "item1": "
            }
}
"""


def load_page(url):
    """
    Load web page from given url
    :param url: url
    :return: webpage
    """
    return requests.get(url, headers={"User-Agent": user_agent})


def parse_page(html_page):
    """
    Convert html text data into readable html obj.
    :param html_page: webpage
    :return soup object (parsed html data)
    """
    assert html_page.ok
    return BeautifulSoup(html_page.content, 'html.parser')


def firm_page():
    pass


def item1():
    """
    Item 1 Identifying Information
    Data can be collected: idCRD, nameEntityManagerBusiness, nameEntityManagerLegal, idSEC, nameEntityManager,
                            addressOfficePrimary, addressStreet1OfficePrimary, cityOfficePrimary, stateOfficePrimary,
                            countryOfficePrimary, zipcodeOfficePrimary, phoneOfficePrimary, faxOfficePrimary, countOfficesOther,
                            addressStreet1OfficeMail, addressStreet2OfficeMail, cityOfficeMail, StateOfficeMail, countryOfficeMail,
                            zipcodeOfficeMail,
    """
    pass


def item2():
    """Item 2 SEC Registration/Reporting"""
    pass


def item3():
    """Item 3 Form Of Organization"""
    pass


def item4():
    """Item 4 Successions"""
    pass


def item5():
    """Item 5 Information About Your Advisory Business"""
    pass


def item6():
    """Item 6 Other Business Activities"""
    pass


def item7a():
    """Item 7.A Financial Industry Affiliations"""
    pass


def item7b():
    """Item 7.B Private Fund Reporting"""
    pass


def item8():
    """Item 8 Participation or Interest in Client Transactions"""
    pass


def item9():
    """Item 9 Custody"""
    pass


def item10():
    """Item 10 Control Persons"""
    pass


def item11():
    """Item 11 Disclosure Information"""
    pass


def item12():
    """Item 12 Small businesses"""
    pass


def main():
    # collecting data into dictionary
    firm_summary = dict()
    url = "https://www.adviserinfo.sec.gov/Firm/105958"

    # Loading column names
    col_names = open('column_names.txt', 'r').read()
    col_names = col_names.split("\n")

    # Loading data for Item 1: Identifying Information
    # No. of Columns can be covered into this page are
    #
    url = "https://www.adviserinfo.sec.gov/IAPD/content/viewform/adv/sections/iapd_AdvIdentifyingInfoSection.aspx?ORG_PK=105958&FLNG_PK=042DAD26000801A505928B5101E87205056C8CC0"
    response = load_page(url)
    soup = parse_page(response)

    # idCRD
    firm_summary[col_names[1]] = soup.find(id="ctl00_ctl00_cphMainContent_ucADVHeader_lblCrdNumber").text

    # nameEntityManagerBusiness
    firm_summary[col_names[2]] = soup.find(
        id="ctl00_ctl00_cphMainContent_cphAdvFormContent_IdentInfoPHSection_ctl00_lblPrimaryName").text

    # nameEntityManagerLegal
    firm_summary[col_names[3]] = soup.find(
        id="ctl00_ctl00_cphMainContent_cphAdvFormContent_IdentInfoPHSection_ctl00_lblFullLegalName").text

    # idRegionSEC - not able to find in document
    firm_summary[col_names[5]] = None

    # idSEC
    firm_summary[col_names[5]] = soup.find("")


if '__name__' == '__main__':
    pass
