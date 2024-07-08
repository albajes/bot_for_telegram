from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from settings import LOGIN_URL, MAIN_LOGIN, MAIN_PASSWORD, MEMBERS


async def set_value_to_true(url, username: str) -> None:
    driver = await login_in_macroserver()
    value = await check_mark(driver=driver, username=username, url=url)
    if value is None:
        await click_and_save(driver=driver, username=username)
    driver.close()


async def set_value_to_none(url, username: str) -> None:
    driver = await login_in_macroserver()
    value = await check_mark(driver=driver, username=username, url=url)
    if value:
        await click_and_save(driver=driver, username=username)
    driver.close()


async def login_in_macroserver() -> webdriver:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1200,800")
    driver = webdriver.Chrome(options=options)
    driver.get(LOGIN_URL)
    login_element = driver.find_element(By.CLASS_NAME, 'form-control')
    login_element.send_keys(MAIN_LOGIN)
    password_element = driver.find_element(By.NAME, 'password')
    password_element.send_keys(MAIN_PASSWORD)
    button_element = driver.find_element(By.XPATH, "//button[@type='submit']")
    button_element.click()
    return driver


async def check_mark(username: str, driver: webdriver, url: str):
    driver.get(url)
    distribution_button = driver.find_elements(By.XPATH, '//select')
    select = Select(distribution_button[17])
    select.select_by_value('round_robin')
    button_element_of_members = driver.find_elements(By.XPATH, "//div[@class='ui-multiselect']")
    if len(button_element_of_members) == 14:
        button_element_of_members[6].click()
    else:
        button_element_of_members[7].click()
    button_element_check = driver.find_element(By.XPATH, f"//input[@type='checkbox'][@value='{MEMBERS[username]}']")
    value = button_element_check.get_attribute('checked')
    return value


async def click_and_save(driver: webdriver, username: str) -> None:
    button_element_check = driver.find_element(By.XPATH, f"//input[@type='checkbox'][@value='{MEMBERS[username]}']")
    button_element_check.click()
    button_element_save = driver.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-success m-b-16']")
    button_element_save.click()
    button_element_save.click()


async def check_mark_macrocatalog(username: str, driver: webdriver, url: str):
    driver.get(url)
    distribution_button = driver.find_elements(By.XPATH, '//select')
    select = Select(distribution_button[8])
    select.select_by_value('round_robin')
    button_element_of_members = driver.find_elements(By.XPATH, "//div[@class='ui-multiselect']")
    button_element_of_members[4].click()
    button_element_check_macrocatalog = driver.find_element(By.XPATH, f"//input[@type='checkbox'][@value='{MEMBERS[username]}']")
    value = button_element_check_macrocatalog.get_attribute('checked')
    return value
