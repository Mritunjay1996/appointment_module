from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from resources.variables import *
import allure, time
from selenium.webdriver.common.action_chains import ActionChains


class mailinatorPageObj:
    # url = "https://www.mailinator.com/v3/index.jsp?zone=public&query=curtis#/#inboxpane"
    url = "https://www.mailinator.com/"
    search_box = (By.XPATH, "//input[@id='addOverlay']")
    goBtn = (By.XPATH, "//button[@id='go-to-public']")
    # link = (By.XPATH, "//a[contains(text(),'https://link.jobrock.com/a0b925a')]")
    link = (By.XPATH, "//div[contains(text(),'"+ unbounce_email + "')]/following-sibling::div[3]/a[1]")
    # initialMail = (By.XPATH, "//a[contains(text(),'initial Mail')]")
    # initialMail = (By.XPATH, "//a[contains(text(),'initial Appointment Mail')]")
    initialMail = (By.XPATH, "//a[contains(text(),'Invite Appointment Email- krishna camp')]")
    selectDate = (By.XPATH, "//span[contains(text(),'" + crrnt_date + "')]/parent::p/parent::div/parent::div"
                                                                      "/following-sibling::div[1]/div[1]/p[1]/span[1]")
    timeslot = (By.XPATH, "//div[@class='selectday bottom']//div[1]//div[1]//span[1]/button[1]")
    move_timeslot = (By.XPATH, "//div[@class='selectday bottom']//div[1]//div[1]//span[1]/button[2]")
    cnfrmBtn = (By.XPATH, "//button[@class='btn btn-block blue']")
    cancelBtn = (By.XPATH, "//a[contains(text(),'Afspraak afzeggen')]")
    moveBtn = (By.XPATH, "//button[contains(text(),'Afspraak verzetten')]")
    alert = (By.XPATH, "//div[@class='sn-title']")
    ifrme = (By.XPATH, "//iframe[@id='msg_body']")
    date_sel = (By.XPATH, "//span[@class='cal-day-badge']/following-sibling::span[contains(text(),'28')]")
    bfr_xpath = "//span[@class='cal-day-badge']/following-sibling::span[contains(text(),'"
    aftr_xpath = "')]"
    show = (By.XPATH, "//span[contains(text(),'Laten zien')]")
    recruiter_month = (By.XPATH, "//button[@class='btn no-btn']")
    nextmonth_arrow = (By.XPATH, "//a[@class='btn no-btn']//i[@class='fa fa-angle-right']")
    selDatepop = (By.XPATH, "//span[@class='cal-day-badge activeColor']/following-sibling::span[text()='28']")
    mail_month = (By.XPATH, "//div[@class='selectday top']/h2[1]")
    time_mail = (By.XPATH, "//div[@class='ins']/h2[1]")
    before = "//span[contains(text(),'"
    after = "')]/parent::p/following-sibling::p/span[2]"
    before1 = "//span[@class='cal-day-badge activeColor']/following-sibling::span[text()='"
    after1 = "']"
    firstRow = (By.XPATH, "//table[@class='table table-striped jambo_table']/tbody/tr[1]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Open Url for mailinator')
    def openMailinator(self):
        # self.browser.execute_script("window.open('');")
        # time.sleep(3)
        # self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get(self.url)
        time.sleep(3)

    @allure.step('Enter email into mailinator to search appointment ')
    def enterEmailinmailinator(self, em):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.search_box))
        self.browser.find_element(*self.search_box).send_keys(em)

    @allure.step('Click on go to public ')
    def clickGopublic(self):
        self.browser.find_element(*self.goBtn).click()

    @allure.step('Click on link to schedule appointment ')
    def clickLinktoSchedule(self):
        iframe = self.browser.find_element(*self.ifrme)
        self.browser.switch_to.frame(iframe)
        time.sleep(2)
        linkk = self.browser.find_element(*self.link).get_attribute('href')
        print("Link is :" + linkk)
        self.browser.find_element_by_xpath("//a[contains(text(),'" + str(linkk) + "')]").click()
        time.sleep(4)
        self.browser.switch_to.default_content()

    @allure.step('Click on Initial Mail')
    def clickInitialMail(self):
        # WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.initialMail))
        first = self.browser.find_element(*self.firstRow).text
        spl = first.split()
        listToStr = ' '.join(map(str, spl[1:3]))
        print(listToStr)
        self.browser.find_element_by_xpath("//a[contains(text(),'" + str(listToStr) + "')]").click()

        # initial = self.browser.find_element(*self.initialMail)
        # self.browser.execute_script("arguments[0].click();", initial)

    @allure.step('Verify Page title ')
    def verifyPagetitle(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        time.sleep(2)
        return self.browser.title

    @allure.step('Click on Next date to scheduled appointment ')
    def clickdatetoSchedule(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.selectDate))
        self.browser.find_element(*self.selectDate).click()

    @allure.step('Select time slot to scheduled appointment')
    def selectTimeslot(self):
        self.browser.find_element(*self.timeslot).click()

    @allure.step('Click on confirm button ')
    def clickConfirmbtn(self):
        self.browser.find_element(*self.cnfrmBtn).click()

    @allure.step('Click on cancel button to cancel appointment ')
    def clickCancelAppBtn(self):
        # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.cancelBtn))
        self.browser.find_element(*self.cancelBtn).click()

    @allure.step('Click on Move Appointment Button ')
    def clickMoveAppBtn(self):
        time.sleep(4)
        global act_time
        tim = self.browser.find_element(*self.time_mail).text
        tim1 = str(tim).split(',')
        tim2 = tim1[2][1 : : ]
        tim3 = tim2.split('-')
        tim4 = tim3[0]
        tim5 = tim4.split(':')
        act_time = tim5[0]
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.moveBtn))
        self.browser.find_element(*self.moveBtn).click()

    @allure.step('Click time slot to move appointment ')
    def clickTimetomoveSlot(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.move_timeslot))
        self.browser.find_element(*self.move_timeslot).click()

    @allure.step('Verify message of alert for successfully appointment')
    def verifyAlertsuccess(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 10, ignored_exceptions).until(EC.presence_of_element_located(self.alert))
        return self.browser.find_element(*self.alert).text

    # @allure.step('Switch to Appointment window ')
    # def switchToappo(self):
    #     time.sleep(2)
    #     self.browser.close()
    #     time.sleep(3)
    #     # Switch back to the first tab
    #     self.browser.switch_to.window(self.browser.window_handles[1])
    #     time.sleep(2)
    #     self.browser.close()
    #     time.sleep(3)
    #     # Switch back to the first tab
    #     self.browser.switch_to.window(self.browser.window_handles[0])

    @allure.step('Get the selected date ')
    def getSeldate(self):
        global appBook_date, monthname
        appBook = self.browser.find_element(*self.selectDate).text
        monthname = self.browser.find_element(*self.mail_month).text
        if int(appBook) < 10:
            appbuk = appBook[1 : : ]
            appBook_date = appbuk
        else:
            appBook_date = appBook

    @allure.step('Get and click on Date to select ')
    def getAndselect(self):
        rec_month = self.browser.find_element(*self.recruiter_month).text
        splt = (rec_month.split(" ", 1))[1]
        if str(monthname) == splt:
            self.browser.find_element_by_xpath(self.bfr_xpath + str(appBook_date) + self.aftr_xpath).click()
        else:
            self.browser.find_element(*self.nextmonth_arrow).click()
            time.sleep(5)
            # self.browser.find_element(*self.date_sel).click()
            self.browser.find_element_by_xpath(self.bfr_xpath + str(appBook_date) + self.aftr_xpath).click()

    @allure.step('Select Date in Popup Calendar ')
    def clickDateinPopup(self):
        day = self.browser.find_element_by_xpath(self.before1 + str(appBook_date) + self.after1 )
        day.click()

    @allure.step('Click on show button to expand ')
    def clickShowbutton(self):
        cal = self.browser.find_element_by_xpath( self.before + act_time + self.after)
        cal.click()






