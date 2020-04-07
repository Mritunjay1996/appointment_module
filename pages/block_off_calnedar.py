from selenium.webdriver.common.by import By
import time
from resources.variables import *
import allure


class blockoffCalendarObj:
    blockoffBtn = (By.XPATH, "//a[@class='orange app-data']")
    calendar = (By.XPATH, "//div[@class='bs-datepicker-container']")
    dateFrm = (By.XPATH, "//input[@placeholder='From']")
    sel_date = (By.XPATH, "//span[contains(text(),'" + crrnt_date + "')]")
    dateTo = (By.XPATH, "//input[@placeholder='To']")
    timefromHH = (By.XPATH, "//label[contains(text(),'Vanaf (tijd)')]/parent::div/timepicker/table/tbody/tr[2]/td["
                            "1]/input")
    timefromMM = (By.XPATH, "//label[contains(text(),'Vanaf (tijd)')]/parent::div/timepicker/table/tbody/tr[2]/td["
                            "3]/input")
    timetoHH = (By.XPATH, "//label[contains(text(),'Vanaf (tijd)')]/parent::div/parent::div/following-sibling::div"
                          "//timepicker/table/tbody/tr[2]/td[1]/input")
    timetoMM = (By.XPATH, "//label[contains(text(),'Vanaf (tijd)')]/parent::div/parent::div/following-sibling::div"
                          "//timepicker/table/tbody/tr[2]/td[3]/input")
    blockMultipledays = (By.XPATH, "//label[@class='app-checkbox pull-right']")
    # calName = (By.XPATH, "//label[contains(text(),'" + edit_agenda + "')]")
    calName = (By.XPATH, "//label[contains(text(),'Edit_agenda Auto2585')]")
    blockBtn = (By.XPATH, "//button[@class='btn blue closet']")
    notes = (By.XPATH, "//textarea[@placeholder='Notes']")
    mon = (By.XPATH, "//label[contains(text(),'Herhaal elke')]/parent::div/ul/li[1]")
    tues = (By.XPATH, "//label[contains(text(),'Herhaal elke')]/parent::div/ul/li[2]")
    wed = (By.XPATH, "//label[contains(text(),'Herhaal elke')]/parent::div/ul/li[3]")
    thurs = (By.XPATH, "//label[contains(text(),'Herhaal elke')]/parent::div/ul/li[4]")
    fri = (By.XPATH, "//label[contains(text(),'Herhaal elke')]/parent::div/ul/li[5]")
    sat = (By.XPATH, "//label[contains(text(),'Herhaal elke')]/parent::div/ul/li[6]")
    sun = (By.XPATH, "//label[contains(text(),'Herhaal elke')]/parent::div/ul/li[7]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Click on Clock off Calendar Label ')
    def clickBlockoffcal(self):
        self.browser.find_element(*self.blockoffBtn).click()

    @allure.step('Select Current Date for From Calendar')
    def selectCurrentdateFrom(self):
        self.browser.find_element(*self.dateFrm).click()
        time.sleep(2)
        self.browser.find_element(*self.sel_date).click()

    @allure.step('Select Current Date for To Calendar')
    def selectCurrentdateTo(self):
        self.browser.find_element(*self.dateTo).click()
        time.sleep(2)
        self.browser.find_elements(*self.sel_date).click()

    @allure.step('Enter from HH in Normal hour ')
    def enterFromhh(self, frmHH):
        store = self.browser.find_element(*self.timefromHH)
        store.send_keys(frmHH)

    @allure.step('Enter from HH in Normal hour ')
    def enterFromMM(self, frmMM):
        store = self.browser.find_element(*self.timefromMM)
        store.send_keys(frmMM)

    @allure.step('Enter To HH in Normal hour ')
    def enterTohh(self, toHH):
        store = self.browser.find_element(*self.timetoHH)
        store.send_keys(toHH)

    @allure.step('Enter To MM in Normal hour ')
    def enterToMM(self, toMM):
        store = self.browser.find_element(*self.timetoMM)
        store.send_keys(toMM)

    @allure.step('Click Agenda name to block appointment')
    def clickAgendaname(self):
        self.browser.find_element(*self.calName).click()

    @allure.step('Click Block Button to block ')
    def clickBlockbutton(self):
        self.browser.find_element(*self.blockBtn).click()

    @allure.step('Enter message in notes textfield')
    def enterMessage(self, msg):
        self.browser.find_element(*self.notes).send_keys(msg)

    @allure.step('Verify Multiple Block option should be displayed')
    def verifyMultiblock(self):
        return self.browser.find_element(*self.blockMultipledays).is_displayed()

    @allure.step('Verify Monday is displayed in repet days ')
    def verifyMonday(self):
        return self.browser.find_element(*self.mon).is_displayed()

    @allure.step('Verify Tuesday is displayed in repet days ')
    def verifyTuesday(self):
        return self.browser.find_element(*self.tues).is_displayed()

    @allure.step('Verify Wednesday is displayed in repet days ')
    def verifyWednesday(self):
        return self.browser.find_element(*self.wed).is_displayed()

    @allure.step('Verify Thursday is displayed in repet days ')
    def verifyThursday(self):
        return self.browser.find_element(*self.thurs).is_displayed()

    @allure.step('Verify Friday is displayed in repet days ')
    def verifyFriday(self):
        return self.browser.find_element(*self.fri).is_displayed()

    @allure.step('Verify Saturday is displayed in repet days ')
    def verifySaturday(self):
        return self.browser.find_element(*self.sat).is_displayed()

    @allure.step('Verify Sunday is displayed in repet days ')
    def verifySunday(self):
        return self.browser.find_element(*self.sun).is_displayed()



