from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.variables import *


class appDashboardObj:
    logo = (By.XPATH, "//img[@class='logo-image-container sizing']")
    profileImg = (By.XPATH, "//img[@class='img-circle img-cu stom min-image-size sizeHeight']")
    profileName = (By.XPATH, "//span[@class='user-name-container']")
    profileDrpdwn = (By.XPATH, "//i[@class='fa fa-angle-down leftSp ace']")
    myProfile = (By.XPATH, "//a[contains(text(),'Mijn profiel')]")
    language = (By.XPATH, "//a[contains(text(),'Taal')]")
    logout = (By.XPATH, "//a[contains(text(),'Log Out')]")
    allAppointmentLabel = (By.XPATH, "//h1[@class='title-2']")
    appointmentTab = (By.XPATH, "//span[contains(text(),'Appointments')]")
    officedrpdwn = (By.XPATH, "//div[@class='toggle']")
    side_menuBar1 = (By.XPATH, "//ul[@class='list-unstyled']/li[1]")
    side_menuBar2 = (By.XPATH, "//ul[@class='list-unstyled']/li[2]")
    side_menuBar3 = (By.XPATH, "//ul[@class='list-unstyled']/li[3]")
    side_menuBar4 = (By.XPATH, "//ul[@class='list-unstyled']/li[4]")
    side_menuBar5 = (By.XPATH, "//ul[@class='list-unstyled']/li[5]")
    add_appointmentTypes = (By.XPATH, "//a[@class='btn blue app-data line']")
    bfrXpth = "//td[div[p[contains(text(),'"
    aftrXpth = "')]]]"
    appTypeAvail = (By.XPATH, bfrXpth + appointment_name + aftrXpth + "/following-sibling::td[2]")
    appTypeEdit = (By.XPATH,  bfrXpth + appointment_name + aftrXpth + "/following-sibling::td[3]/ul/li[1]/a[i["
                                                                      "contains(text(),'')]]")
    To_copy = (By.XPATH, bfrXpth + appointment_name + aftrXpth + "/following-sibling::td[3]/ul/li[2]/a[i[contains("
                                                                 "text(),'')]]")
    update_appTypeEdit = (By.XPATH, bfrXpth + edit_appointment + aftrXpth + "/following-sibling::td[3]/ul/li[1]/a[i["
                                                                            "contains(text(),'')]]")
    edit_apptype_label = (By.XPATH, "//h2[@class='title-3']")
    updateBtn = (By.XPATH, "//button[contains(text(),'Bijwerken')]")
    deleteBtn = (By.XPATH, "//a[@id='del']")
    alert = (By.XPATH, "//div[@class='sn-title']")
    deleteBtnYes = (By.XPATH, "//button[@class='btn btn-default']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Verify Appointment tab on Appointment type dashboard page ')
    def verifyappTab(self):
        return self.browser.find_element(*self.appointmentTab).is_displayed()

    @allure.step('Verify Business Logo on Appointment Type Dashboard')
    def verifyBusslogo(self):
        return self.browser.find_element(*self.logo).is_displayed()

    @allure.step('Verify Recruiter profile image')
    def verifyProfileimage(self):
        return self.browser.find_element(*self.profileImg).is_displayed()

    @allure.step('Verify Recruiter profile name ')
    def verifyProfilename(self):
        return self.browser.find_element(*self.profileName).text

    @allure.step('Verify My profile option in recruiter profile dropdown')
    def verifydropdownoption1(self):
        self.browser.find_element(*self.profileDrpdwn).click()
        return self.browser.find_element(*self.myProfile).text

    @allure.step('Verify My profile option in recruiter profile dropdown')
    def verifydropdownoption2(self):
        return self.browser.find_element(*self.language).text

    @allure.step('Verify Log out option in recruiter profile dropdown')
    def verifydrpodownoption3(self):
        return self.browser.find_element(*self.logout).text

    @allure.step('Verify Label for All Appointment Type Heading')
    def verifyAppPageLabel(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.allAppointmentLabel))
        return self.browser.find_element(*self.allAppointmentLabel).text

    @allure.step('Verify Office dropdown on Appointment type Dashboard page')
    def verifyOfficedrpdwon(self):
        return self.browser.find_element(*self.officedrpdwn).is_displayed()

    @allure.step('Verify Side menu Bar 1 -> afspraken on Appointment type dashboard')
    def verifysideBar1(self):
        return self.browser.find_element(*self.side_menuBar1).text

    @allure.step('Verify Side menu Bar 2 -> Afspraaktype on Appointment type dashboard')
    def verifysideBar2(self):
        return self.browser.find_element(*self.side_menuBar2).text

    @allure.step('Verify Side menu Bar 3 -> Agenda on Appointment type dashboard')
    def verifysideBar3(self):
        return self.browser.find_element(*self.side_menuBar3).text

    @allure.step('Verify Side menu Bar 4 -> Teamagenda on Appointment type dashboard')
    def verifysideBar4(self):
        return self.browser.find_element(*self.side_menuBar4).text

    @allure.step('Verify Side menu Bar 5 -> E-mail-en SMS-sjablonen on Appointment type dashboard')
    def verifysideBar5(self):
        return self.browser.find_element(*self.side_menuBar5).text

    @allure.step('Verify Availability for added Appointment Type ')
    def verify_availAddedapp(self):
        return self.browser.find_element(*self.appTypeAvail).text

    @allure.step('Verify Edit option for added Appointment Type ')
    def verify_editAddedapp(self):
        edit = self.browser.find_element(*self.appTypeEdit)
        return edit.text

    @allure.step('Verify To copy option for added Appointment Type ')
    def verify_tocopyAddedapp(self):
        return self.browser.find_element(*self.To_copy).text

    @allure.step('Click on Edit button to update and delete Existing appointment type')
    def clickeditBtn(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.update_appTypeEdit))
        self.browser.find_element(*self.update_appTypeEdit).click()

    @allure.step('Verify Label for Edit Appointment Type ')
    def verifyEditappLabel(self):
        return self.browser.find_element(*self.edit_apptype_label).text

    @allure.step('Click on Update Button ')
    def clickUpdatebtn(self):
        self.browser.find_element(*self.updateBtn).click()

    @allure.step('Click on Delete Button ')
    def clickDeletebtn(self):
        self.browser.find_element(*self.deleteBtn).click()

    @allure.step('Verify Alert that consist success message ')
    def verifyAlert(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 10, ignored_exceptions).until(EC.presence_of_element_located(self.alert))
        alert = self.browser.find_element(*self.alert).text
        return alert

    @allure.step('Accept confirmation alert for delete Appointment type')
    def acceptAlerttodelete(self):
        self.browser.find_element(*self.deleteBtnYes).click()



