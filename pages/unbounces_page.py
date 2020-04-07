from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import allure, time


class unbouncesObj:
    url = "http://unbouncepages.com/test/lead-testing/"
    pageHeading = (By.XPATH, "//span[contains(text(),'Reageren')]")
    firstName = (By.XPATH, "//input[@id='voornaam']")
    lastName = (By.XPATH, "//input[@id='achternaam']")
    email = (By.XPATH, "//input[@id='email']")
    phone = (By.XPATH, "//input[@id='telefoonnummer']")
    postCode = (By.XPATH, "//input[@id='postcode']")
    clientName = (By.XPATH, "//select[@id='clientName']")
    sourceType = (By.XPATH, "//select[@id='sourceType']")
    sourceId = (By.XPATH, "//input[@id='sourceId']")
    houseNo = (By.XPATH, "//input[@id='huisnummer']")
    reactBtn = (By.XPATH, "//button[@id='lp-pom-button-132']")
    success = (By.XPATH, "//h1[contains(text(),'Bedankt!')]")
    close_alert = (By.XPATH, "//button[@class='close__2NcGKV']")
    iframe = (By.XPATH, "//iframe[@src='http://unbouncepages.com/test/lead-testing/a-form_confirmation.html']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('OPen unbounce Url ')
    def load_unbounce(self):
        self.browser.get(self.url)

    @allure.step('Verify page Heading ')
    def verifyPageheading(self):
        return self.browser.find_element(*self.pageHeading).text

    @allure.step('Enter First Name ')
    def enterFirstname(self, fn):
        self.browser.find_element(*self.firstName).send_keys(fn)

    @allure.step('Enter Last name ')
    def enterLastname(self, ln):
        self.browser.find_element(*self.lastName).send_keys(ln)

    @allure.step('Enter Email ')
    def enterEMail(self, em):
        self.browser.find_element(*self.email).send_keys(em)

    @allure.step('Enter Phone ')
    def enterPhone(self, ph):
        self.browser.find_element(*self.phone).send_keys(ph)

    @allure.step('Enter Postal code ')
    def enterPostalcode(self, post):
        self.browser.find_element(*self.postCode).send_keys(post)

    @allure.step('Select client name ')
    def selectClientname(self, cname):
        sel = Select(self.browser.find_element(*self.clientName))
        sel.select_by_visible_text(cname)

    @allure.step('Select Source type ')
    def selectSourcetype(self, type):
        sel = Select(self.browser.find_element(*self.sourceType))
        sel.select_by_visible_text(type)

    @allure.step('Enter Source Id ')
    def enterSourceid(self, id):
        self.browser.find_element(*self.sourceId).send_keys(id)

    @allure.step('Enter house number ')
    def enterHousenumber(self, num):
        self.browser.find_element(*self.houseNo).send_keys(num)

    @allure.step('Click on button -> React ')
    def clickReactbutton(self):
        self.browser.find_element(*self.reactBtn).click()

    @allure.step('Verify success message after react ')
    def verifySuccessmsg(self):
        ifram = self.browser.find_element(*self.iframe)
        self.browser.switch_to.frame(ifram)
        time.sleep(3)
        return self.browser.find_element(*self.success).text

    @allure.step('Click on cancel button to close popup ')
    def clickCancelbutton(self):
        self.browser.switch_to.default_content()
        time.sleep(2)
        self.browser.find_element(*self.close_alert).click()
        time.sleep(3)





