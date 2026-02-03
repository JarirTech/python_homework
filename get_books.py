from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Task 3: Write a Program to Extract this Data

#4.Within that element, find the element that stores the title.  Note the tag type and the class value.  Your program will need this value too, so save it too.
#'.cp-search-result-item'
#li.row.cp-search-result-item
#  search_results_link = 'li[class="row cp-search-result-item"]'
#"span.title-content
#'//span[@class ="title-content" and text()="Learning Spanish-beginner I"]'
#5.Within the search results li element, find the element that stores the author
##'a.author-link'
#'a[target="_parent"'
#find.elements(By.XPATH, '//a[@class = "author-link"]')


#2.Add code to load the web page given in task 2.



try:
    driver.get('https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart')
    sleep(3)
#3.Find all the li elements in that page for the search list results.
    li_list = driver.find_elements(By.CSS_SELECTOR, 'li[class="row cp-search-result-item"]')
    
#4.Within your program, create an empty list called results    
    results=[]

#5.Main loop: You iterate through the list of li entries. 
#dict that stores these values, with the keys being Title, Author, and Format-Year.  
# Then append that dict to your results list.
    book_items = driver.find_elements(By.CSS_SELECTOR, "li.cp-search-result-item")

    for book in book_items:

        # Title:
        title = ""
        try:
            title_el = book.find_element(By.CSS_SELECTOR, "span.title-content")
            title = title_el.text.strip()
        except:
            pass

        # Author:
        author_elements = book.find_elements(By.CSS_SELECTOR, "a.author-link")
        authors = [a.text.strip() for a in author_elements if a.text.strip()]
        author_text = "; ".join(authors)

        # Year:#'div.cp-format-info'
        format_year = ""
        try:
            format_year_el = book.find_element(
                By.CSS_SELECTOR, "span.display-info-primary"
            )
            format_year = format_year_el.text.strip()
        except:
            pass

        # ---- Store result ----
        results.append({
            "Title": title,
            "Author": author_text,
            "Format-Year": format_year
        })



except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")
finally:
    driver.quit()
##6.Create a DataFrame from this list of dicts.  Print the DataFrame.

df = pd.DataFrame(results)
print(df)

#----------------------------------------------------------------------------
#Task 4: Write out the Data    
#4.1.Write the DataFrame to a file called get_books.csv, within the assignment8 folder

df.to_csv("assignment8/get_books.csv", index=False)

#4.2.Write the results list out to a file called get_books.json, also within the assignment8 folder

with open("assignment8/get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)
