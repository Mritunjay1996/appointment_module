from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from resources.variables import *
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class addCalendarObj:
    addappCal = (By.XPATH, "//a[@class='btn blue app-data line']")
    availBtn = (By.XPATH, "//a[contains(text(),'Beschikbaarheid')]")
    settingBtn = (By.XPATH, "//a[contains(text(),'Instellingen')]")
    normalHour = (By.XPATH, "//label[contains(text(),'Normale werktijden')]")
    daysOff = (By.XPATH, "//label[contains(text(),'Vrije dagen')]")
    hrfrmHH =(By.XPATH, "//label[contains(text(),'Normale werktijden')]/parent::div//div/div["
                        "1]/div/timepicker/table/tbody/tr[2]/td[1]/input")
    hrfrmMM = (By.XPATH, "//label[contains(text(),'Normale werktijden')]/parent::div//div/div["
                         "1]/div/timepicker/table/tbody/tr[2]/td[3]/input")
    hrtoHH = (By.XPATH, "//label[contains(text(),'Normale werktijden')]/parent::div//div/div["
                        "2]/div/timepicker/table/tbody/tr[2]/td[1]/input")
    hrtoMM = (By.XPATH, "//label[contains(text(),'Normale werktijden')]/parent::div//div/div["
                        "2]/div/timepicker/table/tbody/tr[2]/td[3]/input")
    applyBtn = (By.XPATH, "//button[contains(text(),'Toepassen')]")
    daysoffMonday = (By.XPATH, "//label[contains(text(),'Ma')]")
    daysoffTues = (By.XPATH, "//label[contains(text(),'Di')]")
    daysoffWed = (By.XPATH, "//label[contains(text(),'Woe')]")
    daysoffThur = (By.XPATH, "//label[contains(text(),'Do')]")
    daysOffFri = (By.XPATH, "//label[@class='app-checkbox'][contains(text(),'Vr')]")
    daysoffSat = (By.XPATH, "//label[contains(text(),'Za')]")
    daysoffSun = (By.XPATH, "//label[contains(text(),'Zo')]")
    prevBtn = (By.XPATH, "//a[contains(text(),'voorgaand')]")
    nextBtn =(By.XPATH, "//ul[@class='pager']//a[contains(text(),'volgende')]")
    addBtn = (By.XPATH, "//button[@class='btn blue closet']")
    cancelBtn = (By.XPATH, "//a[@class='btn line closet']")
    backLink = (By.XPATH, "//a[@class='back closet']")
    crossBtn = (By.XPATH, "//a[@class='closet']")

    agendaTitle = (By.XPATH, "//label[contains(text(),'Agenda titel')]")
    enteragenda = (By.XPATH, "//div[@class='form-group']//input[@name='text']")
    email = (By.XPATH, "//label[contains(text(),'Email')]")
    enteremail = (By.XPATH, "//input[@formcontrolname='NotificationEmail']")
    telephone = (By.XPATH, "//label[contains(text(),'Telefoonnummer')]")
    enterphone = (By.XPATH, "//div[@class='form-group row']//div[2]//input[1]")
    numofperson = (By.XPATH, "//label[contains(text(),'Aantal kandidaten per tijdslot')]")
    entermaxpeople = (By.XPATH, "//input[@formcontrolname='MaxAppointmentPerSlot']")
    dropdown = (By.XPATH, "//div[@class='col-md-7']/select[1]")
    personalCal = (By.XPATH, "//p[@class='item']")
    labelTolink = (By.XPATH, "//span[@class='in grey-bkg']")
    comwide = (By.XPATH, "//label[@class='app-checkbox beta active']")
    specoficoffice = (By.XPATH, "//label[@class='app-checkbox beta']")
    searchbox = (By.XPATH, "//input[@placeholder='Search by Appointment Type']")
    officedrpdwn = (By.XPATH, "//a[@class='dropdown-toggle block btn white shadow t1 dropdown-container officeWidth']")
    selectApp = (By.XPATH, "//label[@class='app-checkbox word-brk']")
    calEdit = (By.XPATH, "//p[contains(text(),'" + edit_agenda + "')]/parent::div/parent::td/following-sibling::td/ul[1]/li[2]")
    updateBtn = (By.XPATH, "//button[@class='btn blue closet']")
    alert = (By.XPATH, "//div[@class='sn-title']")
    deleteBtn = (By.XPATH, "//a[@id='del']")
    deleteBtnYes = (By.XPATH, "//button[@class='btn btn-default']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Click on action button -> Setting')
    def clickSettingbtn(self):
        self.browser.find_element(*self.settingBtn).click()

    @allure.step('Verify Agenda Title in setting')
    def verifyagendaTitle(self):
        return self.browser.find_element(*self.agendaTitle).is_displayed()

    @allure.step('Verify Email in setting')
    def verifyEmail(self):
        return self.browser.find_element(*self.email).is_displayed()

    @allure.step('Verify Telephone Number in Setting')
    def verifyTelephonenum(self):
        return self.browser.find_element(*self.telephone).is_displayed()

    @allure.step('Verify Number of candidates per time slot')
    def verifyCandidatenum(self):
        return self.browser.find_element(*self.numofperson).is_displayed()

    @allure.step('Verify Dropdown for Schedule appointment')
    def verifydropdownSchedule(self):
        return self.browser.find_element(*self.dropdown).is_displayed()

    @allure.step('Verify Personal Calendar switch button')
    def verifyCalswitchbtn(self):
        return self.browser.find_element(*self.personalCal).is_displayed()

    @allure.step('Verify Label to link calendar with appointment type')
    def verifyCaLinkAppLabel(self):
        return self.browser.find_element(*self.labelTolink).is_displayed()

    @allure.step('Verify company wide button')
    def verifyCompwide(self):
        return self.browser.find_element(*self.comwide).is_displayed()

    @allure.step('Verify Search Appointment Type- > Office wise')
    def verifyOfficewise(self):
        return self.browser.find_element(*self.specoficoffice).is_displayed()

    @allure.step('Verify office dropdown with selecting office wise')
    def verifyOfficedropdown(self):
        return self.browser.find_element(*self.officedrpdwn).is_displayed()

    @allure.step('Verify Search box ')
    def verifySearchbox(self):
        return self.browser.find_element(*self.searchbox).is_enabled()

    @allure.step('Click company wide option ')
    def clickCompwide(self):
        self.browser.find_element(*self.comwide).click()

    @allure.step('click office wise option')
    def clickOfficewise(self):
        self.browser.find_element(*self.specoficoffice).click()

    @allure.step('Verify option for normal working hour')
    def verifyNormwrkhr(self):
        return self.browser.find_element(*self.normalHour).is_displayed()

    @allure.step('Verify Setting Button ')
    def verifySettingbtn(self):
        return self.browser.find_element(*self.settingBtn).is_displayed()

    @allure.step('Verify Availability button ')
    def verifyAvailbtn(self):
        return self.browser.find_element(*self.availBtn).is_displayed()

    @allure.step('Verify cross button to close the popup ')
    def verifyCrossbtn(self):
        return self.browser.find_element(*self.crossBtn).is_displayed()

    @allure.step('Verify Back to appointment calendar link ')
    def verifyBackappcal(self):
        return self.browser.find_element(*self.backLink).is_displayed()

    @allure.step('Verify Add Button on Add new Calendar form')
    def verifyAddbtn(self):
        return self.browser.find_element(*self.addBtn).is_displayed()

    @allure.step('Verify Cancel Button on Add new Calendar form')
    def verifyCancelbtn(self):
        return self.browser.find_element(*self.cancelBtn).is_displayed()

    @allure.step('Verify Previous Button ')
    def verifyPrevbtn(self):
        return self.browser.find_element(*self.prevBtn).is_displayed()

    @allure.step('Verify Next Button')
    def verifyNextbtn(self):
        return self.browser.find_element(*self.nextBtn).is_displayed()

    @allure.step('Verify Apply Button ')
    def verifyApplybtn(self):
        return self.browser.find_element(*self.applyBtn).is_displayed()

    @allure.step('Click on button -> Add new Calendar')
    def clickAddcalendar(self):
        self.browser.find_element(*self.addappCal).click()

    @allure.step('Enter from HH in Normal hour ')
    def enterFromhh(self, frmHH):
        store = self.browser.find_element(*self.hrfrmHH)
        store.send_keys(frmHH)

    @allure.step('Enter from HH in Normal hour ')
    def enterFromMM(self, frmMM):
        store = self.browser.find_element(*self.hrfrmMM)
        store.send_keys(frmMM)

    @allure.step('Enter To HH in Normal hour ')
    def enterTohh(self, toHH):
        store = self.browser.find_element(*self.hrtoHH)
        store.send_keys(toHH)

    @allure.step('Enter To MM in Normal hour ')
    def enterToMM(self, toMM):
        store = self.browser.find_element(*self.hrtoMM)
        store.send_keys(toMM)

    @allure.step('Verify Days off option in available add calendar. ')
    def verifyDaysoff(self):
        return self.browser.find_element(*self.daysOff).is_displayed()

    @allure.step('Verify Days off , Monday')
    def verifyMondayoff(self):
        return self.browser.find_element(*self.daysoffMonday).is_displayed()

    @allure.step('Verify Days off , Tuesday')
    def verifyTuesoff(self):
        return self.browser.find_element(*self.daysoffTues).is_displayed()

    @allure.step('Verify Days off , Wednesday')
    def verifyWedoff(self):
        return self.browser.find_element(*self.daysoffWed).is_displayed()

    @allure.step('Verify Days off , Thursday')
    def verifyThursoff(self):
        return self.browser.find_element(*self.daysoffThur).is_displayed()

    @allure.step('Verify Days off , Friday')
    def verifyFrioff(self):
        return self.browser.find_element(*self.daysOffFri).is_displayed()

    @allure.step('Verify Days off , Saturday')
    def verifySatoff(self):
        return self.browser.find_element(*self.daysoffSat).is_displayed()

    @allure.step('Verify Days off , Sunday')
    def verifySundayoff(self):
        return self.browser.find_element(*self.daysoffSun).is_displayed()

    @allure.step('Click cross button ')
    def clickCrossBtn(self):
        self.browser.find_element(*self.crossBtn).click()

    @allure.step('Verify After clicking on Add Appointment calendar By default it should select')
    def verifyAvailbtnSelected(self):
        return self.browser.find_element(*self.availBtn).text

    @allure.step('Click on Saturday in days off list ')
    def clickSaturdayoff(self):
        self.browser.find_element(*self.daysoffSat).click()

    @allure.step('Click on Sunday in days off list ')
    def clickSundayoff(self):
        self.browser.find_element(*self.daysoffSun).click()

    @allure.step('CLick on Apply button to set working hours')
    def clickApplybtn(self):
        self.browser.find_element(*self.applyBtn).click()
        self.browser.find_element(*self.applyBtn).click()

    @allure.step('Enter Name for Agenda Title ')
    def enterAgendaname(self, name):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.enteragenda))
        self.browser.find_element(*self.enteragenda).send_keys(name)

    @allure.step('Enter Email To notify people about appointment type in setting')
    def enterEmailaddress(self, email):
        self.browser.find_element(*self.enteremail).send_keys(email)

    @allure.step('Enter Telephone number ')
    def enterTelephonenumber(self, number):
        self.browser.find_element(*self.enterphone).send_keys(number)

    @allure.step('Enter Number of candidates per time slot')
    def enterNumpeoplePTS(self, num):
        self.browser.find_element(*self.entermaxpeople).send_keys(num)

    @allure.step('Select Calendar to Schedule max appointment per time')
    def selectMaxappointment(self):
        sel = Select(self.browser.find_element(*self.dropdown))
        sel.select_by_value('3')

    @allure.step('Enter Appointment name in search box to search and link ')
    def enterAppointmentName(self, app_name):
        self.browser.find_element(*self.searchbox).send_keys(app_name)

    @allure.step('Select Appointment to link with Calendar after Filter')
    def slectAppwidCal(self):
        # WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.selectApp))
        self.browser.find_element(*self.selectApp).click()

    @allure.step('Click Add Calendar with linking Appointment ')
    def clickaddCalwidAppBtn(self):
        self.browser.find_element(*self.addBtn).click()

    @allure.step('Click Update Button to edit Calendar')
    def clickUpdatebtn(self):
        self.browser.find_element(*self.updateBtn).click()

    @allure.step('CLick Setting Button on Calendar Dashboard to edit calendar')
    def clickSettingtoEdit(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 10, ignored_exceptions).until(EC.presence_of_element_located(self.alert))
        self.browser.find_element(*self.calEdit).click()

    @allure.step('Verify Alert that consist success message ')
    def verifyAlert(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 10, ignored_exceptions).until(EC.presence_of_element_located(self.alert))
        alert = self.browser.find_element(*self.alert).text
        return alert

    @allure.step('Accept confirmation alert for delete Caledar')
    def acceptAlerttodelete(self):
        self.browser.find_element(*self.deleteBtnYes).click()

    @allure.step('Click on Delete Button ')
    def clickDeletebtn(self):
        self.browser.find_element(*self.deleteBtn).click()













