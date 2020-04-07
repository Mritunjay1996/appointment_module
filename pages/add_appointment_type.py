import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class addAppointmentypeObj:
    appointmentTab = (By.XPATH, "//span[contains(text(),'Appointments')]")
    appointmentTypes = (By.XPATH, "//a[contains(text(),'Appointment types')]")
    add_appointmentTypes = (By.XPATH, "//a[@class='btn blue app-data line']")
    appointmentName = (By.XPATH, "//label[contains(text(),'Afspraak')]")
    apointmntDesc = (By.XPATH, "//label[contains(text(),'Omschrijving')]")
    confirmationMessage = (By.XPATH, "//label[contains(text(),'Bevestigingsbericht')]")
    appointmentDuration = (By.XPATH, "//div[@class='col-sm-3']//label[@class='control-label'][contains(text(),'Tijd')]")
    extraTime = (By.XPATH, "//label[contains(text(),'Extra tijd')]")
    categoryDropdown = (By.XPATH, "//label[contains(text(),'Categorie')]")
    addnewCategory = (By.XPATH, "//label[contains(text(),'Nieuwe categorie toevoegen')]")
    okButton = (By.XPATH, "//button[@class='btn blue']")
    colorCode = (By.XPATH, "//label[contains(text(),'Kleurcode')]")
    maxpeopleAllowed = (By.XPATH, "//label[contains(text(),'Maximaal aantal toegestane kandidaten')]")
    availAppoitment = (By.XPATH, "//label[contains(text(),'Op afspraak')]")
    availVast = (By.XPATH, "//label[contains(text(),'Op afspraak')]")
    linkAppointmentCal = (By.XPATH, "//div[@class='in']/following-sibling::span")
    addButton = (By.XPATH, "//button[@class='btn blue closet']")
    cancelButton = (By.XPATH, "//a[@class='btn line closet']")
    backAppointment = (By.XPATH, "//a[@class='back closet']")
    setappName = (By.XPATH, "//input[@name='date']")
    setappDesc = (By.XPATH, "//label[contains(text(),'Omschrijving')]/following-sibling::textarea")
    # setappDesc = (By.XPATH, "//div[@id='data-edit']//textarea[@formcontrolname='AppointmentTypeDescription']")
    setcnfrmMsg = (By.XPATH, "//div[@class='ql-editor ql-blank']//p")
    setappDuration = (By.XPATH, "//input[@name='quant[1]']")
    setappExtratym = (By.XPATH, "//input[@name='quant[2]']")
    setcategryDrpdwn = (By.XPATH, "//div[@class='col-md-3']/select")
    setnewCtgry = (By.XPATH, "//select[@class='form-control select2 ng-pristine ng-valid ng-touched']")
    setmaxPeople = (By.XPATH, "//div[@class='col-md-3']/input[@class='form-control ng-untouched ng-pristine ng-valid']")
    appointmentTypeTitle = (By.XPATH, "//h1[@class='title-2']")
    officeradiobtn = (By.XPATH, "//label[contains(text(),'Office Wise')]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Click Appointment type from appointment dropdown .')
    def clickAppointmentypes(self):
        appoint = self.browser.find_element(*self.appointmentTab)
        ActionChains(self.browser).move_to_element(appoint).perform()
        self.browser.find_element(*self.appointmentTypes).click()

    @allure.step('Click Add Appointment Type button ')
    def clickAddAppointmentype(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.add_appointmentTypes))
        self.browser.find_element(*self.add_appointmentTypes).click()

    @allure.step('Verify Appointment name option should be in Add appointment type. ')
    def verifyAppointmentName(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.appointmentName))
        return self.browser.find_element(*self.appointmentName).is_displayed()

    @allure.step('Verify Appointment description ')
    def verifyAppointmentDescription(self):
        return self.browser.find_element(*self.apointmntDesc).is_displayed()

    @allure.step('Verify Confirmation message option')
    def verifyMessageConfirmation(self):
        return self.browser.find_element(*self.confirmationMessage).is_displayed()

    @allure.step('Verify Duration option should be in Add appointment type form. ')
    def verifyDuration(self):
        return self.browser.find_element(*self.appointmentDuration).is_displayed()

    @allure.step('Verify Extra Time ')
    def verifyExtraTime(self):
        return self.browser.find_element(*self.extraTime).is_displayed()

    @allure.step('Verify Category Dropdown option ')
    def verifyCategoryDropdown(self):
        return self.browser.find_element(*self.categoryDropdown).is_displayed()

    @allure.step('Verify Add New Category ')
    def verifyAddnewCategory(self):
        return self.browser.find_element(*self.addnewCategory).is_displayed()

    @allure.step('Verify OK Button ')
    def verifyokButton(self):
        return self.browser.find_element(*self.okButton).is_displayed()

    @allure.step('Verify Color code ')
    def verifyColorCode(self):
        return self.browser.find_element(*self.colorCode).is_displayed()

    @allure.step('Verify Maximum number of people allowed option ')
    def verifyMaxPeopleAllowed(self):
        return self.browser.find_element(*self.maxpeopleAllowed).is_displayed()

    @allure.step('Verify Availability mode for appointment based ')
    def verifyavailAppoint(self):
        return self.browser.find_element(*self.availAppoitment).is_displayed()

    @allure.step('Verify Availibility mode for Vast based ')
    def verifyavailVast(self):
        return self.browser.find_element(*self.availVast).is_displayed()

    @allure.step('Verify Option for link to existing appointment calendars label')
    def verifyLinkappointment(self):
        return self.browser.find_element(*self.linkAppointmentCal).is_displayed()

    @allure.step('Verify Add Buttons')
    def verifyAddButton(self):
        return self.browser.find_element(*self.addButton).is_displayed()

    @allure.step('Verify Cancel Button  ')
    def verifyCancelButton(self):
        return self.browser.find_element(*self.cancelButton).is_displayed()

    @allure.step('Verify Option for back to my appointment')
    def verifyBackToappointment(self):
        return self.browser.find_element(*self.backAppointment).is_displayed()

    @allure.step('Enter Appointment name ')
    def enterAppointmentName(self, name):
        self.browser.find_element(*self.setappName).send_keys(name)

    @allure.step('Enter Appointment Description ')
    def enterAppointmentDescription(self, desc):
        self.browser.find_element(*self.setappDesc).send_keys(desc)

    @allure.step('Enter Confirmation message ')
    def enterConfirmationMsg(self, msg):
        self.browser.find_element(*self.setcnfrmMsg).send_keys(msg)

    @allure.step('Enter Appointment Duration ')
    def enterAppointmentDuration(self, duration):
        self.browser.find_element(*self.setappDuration).clear()
        time.sleep(2)
        self.browser.find_element(*self.setappDuration).send_keys(duration)

    @allure.step('Enter Appointment Extra Time ')
    def enterAppointmentextraTime(self, extra):
        self.browser.find_element(*self.setappExtratym).send_keys(extra)

    @allure.step('Select Category from Dropdown ')
    def selectCategoryDropdown(self, category):
        sel = Select(self.browser.find_element(*self.setcategryDrpdwn))
        sel.select_by_visible_text(category)

    @allure.step('Enter name to add new Category')
    def enterToaddNewCat(self, newCat):
        self.browser.find_element(*self.setnewCtgry).send_keys(newCat)

    @allure.step('Click Button -> OK ')
    def clickokButton(self):
        self.browser.find_element(*self.okButton).click()

    @allure.step('Enter Maximum number of allowed candidate')
    def enterMaxallowed(self, max):
        self.browser.find_element(*self.setmaxPeople).send_keys(max)

    @allure.step('Select Availability from Radio Button ')
    def selectAvailability(self):
        self.browser.find_element(*self.availAppoitment).click()

    @allure.step('Click Button -> Add')
    def clickAddButton(self):
        self.browser.find_element(*self.addButton).click()

    @allure.step('Click Back to my appointment link to go on Appointment Type page')
    def clickBackmyAppointment(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.backAppointment))
        self.browser.find_element(*self.backAppointment).click()

    @allure.step('Verify Page heading for Appointment Type Heading')
    def verifyAppPageheading(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.appointmentTypeTitle))
        return self.browser.find_element(*self.appointmentTypeTitle).text

    @allure.step('Edit Appointment Type name ')
    def editAppointmentName(self, desc):
        self.browser.find_element(*self.setappName).click()
        # self.browser.find_element(*self.setappName).send_keys(Keys.CONTROL + 'a')
        # self.browser.find_element(*self.setappName).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*self.setappName).clear()
        time.sleep(2)
        self.browser.find_element(*self.setappName).send_keys(desc)

    @allure.step('CLick on office wise Radio Button to edit Appointment type ')
    def clickOfficeRadio(self):
        self.browser.find_element(*self.officeradiobtn).click()





