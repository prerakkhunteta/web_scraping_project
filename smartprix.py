import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

s = Service('c:/Users/prera/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=s)
wait = WebDriverWait(driver, 10)  # 10 seconds timeout

# Maximize window to ensure all elements are clickable
driver.maximize_window()

driver.get('https://www.smartprix.com/mobiles')

# Wait for and click the first checkbox
first_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')))
first_checkbox.click()

# Wait for and click the second checkbox
second_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input')))
second_checkbox.click()

# Wait for the page to load initial content
time.sleep(3)

# Function to scroll to bottom
def scroll_to_bottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Function to get page height
def get_page_height():
    return driver.execute_script("return document.body.scrollHeight")

# Initial height
scroll_to_bottom()
old_height = get_page_height()
print(f"Initial height: {old_height}")

retry_count = 0
max_retries = 3
same_height_count = 0

while True:
    try:
        # Scroll to bottom before clicking load more
        scroll_to_bottom()
        
        # Try to find and click the load more button
        load_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/main/div[1]/div[2]/div[3]')))
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", load_more)
        time.sleep(2)  # Wait for any animations
        load_more.click()
        
        # Wait longer for content to load
        time.sleep(3)
        
        # Scroll to bottom again after clicking
        scroll_to_bottom()
        
        new_height = get_page_height()
        print(f"Old height: {old_height}")
        print(f"New height: {new_height}")
        
        if new_height == old_height:
            same_height_count += 1
            if same_height_count >= 3:  # If height remains same for 3 consecutive tries
                print("Reached end of page - no new content loading")
                break
        else:
            same_height_count = 0  # Reset counter if height changes
            
        old_height = new_height
        retry_count = 0  # Reset retry count on successful click
        
    except (TimeoutException, ElementClickInterceptedException) as e:
        print(f"Error encountered: {str(e)}")
        retry_count += 1
        if retry_count >= max_retries:
            print("Max retries reached, stopping")
            break
        time.sleep(2)  # Wait before retrying

print("Finished loading all content")

# Get all the products
products = driver.find_elements(By.CSS_SELECTOR, '.sm-product')
print(f"\nFound {len(products)} products")

for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, '.name').text
        price = product.find_element(By.CSS_SELECTOR, '.price').text
        print(f"Product: {name} - Price: {price}")
    except:
        continue

# Save the final HTML
html = driver.page_source
with open('smartprix.html', 'w', encoding='utf-8') as f:
    f.write(html)

driver.quit()
