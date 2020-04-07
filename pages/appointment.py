import allure
from selenium.webdriver.common.by import By


class AppointmentObj:

    day_cal = (By.XPATH, "//a[@class='active']")
    week_cal = (By.XPATH, "//a[contains(text(),'Week')]")
    month_cal = (By.XPATH, "//a[contains(text(),'Maand')]")
    cal_filter = (By.XPATH, "//a[@class='dropdown-toggle block btn caret-down white shadow t1']")
    office = (By.XPATH, "//div[@class='ember-office pointer']")
    resume = (By.XPATH, "//h2[contains(text(),'Samenvatting')]")
    side_menuBar1 = (By.XPATH, "//span[contains(text(),'afspraken')]")
    side_menuBar2 = (By.XPATH, "//ul[@class='list-unstyled']/li[2]")
    side_menuBar3 = (By.XPATH, "//ul[@class='list-unstyled']/li[3]")
    side_menuBar4 = (By.XPATH, "//ul[@class='list-unstyled']/li[4]")
    side_menuBar5 = (By.XPATH, "//ul[@class='list-unstyled']/li[5]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verify Day Button calendar in Aethon Appointment Scheduler')
    def verifyDaybutton(self):
        return self.browser.find_element(*self.day_cal).text

    @allure.step('Verify week Button calendar in Aethon Appointment Scheduler')
    def verifyWeekbutton(self):
        return self.browser.find_element(*self.week_cal).text

    @allure.step('Verify month Button calendar in Aethon Appointment Scheduler')
    def verifyMonthbutton(self):
        return self.browser.find_element(*self.month_cal).text

    @allure.step('Verify office dropdown box in aethon appointment scheduler')
    def verifyOffice_dropdown(self):
        return self.browser.find_element(*self.office).is_displayed()

    @allure.step('Verify Resume in Aethon Appointment Scheduler')
    def verifyResumeheading(self):
        return self.browser.find_element(*self.resume).text

    @allure.step('Verify Side menu Bar 1 -> afspraken')
    def verifysideBar1(self):
        return self.browser.find_element(*self.side_menuBar1).text

    @allure.step('Verify Side menu Bar 2 -> Afspraaktype')
    def verifysideBar2(self):
        return self.browser.find_element(*self.side_menuBar2).text

    @allure.step('Verify Side menu Bar 3 -> Agenda ')
    def verifysideBar3(self):
        return self.browser.find_element(*self.side_menuBar3).text

    @allure.step('Verify Side menu Bar 4 -> Teamagenda ')
    def verifysideBar4(self):
        return self.browser.find_element(*self.side_menuBar4).text

    @allure.step('Verify Side menu Bar 5 -> E-mail-en SMS-sjablonen ')
    def verifysideBar5(self):
        return self.browser.find_element(*self.side_menuBar5).text

