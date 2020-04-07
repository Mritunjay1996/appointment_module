from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from resources.variables import *
import allure, time


class moveActiveObj:
    initial = (By.XPATH, "//a[contains(text(),'Eerste afspraak')]")
    appointmentTab = (By.XPATH, "//span[contains(text(),'Appointments')]")
    emailSms = (By.XPATH, "//a[contains(text(),'E-mail & SMS templates')]")
    emailHeading = (By.XPATH, "//h1[@class='title-4']")
    template3 = (By.XPATH, "//label[contains(text(),'Associëren met template 3')]")
    appointmentTomove = (By.XPATH, "//span[contains(text(),'" + appointment_name + "')]/parent::li/a[1]") #"//span[contains(text(),'Appointment Automation900')]/parent::li/a[1]"
    compnyWideChkbox = (By.XPATH, "//label[@class='app-checkbox beta']")
    save_btn = (By.XPATH, "//button[@class='btn blue closet']")
    final_save = (By.XPATH, "//button[@class='btn blue']")
    appointmCnfrm = (By.XPATH, "//a[contains(text(),'Afspraak bevestiging')]")
    appointReminder = (By.XPATH, "//a[contains(text(),'Herinnering')]")
    rescheduling = (By.XPATH, "//a[contains(text(),'Afspraak verzetten')]")
    cancellation = (By.XPATH, "//ul[@class='nav nav-tabs']//a[contains(text(),'Annuleren')]")
    preview = (By.XPATH, "//a[contains(text(),'Voorbeeld')]")
    useDefault = (By.XPATH, "//a[contains(text(),'Gebruik standaardtemplate')]")
    emailTemp = (By.XPATH, "//h2[contains(text(),'E-mail Template')]")
    smsTemp = (By.XPATH, "//h2[contains(text(),'SMS-sjabloon')]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Click on EMail and SMS Template Button ')
    def clickEmailSms(self):
        appint = self.browser.find_element(*self.appointmentTab)
        ActionChains(self.browser).move_to_element(appint).perform()
        self.browser.find_element(*self.emailSms).click()

    @allure.step('Verify EMail and SMS template Heading')
    def verify_emailsms_heading(self):

        return self.browser.find_element(*self.emailHeading).text

    @allure.step('Move from inactive to active template ')
    def moveInactivetoactive(self):
        time.sleep(2)
        temp = self.browser.find_element(*self.appointmentTomove)
        temp.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        self.browser.find_element(*self.appointmentTomove).click()
        time.sleep(5)
        appoint = self.browser.find_element(*self.template3)
        appoint.click()
        time.sleep(4)
        self.browser.find_element(*self.save_btn).click()

        # ActionChains(self.browser).drag_and_drop(appoint , temp).perform()
        # try:
        #     element = ActionChains(self.browser).click_and_hold(appoint)
        #     time.sleep(2)
        #     temp.send_keys(Keys.HOME)
        #     time.sleep(2)
        #     element.move_to_element(temp).release(temp).perform()
        #
        # except:
        #     pass

    @allure.step('Click on checkbox to enable company wide ')
    def clickOncheckbox(self):
        time.sleep(2)
        self.browser.find_element(*self.compnyWideChkbox).click()

    @allure.step('Click on save button to save the appointment type into other template')
    def clickSavebutton(self):
        time.sleep(2)
        self.browser.find_element(*self.final_save).click()

    @allure.step('Click on Appointment cofirmation tab')
    def clickAppointmentConfirm(self):
        time.sleep(1)
        self.browser.find_element(*self.appointmCnfrm).click()

    @allure.step('Click on Appointment Reminder')
    def clickappointmentReminder(self):
        time.sleep(1)
        self.browser.find_element(*self.appointReminder).click()

    @allure.step('CLick on Rescheduling tab')
    def clickReschedulingtab(self):
        time.sleep(1)
        self.browser.find_element(*self.rescheduling).click()

    @allure.step('Click on cancellation tab')
    def clickCancellationtab(self):
        time.sleep(1)
        self.browser.find_element(*self.cancellation).click()

    @allure.step('Verify Initial appointment tab')
    def verifyInitialtab(self):
        time.sleep(1)
        return self.browser.find_element(*self.initial).text

    @allure.step('Verify Appointment confirmation tab')
    def verifyApptconfirmationTab(self):
        time.sleep(1)
        return self.browser.find_element(*self.appointmCnfrm).text

    @allure.step('Verify Appointment Reminder tab')
    def verifyApptRemindertab(self):
        time.sleep(1)
        return self.browser.find_element(*self.appointReminder).text

    @allure.step('Verify Rescheduling tab in header')
    def verifyReschedulingTab(self):
        time.sleep(1)
        return self.browser.find_element(*self.rescheduling).text

    @allure.step('Verify Cancellation tab in header')
    def verifyCancellationtab(self):
        return self.browser.find_element(*self.cancellation).text

    @allure.step('Verify Check box for standard option ')
    def verifyCheckbox(self):
        return self.browser.find_element(*self.compnyWideChkbox).is_displayed()

    @allure.step('Verify Save button below email and sms template block')
    def verifySavebutton(self):
        time.sleep(1)
        return self.browser.find_element(*self.final_save).is_displayed()

    @allure.step('Verify Preview Button below email and sms template')
    def verifyPreviewbutton(self):
        return self.browser.find_element(*self.preview).is_displayed()

    @allure.step('Verify Default Preview button below email and sms template block ')
    def verifyuseDefaultBtn(self):
        return self.browser.find_element(*self.useDefault).is_displayed()

    @allure.step('Verify Email template block should be there')
    def verifyEmailtemplate(self):
        time.sleep(1)
        return self.browser.find_element(*self.emailTemp).text

    @allure.step('Verify SMS template block should be there ')
    def verifySmstemplate(self):
        time.sleep(1)
        return self.browser.find_element(*self.smsTemp).text






