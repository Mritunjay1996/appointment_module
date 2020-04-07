from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure


class appointmentsummaryObj:
    dropdownarow = (By.XPATH, "//div[@class='toggle']")
    oneKOffice = (By.XPATH, "//div[contains(text(),'1000 - Flex Zorg')]")
    cancelBtn = (By.XPATH, "//div[contains(text(),'6000 - Deta Publica')]")
    bukdappCal = (By.XPATH, "//span[@class='cal-day-badge']/following-sibling::span[1]")
    crossBtn = (By.XPATH, "//div[@class='flex-scroll']//i[@class='fa-icon cancel']")
    month = (By.XPATH, "//a[contains(text(),'Maand')]")
    cal_icon = (By.XPATH, "//ul[@class='list-unstyled sub-menu']//i[@class='fa-icon calendar']")
    resedule_rec = (By.XPATH, "//div[@class='timeslot-calc']/div[1]/div[1]/label[9]")
    resedule_btn = (By.XPATH, "//button[@class='btn blue medium closet']")
    cancel_icon = (By.XPATH, "//ul[@class='list-unstyled sub-menu']//i[@class='fa-icon cancel']")
    cancelPage = (By.XPATH, "//h2[@class='title-1']")
    cancel_sbmt = (By.XPATH, "//a[@class='btn blue medium closet']")

    # showBtn =

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Select office to verify booked appointment ')
    def selectOffice(self):
        self.browser.find_element(*self.dropdownarow).click()
        time.sleep(2)
        self.browser.find_element(*self.oneKOffice).click()

    @allure.step('Get Booked appointment date ')
    def getBookedapp(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.bukdappCal))
        date = self.browser.find_elements(*self.bukdappCal)
        print(date)
        # for value in date:
        #     print(value.text)

    @allure.step('Click day which have appointment scheduled ')
    def clickDayinCal(self):
        self.browser.find_element(*self.bukdappCal).click()

    @allure.step('Click cross Button to cancel the boked appointment ')
    def clickCrossbtn(self):
        self.browser.find_element(*self.crossBtn).click()

    @allure.step('Select Month to open Calendar')
    def selectMonth(self):
        # WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.month))
        # WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable(self.month))
        self.browser.find_element(*self.month).click()

    @allure.step('click on calendar icon to reschedule ')
    def clickCalendaricon(self):
        self.browser.find_element(*self.cal_icon).click()

    @allure.step('Click on time slot on pop page to reschedule appointment ')
    def clickTimslotPop(self):
        self.browser.find_element(*self.resedule_rec).click()

    @allure.step('After selecting slot click on button')
    def clickResedulebtn(self):
        self.browser.find_element(*self.resedule_btn).click()

    @allure.step('Click on cancel icon to cancel appointment')
    def clickCancelicon(self):
        self.browser.find_element(*self.cancel_icon).click()

    @allure.step('Verify cancel page is opened ')
    def verifyCancelPage(self):
        return self.browser.find_element(*self.cancelPage).text

    @allure.step('CLick on cancel button in pop ')
    def clickCancelbuttonpop(self):
        self.browser.find_element(*self.cancel_sbmt).click()




