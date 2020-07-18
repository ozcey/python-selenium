from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'C:\\Users\OZ\\Downloads\\chromedriver_win32 (4)\\chromedriver.exe')
driver.get('https://formy-project.herokuapp.com/form')


def formSubmissionTest():
    before()
    submitForm()
    waitUntilAlert()
    assert getText().text == 'The form was successfully submitted!'
    tearDown()


def submitForm():
    driver.find_element_by_id('first-name').send_keys('John')
    driver.find_element_by_id('last-name').send_keys('Doe')
    driver.find_element_by_id('job-title').send_keys('Software Developer')
    driver.find_element_by_id('radio-button-3').click()
    driver.find_element_by_id('checkbox-1').click()
    driver.find_element_by_id('select-menu').click()
    driver.find_element_by_xpath('//*[@id="select-menu"]/option[4]').click()
    driver.find_element_by_id('datepicker').send_keys('07/18/2020')
    driver.find_element_by_id('datepicker').send_keys(Keys.RETURN)
    driver.find_element_by_xpath('/html/body/div[1]/form/div/div[8]/a').click()


def waitUntilAlert():
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div/div')))


def getText():
    return driver.find_element_by_xpath('/html/body/div/div')


def before():
    driver.maximize_window()


def tearDown():
    driver.quit()


if __name__ == '__main__':
    formSubmissionTest()
