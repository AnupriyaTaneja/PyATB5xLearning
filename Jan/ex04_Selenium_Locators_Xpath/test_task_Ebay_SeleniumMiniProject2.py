# Open the Url - www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067
# Search for the Macmini
# Click on the search ICON
# Get all the titles
# Get all the prices
# Print all the titles and prices in the end.
#------------------------------------------------------


from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_get_title_price():
    #    chrome_options = Options()
    #    my_driver = webdriver.Chrome(chrome_options)
    my_driver = webdriver.Chrome()

    # <input data-marko="{&quot;oninput&quot;:&quot;handleTextUpdate s0-1-4-13-4 false&quot;
    # ,&quot;onfocusin&quot;:&quot;handleMarkTimer s0-1-4-13-4 false&quot;,&quot;onkeydown&quot;
    # :&quot;handleMarkTimer s0-1-4-13-4 false&quot;}" data-marko-key="@input s0-1-4-13-4" id="gh-ac"
    # class="gh-search-input gh-tb ui-autocomplete-input ui-autocomplete-loading" title="Search"
    # type="text" placeholder="Search for anything" aria-autocomplete="list" aria-expanded="false" size="50"
    # maxlength="300" aria-label="Search for anything" name="_nkw" autocapitalize="off" autocorrect="off"
    # spellcheck="false" autocomplete="off" aria-haspopup="true" role="combobox" tabindex="4" aria-owns="ui-id-1">

    my_driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    time.sleep(3)
    my_element = my_driver.find_element(By.CSS_SELECTOR, "input[placeholder *='Search for anything']")
    my_element.click()
    my_element.send_keys("Macmini")
    my_element.click()
    time.sleep(3)

    search_button = my_driver.find_element(By.XPATH, "//button[@class='gh-search-button btn btn--primary']")
    search_button.click()
    time.sleep(3)

# <button data-marko="{&quot;onclick&quot;:&quot;handleClick s0-1-4-13-8-@btn false&quot;,&quot;
# onkeydown&quot;:&quot;handleKeydown s0-1-4-13-8-@btn
# false&quot;,&quot;onfocus&quot;:&quot;handleFocus s0-1-4-13-8-@btn false&quot;,&quot;onblur&quot;
# :&quot;handleBlur s0-1-4-13-8-@btn false&quot;}" class="gh-search-button btn btn--primary"
# data-ebayui="" type="submit" id="gh-search-btn" role="button" value="Search" tabindex="6">
# <span class="gh-search-button__label">Search</span><svg data-marko-key="@svg s0-1-4-13-8-@btn-7-2-0"
# class="gh-search-button__icon icon icon--24" focusable="false" aria-hidden="true"><use href="#icon-search-24">
# </use></svg></button>

    list_of_items = my_driver.find_elements(By.XPATH, "//div[@class = 's-item__title']")
    list_of_item_prices = my_driver.find_elements(By.CSS_SELECTOR, ".s-item__price")
    print("Total items available on this page: ", len(list_of_items))

    print("Listing all products with their prices: ")
    # Combining two lists using zip function and then iterating through it
    for item, price in (list(zip(list_of_items,list_of_item_prices))):
       print(item.text)
       print(price.text)
       # print(f"Product Name: ", item.text)
       # print(f" and its price: ", price.text)
       # print("--------")

    my_driver.quit()





    #print(" and its price: ")
    #list_of_item_prices = my_driver.find_elements(By.CSS_SELECTOR, ".s-item__price")
    #print(item_price)
    #print("-----------")
    '''
    for i in list_of_items:
        print(i.text)
        #print("Product Name: ",i.text)
        #print(" and its price: ")
        #for j in list_of_item_prices:
        #    print(j.text)
        #print("-----------")

    for j in list_of_item_prices:
        print(j.text)
     '''

    '''
    i= 0
    j= 0
    while i<len(list_of_items):
        print("Product Name: ",str(list_of_items[i]))#i.text)
        print(" and its price: ")
        while j<len(list_of_item_prices):
            j==i
            print(str(list_of_item_prices[j]))
            j=j+1
        i=i+1
              
'''




# <span role="heading" aria-level="3">
# <!--F#f_0-->Mac mini, Intel i5, 128GB SSD, 256GB SSD, 512GB SSD, 8GB RAM, 16GB RAM<!--F/--></span>
