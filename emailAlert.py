# Open an Amazon product page.
# Extract the current price.
# If the price drops below a set value, send an email alert.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Firefox()
driver.get("https://www.amazon.in/Nursery-Pune-Plants-Live-Season/dp/B0DRT7TF2L/?_encoding=UTF8&pd_rd_w=c3Li3&content-id=amzn1.sym.0a89cdee-4cd3-4648-83ed-2e98b723ee93&pf_rd_p=0a89cdee-4cd3-4648-83ed-2e98b723ee93&pf_rd_r=ZY4NTGBKD97C41MSJJJQ&pd_rd_wg=WFELT&pd_rd_r=791ffcc6-d213-4c31-8a6b-f0dfd28c6556&ref_=pd_hp_d_btf_NAMCLOTHING")
try: 
    price_element = driver.find_element(By.XPATH, "//span[@class = 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay']")
    price = price_element.text.strip().replace(",", "")
    price= price.replace("₹", "").strip()
    
    
    price = int(price)
    
    target_price =150
    if price < target_price:
        print(f"drop alert : {price}")
    else:
        print(f"current price: {price}")


except Exception as e:
    print(" Error fetching price:", e)
time.sleep(5)
# Close the browser
driver.quit()