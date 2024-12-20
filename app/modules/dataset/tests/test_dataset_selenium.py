from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def get_host_for_selenium_testing():
    # Return the host URL for Selenium testing
    return "http://localhost:8000"


def initialize_driver():
    # Initialize the WebDriver (e.g., Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)
    return driver


class TestTestDataSet():

    def setup_method(self, method):
        self.driver = initialize_driver()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testDataSet(self):
        self.driver.get(get_host_for_selenium_testing())
        self.driver.set_window_size(1920, 1032)
        self.driver.find_element(By.CSS_SELECTOR, ".sidebar-item:nth-child(2) .align-middle:nth-child(2)").click()
        self.driver.find_element(By.LINK_TEXT, "Sample dataset 4").click()
        self.driver.find_element(By.ID, "btnGroupDrop10").click()
        self.driver.find_element(By.LINK_TEXT, "Syntax check").click()
        self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(2) .col-12 > .btn").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(2) .col-12 > .btn")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-close").click()
        self.driver.find_element(By.ID, "btnGroupDrop11").click()
        self.driver.find_element(By.LINK_TEXT, "Syntax check").click()
        self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(3) .text-end").click()
        self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(3) .col-12 > .btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-close").click()
        self.driver.find_element(By.ID, "btnGroupDropExport11").click()
        self.driver.find_element(By.LINK_TEXT, "UVL").click()
