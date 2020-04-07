import allure, time
from pages.home_page import homePageObj
from resources.variables import *
from pages.appointment_summary import appointmentsummaryObj
from pages.mailinator_page import mailinatorPageObj
from pages.unbounces_page import unbouncesObj


@allure.title('TC_15: To verify User can insert lead from unbounces page ')
def test_lead_unbounce(browser):
    lead = unbouncesObj(browser)
    lead.load_unbounce()
    time.sleep(3)
    lead.enterFirstname(unbounce_fname)
    lead.enterLastname(unbounce_lname)
    lead.enterEMail(unbounce_email)
    lead.enterPhone(unbounce_phone + "123")
    time.sleep(2)
    lead.enterPostalcode(unbounce_post)
    lead.selectClientname("Aethon")
    time.sleep(1)
    lead.selectSourcetype("Campaign")
    time.sleep(1)
    lead.enterSourceid("camp-875")
    lead.enterHousenumber(unbounce_hnum)
    time.sleep(2)
    lead.clickReactbutton()
    time.sleep(3)
    assert lead.verifySuccessmsg() == "Bedankt!", "After clicking on react success message should be open in popup "
    lead.clickCancelbutton()
    time.sleep(10)


@allure.title('TS_16: To verify schedule, reschedule and cancel appointment using mailinator ')
def test_appointment_schedule(browser):
    mail = mailinatorPageObj(browser)
    mail.openMailinator()
    time.sleep(80)
    # time.sleep(3)
    mail.enterEmailinmailinator(unbounce_email)
    mail.clickGopublic()
    time.sleep(3)
    mail.clickInitialMail()
    time.sleep(4)
    mail.clickLinktoSchedule()
    time.sleep(3)
    assert mail.verifyPagetitle() == "Appointment Scheduler", "Page title is showing wrong. title should be " \
                                                              "Appointment Scheduler "
    mail.clickdatetoSchedule()
    mail.selectTimeslot()
    time.sleep(2)
    mail.getSeldate()
    time.sleep(2)
    mail.clickConfirmbtn()
    time.sleep(1)
    assert mail.verifyAlertsuccess() == "Appointment has been made", "After clicking on confirm button Appointment " \
                                                                     "has been made message should be displayed. "
    time.sleep(2)
    mail.clickMoveAppBtn()
    mail.clickTimetomoveSlot()
    time.sleep(2)
    mail.clickConfirmbtn()
    time.sleep(1)
    assert mail.verifyAlertsuccess() == "Appointment has been made", "After clicking on confirm button Appointment " \
                                                                     "has been made message should be displayed. "
    time.sleep(4)
    mail.clickCancelAppBtn()
    time.sleep(1)
    assert mail.verifyAlertsuccess() == "Appointment has been canceled", "After clicking on cancel button Appointment " \
                                                                         "has been canceled message should be " \
                                                                         "displayed. "
    time.sleep(5)
    mail.clickdatetoSchedule()
    mail.selectTimeslot()
    time.sleep(1)
    mail.clickConfirmbtn()
    assert mail.verifyAlertsuccess() == "Appointment has been made", "After clicking on confirm button Appointment " \
                                                                     "has been made message should be displayed. "
    time.sleep(5)
    # mail.switchToappo()
    # time.sleep(2)


@allure.title('TC_17: To verify Recruiter can Reschedule and cancel the booked appointment .')
def test_cancel_bookedapp(browser):
    cancel = appointmentsummaryObj(browser)
    mail = mailinatorPageObj(browser)
    home_page = homePageObj(browser)
    home_page.load()
    home_page.enterUsername(recruiter_username)
    home_page.clickNextButton()
    time.sleep(2)
    home_page.enterPassword(recruiter_password)
    home_page.clickSigninButton()
    time.sleep(2)
    home_page.clickStaysignedIN()
    time.sleep(2)
    assert home_page.verifyPageTitle() == "Aethon", "After login, Aethon page is not opening. Aethon page should be " \
                                                    "open. "
    home_page.clickAppointmenttab()
    time.sleep(10)
    cancel.selectMonth()
    cancel.selectOffice()
    time.sleep(2)
    # mail.getSeldate()
    mail.getAndselect()
    time.sleep(2)
    mail.clickShowbutton()
    time.sleep(2)
    cancel.clickCalendaricon()
    time.sleep(5)
    mail.clickDateinPopup()
    time.sleep(4)
    cancel.clickTimslotPop()
    cancel.clickResedulebtn()
    time.sleep(1)
    assert mail.verifyAlertsuccess() == "succesvol geupdatet", "After rescheduling success message is not showing."
    time.sleep(4)
    cancel.clickCancelicon()
    time.sleep((3))
    assert cancel.verifyCancelPage() == "Weet je zeker dat je deze afspraak wilt annuleren?", "Cancel pop up is not " \
                                                                                              "opening after clicking" \
                                                                                              " on cancel icon "
    time.sleep(2)
    cancel.clickCancelbuttonpop()
    time.sleep(1)
    assert mail.verifyAlertsuccess() == "Kalender is geannuleerd", " After cancel success message is not showing. "
    time.sleep(5)






