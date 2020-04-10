import allure, time
from pages.home_page import homePageObj
from pages.appointment import AppointmentObj
from resources.variables import *
from pages.block_off_calnedar import blockoffCalendarObj
from pages.appointment_type_dashboard import appDashboardObj
from pages.add_appointment_type import addAppointmentypeObj
from pages.appointment_calendar_dashboard import appCalendarDashbrdObj
from pages.add_calendar import addCalendarObj
from pages.move_active import moveActiveObj


@allure.title('TS_01: To verify UI elements present on Dashboard page')
def test_homepage(browser):
    home_page = homePageObj(browser)
    appointment = AppointmentObj(browser)
    home_page.load()
    home_page.enterUsername(recruiter_username)
    home_page.clickNextButton()
    time.sleep(2)
    home_page.enterPassword(recruiter_password)
    home_page.clickSigninButton()
    time.sleep(7)
    home_page.clickStaysignedIN()
    time.sleep(2)
    assert home_page.verifyPageTitle() == "Aethon", "After login, Aethon page is not opening. Aethon page should be " \
                                                    "open. "
    assert home_page.verifyBusinesslogo() == True, "Business Logo is displaying . Business logo should be on top of " \
                                                   "Page. "
    assert home_page.verifyProfileimage() == True, "Recruiter Profile image is not showing. Profile image should be " \
                                                   "displayed. "
    assert home_page.verifyProfilename() == "Automation Script", "Recruiter Profile name is not displaying . Profile " \
                                                                 "name should be there. "
    time.sleep(2)
    assert home_page.verifydropdownoption1() == "Mijn profiel", "Mijn profiel is not present in Recruiter Dropdown " \
                                                                "option. "
    assert home_page.verifydrpodownoption2() == "Uitloggen", "Uitloggen is not present in Recruiter Dropdown Options. "
    assert home_page.verifyAppointmentab() == True, "Appointment tab is not present on Aethon Page. Appointment Tab " \
                                                    "should be displayed . "
    time.sleep(2)
    assert home_page.verifyAppointment_calendar() == True, "Calendar option is not present in Appointment dropdown " \
                                                           "list. Calendar option should be there. "
    assert home_page.verifyAppointment_teamcal() == True, "Team Calendar option is not present in Appointment " \
                                                          "dropdown list. Team Calendar option should be in " \
                                                          "appointment tab. "
    assert home_page.verifyAppointment_appointType() == True, "Appointment type option show be in appointment " \
                                                              "dropdown list "
    assert home_page.verifyAppointment_emailSms() == True, "Email & SMS Template is not showing, Email & SMS Template " \
                                                           "should be present in appointment dropdown list. "
    time.sleep(3)
    home_page.clickAppointmenttab()
    time.sleep(5)
    assert appointment.verifyDaybutton() == "Dag", "Day Button in aethon appointment scheduler is displaying . Day " \
                                                   "should be present. "
    assert appointment.verifyWeekbutton() == "Week", "Day Button in aethon appointment scheduler is displaying . Day " \
                                                     "should be present. "
    assert appointment.verifyMonthbutton() == "Maand", "Day Button in aethon appointment scheduler is displaying . " \
                                                       "Day should be present. "
    assert appointment.verifyOffice_dropdown() == True, "Office dropdown is not displaying on aethon appointment " \
                                                        "scheduler Page. "
    assert appointment.verifyResumeheading() == "Samenvatting", "Resume heading is not displaying below office " \
                                                                "dropdown . "
    time.sleep(2)
    assert appointment.verifysideBar1() == "afspraken", "Side menu bar does not have 'afspraken'. afspraken should be " \
                                                        "in side menu bar. "
    assert appointment.verifysideBar2() == "Afspraaktype", "Side menu does not have 'Afspraaktype'. Afspraaktype " \
                                                           "should be in side menu bar. "
    assert appointment.verifysideBar3() == "Agenda's", "Side menu bar does not have Agenda's. Agenda's should be in " \
                                                       "side menu bar. "
    time.sleep(1)
    assert appointment.verifysideBar4() == "Teamagenda", "Side menu bar does not have 'Teamagenda'. Teamagenda should " \
                                                         "be in side menu bar. "
    assert appointment.verifysideBar5() == "E-mail-en SMS-sjablonen", "Side menu bar does not have 'E-mail-en " \
                                                                      "SMS-sjablonen'. E-mail-en SMS-sjablonen should " \
                                                                      "be in side menu bar. "
    time.sleep(2)


@allure.title('TS_02: To verify UI elements for  Appointment types ')
def test_verifyui_appointmentype(browser):
    app_dash = appDashboardObj(browser)
    ui = addAppointmentypeObj(browser)
    ui.clickAppointmentypes()
    time.sleep(7)
    assert app_dash.verifyBusslogo() == True, "Business Logo is displaying . Business logo should be on top of Page. "
    assert app_dash.verifyProfileimage() == True, "Recruiter Profile image is not showing. Profile image should be " \
                                                  "displayed. "
    assert app_dash.verifyProfilename() == profile_name, "Recruiter Profile name is not displaying . Profile name " \
                                                         "should be there. "
    time.sleep(2)
    assert app_dash.verifydropdownoption1() == "Mijn profiel", "Mijn profiel is not present in Recruiter Dropdown " \
                                                               "option. "
    assert app_dash.verifydropdownoption2() == "Taal", "Language option in Recruiter profile is not present . " \
                                                       "Language should be displayed in list. "
    assert app_dash.verifydrpodownoption3() == "Log Out", "Log Out is not present in Recruiter Dropdown Options. "
    assert app_dash.verifyAppPageLabel() == "Alle afspraak-types", "After clicking on Back to my appointment link ," \
                                                                   "Appointment Page should be open. "
    assert app_dash.verifyappTab() == True, "Appointment tab should be displayed on Appointment type Dashboard Page"
    assert app_dash.verifyOfficedrpdwon() == True, "Office Dropdown should be displayed and enabled."
    time.sleep(2)
    assert app_dash.verifysideBar1() == "afspraken", "Side menu bar does not have 'afspraken'. afspraken should be in " \
                                                     "side menu bar. "
    assert app_dash.verifysideBar2() == "Afspraaktype", "Side menu does not have 'Afspraaktype'. Afspraaktype should " \
                                                        "be in side menu bar. "
    assert app_dash.verifysideBar3() == "Agenda's", "Side menu bar does not have Agenda's. Agenda's should be in side " \
                                                    "menu bar. "
    time.sleep(1)
    assert app_dash.verifysideBar4() == "Teamagenda", "Side menu bar does not have 'Teamagenda'. Teamagenda should be " \
                                                      "in side menu bar. "
    assert app_dash.verifysideBar5() == "E-mail-en SMS-sjablonen", "Side menu bar does not have 'E-mail-en " \
                                                                   "SMS-sjablonen'. E-mail-en SMS-sjablonen should be " \
                                                                   "in side menu bar. "


@allure.title('TS_03: To verify UI elements present on  Add appointment type page')
def test_addappoinment_ui(browser):
    ui = addAppointmentypeObj(browser)
    time.sleep(8)
    browser.refresh()
    time.sleep(5)
    ui.clickAddAppointmentype()
    time.sleep(2)
    assert ui.verifyAppointmentName() == True, "Appointment name option is not present on Appointment Type. Option " \
                                               "for name should be present. "
    assert ui.verifyAppointmentDescription() == True, "Option for Appointment Description is not present . " \
                                                      "Description should be there. "
    assert ui.verifyMessageConfirmation() == True, "Confirmation message option is not there. Confirmation message " \
                                                   "option should be present . "
    assert ui.verifyDuration() == True, "Duration option is not there. it should be present."
    assert ui.verifyExtraTime() == True, "Extra Time option is not showing there . option should be on Add " \
                                         "appointment Form. . "
    assert ui.verifyCategoryDropdown() == True, "Category Dropdown is not displaying in Form. It should be present ."
    assert ui.verifyAddnewCategory() == True, "Add new Category is not displaying . option should be there."
    assert ui.verifyokButton() == True, "Ok button should be enabled for adding category. "
    assert ui.verifyColorCode() == True, "Label for Color code not showing up there. Color code should display on page."
    assert ui.verifyMaxPeopleAllowed() == True, "Maximum People allowed option not displayed . Maximum People allowed " \
                                                "option should be present. "
    assert ui.verifyavailAppoint() == True, "Radio Button with Availability mode for appointment based should displayed"
    assert ui.verifyavailVast() == True, "Radio Button with Availability mode for Vast based should displayed. "
    assert ui.verifyLinkappointment() == True, "Label for Link existing calendar is not present .option should be show."
    assert ui.verifyAddButton() == True, "Add button is not displaying . Add Button should be enabled . "
    assert ui.verifyCancelButton() == True, "Cancel button is not displaying . Cancel Button should be enabled . "
    assert ui.verifyBackToappointment() == True, "Link to go back on appointment type page should be present. "


@allure.title('TS_04: To verify Recuiter is able to add appointment type using Add Apointment Type button ')
def test_addAppointment_type(browser):
    time.sleep(2)
    add = addAppointmentypeObj(browser)
    app_dshbrd = appDashboardObj(browser)
    add.enterAppointmentName(appointment_name)
    time.sleep(1)
    add.enterAppointmentDescription("Description added by Automation")
    add.enterConfirmationMsg("Appointment confirmed")
    time.sleep(1)
    add.enterAppointmentDuration("30")
    add.enterAppointmentextraTime("10")
    time.sleep(1)
    add.selectCategoryDropdown("Automation_Category")
    add.enterMaxallowed("1")
    add.selectAvailability()
    time.sleep(1)
    assert add.verifyLinkappointment() == True, "With selecting Appointment availability ,Label for Link existing " \
                                                "calendar is not showing . Option should be show. "
    add.clickAddButton()
    time.sleep(5)
    # add.clickBackmyAppointment()
    # time.sleep(4)
    assert add.verifyAppPageheading() == "Alle afspraak-types", "After clicking on Back to my appointment link , " \
                                                                "Appointment Page should be open. "
    time.sleep(2)
    assert app_dshbrd.verify_availAddedapp() == "Niet beschikbaar", "Availibility for added appointment type is not " \
                                                                    "showing . availablity should show . "
    assert app_dshbrd.verify_editAddedapp() == "Bewerken", "Edit option for added appointment is not showing " \
                                                           ".'Bewerken' should shown "
    assert app_dshbrd.verify_tocopyAddedapp() == "Kopiëren", "To copy option for added appointment is not showing.' " \
                                                              "Kopiëren' should shown "


@allure.title('TS_05: To verify that  Reccuiter should be able to  update and delete existing Appointment Type.')
def test_update_apptype(browser):
    add = addAppointmentypeObj(browser)
    app_dshbrd = appDashboardObj(browser)
    time.sleep(4)
    browser.refresh()
    time.sleep(5)
    add.clickAddAppointmentype()
    time.sleep(2)
    add.enterAppointmentName(edit_appointment)
    time.sleep(3)
    add.enterAppointmentDescription("Description added by Automation")
    add.enterConfirmationMsg("Appointment confirmed")
    time.sleep(1)
    add.enterAppointmentDuration("30")
    add.enterAppointmentextraTime("10")
    time.sleep(1)
    add.selectCategoryDropdown("Automation_Category")
    add.enterMaxallowed("1")
    add.selectAvailability()
    time.sleep(1)
    assert add.verifyLinkappointment() == True, "With selecting Appointment availability ,Label for Link existing " \
                                                "calendar is not showing . Option should be show. "
    add.clickAddButton()
    time.sleep(5)
    add.clickAddAppointmentype()
    time.sleep(2)
    add.enterAppointmentName(edit_appointment + '2')
    time.sleep(3)
    add.enterAppointmentDescription("Description added by Automation for multiple calendar ")
    add.enterConfirmationMsg("Appointment confirmed")
    time.sleep(1)
    add.enterAppointmentDuration("30")
    add.enterAppointmentextraTime("10")
    time.sleep(1)
    add.selectCategoryDropdown("Automation_Category")
    add.enterMaxallowed("1")
    add.selectAvailability()
    time.sleep(1)
    assert add.verifyLinkappointment() == True, "With selecting Appointment availability ,Label for Link existing " \
                                                "calendar is not showing . Option should be show. "
    add.clickAddButton()
    time.sleep(3)
    app_dshbrd.clickeditBtn()
    time.sleep(5)
    # add.editAppointmentName(edit_appointment + "2")
    # add.clickOfficeRadio()
    app_dshbrd.clickUpdatebtn()
    time.sleep(1)
    assert app_dshbrd.verifyAlert() == "Afspraaktypes bijgewerkt", "Alert is not coming after updating appointment " \
                                                                   "type. "
    app_dshbrd.clickeditBtn()
    time.sleep(3)
    app_dshbrd.clickDeletebtn()
    time.sleep(2)
    app_dshbrd.acceptAlerttodelete()
    time.sleep(1)
    assert app_dshbrd.verifyAlert() == "Afspraaktype is verwijderd", "Alert is not showing Afspraaktype is verwijderd " \
                                                                     " message after updating appointment type. "


@allure.title('TS_06: To verify UI elements present on Appointment Calendar')
def test_calendar_ui(browser):
    cal_dash = appCalendarDashbrdObj(browser)
    cal_dash.clickCalendar()
    time.sleep(4)
    app_dash = appDashboardObj(browser)
    assert cal_dash.verifyappTab() == True, "Appointment Tab should be shown on Calendar Dashboard Page"
    assert cal_dash.verifycalendarLogo() == True, "Business Logo is not displaying on Calendar Page. Business logo " \
                                                  "should be on top of Page. "
    assert cal_dash.verifyProfileimage() == True, "Recruiter Profile image is not showing. Profile image should be " \
                                                  "displayed. "
    assert cal_dash.verifyProfilename() == profile_name, "Recruiter Profile name is not displaying . Profile name " \
                                                         "should be there. "
    time.sleep(2)
    assert cal_dash.verifydropdownoption1() == "Mijn profiel", "Mijn profiel is not present in Recruiter Dropdown " \
                                                               "option. "
    assert cal_dash.verifydropdownoption2() == "Taal", "Language option in Recruiter profile is not present . " \
                                                       "Language should be displayed in list. "
    assert cal_dash.verifydrpodownoption3() == "Log Out", "Log Out is not present in Recruiter Dropdown Options. "
    assert cal_dash.verifyCalLabel() == "Agenda", "After clicking on Back to my appointment link Appointment Page " \
                                                  "should be open. "
    assert cal_dash.verifyappTab() == True, "Appointment tab should be displayed on Appointment type Dashboard Page"
    assert cal_dash.verifyOfficedrpdwon() == True, "Office Dropdown should be displayed and enabled."
    time.sleep(2)
    assert app_dash.verifysideBar1() == "afspraken", "Side menu bar does not have 'afspraken'. afspraken should be in " \
                                                     "side menu bar. "
    assert app_dash.verifysideBar2() == "Afspraaktype", "Side menu does not have 'Afspraaktype'. Afspraaktype should " \
                                                        "be in side menu bar. "
    assert app_dash.verifysideBar3() == "Agenda's", "Side menu bar does not have Agenda's. Agenda's should be in side " \
                                                    "menu bar. "
    time.sleep(1)
    assert app_dash.verifysideBar4() == "Teamagenda", "Side menu bar does not have 'Teamagenda'. Teamagenda should be " \
                                                      "in side menu bar. "
    assert app_dash.verifysideBar5() == "E-mail-en SMS-sjablonen", "Side menu bar does not have 'E-mail-en " \
                                                                   "SMS-sjablonen'. E-mail-en SMS-sjablonen should be " \
                                                                   "in side menu bar. "


@allure.title('TS_07: To verify UI elements present on Add new Appointment Calendar POPUP for Calendar availablilty')
def test_addcal_availableUi(browser):
    add_cal = addCalendarObj(browser)
    time.sleep(2)
    add_cal.clickAddcalendar()
    time.sleep(2)
    assert add_cal.verifyAvailbtn() == True, "Available button should be present on Add new appointment Calendar. "
    assert add_cal.verifySettingbtn() == True, "Setting button should be present on Add new appointment Calendar. "
    assert add_cal.verifyCrossbtn() == True, "Cross button should be present on Add Calendar to close popup. "
    assert add_cal.verifyBackappcal() == True, "Back to appointment link should be present on Add new appointment " \
                                               "Calendar to go on BAck to calendar dashboard page. "
    assert add_cal.verifyNormwrkhr() == True, "Option for normal working is not showing . should be displayed on Page. "
    assert add_cal.verifyDaysoff() == True, "Days off option is not showing.It should display on available add calendar"
    assert add_cal.verifyMondayoff() == True, "Days off for Monday is not showing in week days list. should be display."
    assert add_cal.verifyTuesoff() == True, "Days off for Tuesday is not showing in week days list. should be display."
    assert add_cal.verifyWedoff() == True, "Days off for Wednesday is not showing in week days list. should be display."
    assert add_cal.verifyThursoff() == True, "Days off for Thursday is not showing in week days list. should be display"
    assert add_cal.verifyFrioff() == True, "Days off for Friday is not showing in week days list. should be display."
    assert add_cal.verifySatoff() == True, "Days off for Saturday is not showing in week days list. should be display."
    assert add_cal.verifySundayoff() == True, "Days off for Sunday is not showing in week days list. should be display."
    assert add_cal.verifyApplybtn() == True, "Apply button is not showing. should be displayed."
    assert add_cal.verifyPrevbtn() == True, "Previous Button is not showing . Prev button should be displayed. "
    assert add_cal.verifyNextbtn() == True, "Next button is not showing on Add cal page. should be displayed."
    assert add_cal.verifyCancelbtn() == True, "Cancel button is not showing on Add cal page. should be displayed."
    assert add_cal.verifyAddbtn() == True, "Add button is not showing on Add calendar page. should be displayed."
    time.sleep(2)


@allure.title('TS_08: To verify UI elements present on Add new Appointment Calendar POPUP for Calendar Setting')
def test_addcal_settingUi(browser):
    add_cal1 =  addCalendarObj(browser)
    add_cal1.clickSettingbtn()
    time.sleep(2)
    assert add_cal1.verifyagendaTitle() == True, "Agenda Title should be present on Add calendar setting page. "
    assert add_cal1.verifyEmail() == True, "Email option should be displayed on Add calendar setting page."
    assert add_cal1.verifyTelephonenum() == True, "Telephone number option should be on Add calendar page. "
    assert add_cal1.verifyCandidatenum() == True, "Option for set number of candidate per time slot should be there. "
    # assert add_cal1.verifydropdownSchedule() == True, "Dropdown for schedule appointment calendar should show"
    assert add_cal1.verifyCalswitchbtn() == True, "Calendar switch button is not displaying on add calendar setting " \
                                                  "page. it should show. "
    time.sleep(2)
    assert add_cal1.verifyCaLinkAppLabel() == True, "Label to link calendar with appointment type is not displaying . " \
                                                    "it should display. "
    assert add_cal1.verifyCompwide() == True, "Company wide option is not showing over there.It should display com wide"
    assert add_cal1.verifyOfficewise() == True, "Office wise option is not showing over there . it should show."
    add_cal1.clickOfficewise()
    assert add_cal1.verifyOfficedropdown() == True, "After selecting office wise Office dropdown is not displaying " \
                                                    "below link to calendar label. "
    time.sleep(1)
    add_cal1.clickCompwide()
    time.sleep(3)
    assert add_cal1.verifyCancelbtn() == True, "Cancel button is not showing on Add cal page. should be displayed."
    assert add_cal1.verifyAddbtn() == True, "Add button is not showing on Add calendar page. should be displayed."
    time.sleep(2)
    add_cal1.clickCrossBtn()
    time.sleep(5)


@allure.title('TS_09: To verify functionality of Add Apointment Calendar')
def test_addcal_functionality(browser):
    add =  addCalendarObj(browser)
    add.clickAddcalendar()
    time.sleep(2)
    assert add.verifyAvailbtnSelected() == "Beschikbaarheid", "After clicking on Add Appointment calendar By default " \
                                                              "available button is not selected. "
    add.enterFromhh("10")
    add.enterFromMM("00")
    add.enterTohh("19")
    add.enterToMM("10")
    add.clickSaturdayoff()
    add.clickSundayoff()
    time.sleep(2)
    add.clickApplybtn()
    time.sleep(2)
    add.clickSettingbtn()
    time.sleep(2)
    add.enterAgendaname(agenda_name)
    add.enterEmailaddress(agenda_email)
    add.enterTelephonenumber("9988776655")
    time.sleep(1)
    add.enterNumpeoplePTS("2")
    add.selectMaxappointment()
    time.sleep(1)
    add.enterAppointmentName(appointment_name)
    time.sleep(8)
    add.slectAppwidCal()
    time.sleep(2)
    add.clickaddCalwidAppBtn()
    time.sleep(4)


@allure.title('TS_10: To verify that Recruiter should be able to update and delete existing Appointment Calendar ')
def test_update_calendar(browser):
    add = addCalendarObj(browser)
    add.clickAddcalendar()
    time.sleep(2)
    assert add.verifyAvailbtnSelected() == "Beschikbaarheid", "After clicking on Add Appointment calendar By default " \
                                                                  "available button is not selected. "
    add.enterFromhh("11")
    add.enterFromMM("00")
    add.enterTohh("20")
    add.enterToMM("10")
    add.clickSaturdayoff()
    add.clickSundayoff()
    time.sleep(2)
    add.clickApplybtn()
    time.sleep(2)
    add.clickSettingbtn()
    time.sleep(2)
    add.enterAgendaname(edit_agenda)
    add.enterEmailaddress(agenda_email)
    add.enterTelephonenumber("9988776655")
    time.sleep(1)
    add.enterNumpeoplePTS("2")
    add.selectMaxappointment()
    time.sleep(2)
    add.clickaddCalwidAppBtn()
    add.clickSettingtoEdit()
    time.sleep(3)
    add.clickUpdatebtn()
    time.sleep(2)
    assert add.verifyAlert() == "Kalender is bijgewerkt", "After Updating Calendar , Success message Kalender is " \
                                                          "bijgewerkt is not showing. "
    add.clickSettingtoEdit()
    time.sleep(3)
    add.clickDeletebtn()
    time.sleep(2)
    add.acceptAlerttodelete()
    assert add.verifyAlert() == "Kalender is verwijderd", "Alert is not showing Kalender is verwijderd  message after " \
                                                          "updating calendar type. "


@allure.title('TS_11: To verify Link of multiple appointment calendars to single appointment type')
def test_multical_singleapp(browser):
    add = addCalendarObj(browser)
    add.clickAddcalendar()
    time.sleep(2)
    assert add.verifyAvailbtnSelected() == "Beschikbaarheid", "After clicking on Add Appointment calendar By default " \
                                                              "available button is not selected. "
    add.enterFromhh("12")
    add.enterFromMM("00")
    add.enterTohh("19")
    add.enterToMM("00")
    add.clickSaturdayoff()
    add.clickSundayoff()
    time.sleep(2)
    add.clickApplybtn()
    time.sleep(2)
    add.clickSettingbtn()
    time.sleep(2)
    add.enterAgendaname(edit_agenda)
    add.enterEmailaddress(agenda_email)
    add.enterTelephonenumber("9988776655")
    time.sleep(1)
    add.enterNumpeoplePTS("2")
    add.selectMaxappointment()
    time.sleep(1)
    add.enterAppointmentName(edit_appointment + '2')
    time.sleep(4)
    add.slectAppwidCal()
    time.sleep(2)
    add.clickaddCalwidAppBtn()
    time.sleep(4)
    add.clickAddcalendar()
    time.sleep(2)
    assert add.verifyAvailbtnSelected() == "Beschikbaarheid", "After clicking on Add Appointment calendar By default " \
                                                              "available button is not selected. "
    add.enterFromhh("09")
    add.enterFromMM("00")
    add.enterTohh("06")
    add.enterToMM("00")
    add.clickSaturdayoff()
    add.clickSundayoff()
    time.sleep(2)
    add.clickApplybtn()
    time.sleep(2)
    add.clickSettingbtn()
    time.sleep(2)
    add.enterAgendaname(edit_agenda + '2')
    add.enterEmailaddress(agenda_email)
    add.enterTelephonenumber("9988776655")
    time.sleep(1)
    add.enterNumpeoplePTS("2")
    add.selectMaxappointment()
    time.sleep(1)
    add.enterAppointmentName(edit_appointment + '2')
    time.sleep(4)
    add.slectAppwidCal()
    time.sleep(2)
    add.clickaddCalwidAppBtn()

#
# @allure.title('TS_12: To verify the Functionality of Block off Calendar')
# def test_blockoff_calendar(browser):
#     block = blockoffCalendarObj(browser)
#     cal_dash = appCalendarDashbrdObj(browser)
#     cal_dash.clickCalendar()
#     time.sleep(4)
#     block.clickBlockoffcal()
#     time.sleep(3)
#     block.selectCurrentdateFrom()
#     block.selectCurrentdateTo()
#     time.sleep(2)
#     block.enterFromhh("12")
#     block.enterFromMM("00")
#     block.enterTohh("13")
#     block.enterToMM("00")
#     time.sleep(2)
#     block.clickAgendaname()
#     time.sleep(1)
#     assert block.verifyMultiblock() == True, "Multiple Block option is not showing on Block off calendar page. "
#     assert block.verifyMonday() == True, "Monday is not displaying in Repet Days option. "
#     assert block.verifyTuesday() == True, "Tuesday is not displaying in Repet Days option. "
#     time.sleep(1)
#     assert block.verifyWednesday() == True, "Wednesday is not displaying in Repet Days option. "
#     assert block.verifyThursday() == True, "Thursday is not displaying in Repet Days option. "
#     assert block.verifyFriday() == True, "Friday is not displaying in Repet Days option. "
#     assert block.verifySaturday() == True, "Saturday is not displaying in Repet Days option. "
#     assert block.verifySunday() == True, "Sunday is not displaying in Repet Days option. "
#     time.sleep(2)
#     block.enterMessage(agenda_name + " is blocked now. ")
#     block.clickBlockbutton()
#     time.sleep(4)


@allure.title('ID 13: To verify UI elements on  email & sms template ')
def test_emailsms_ui(browser):
    ui = moveActiveObj(browser)
    time.sleep(12)
    ui.clickEmailSms()
    time.sleep(3)
    assert ui.verify_emailsms_heading() == "Alle templates", " All Template heading should be displayed in heading "
    assert ui.verifyInitialtab() == "Eerste afspraak", " Initial appointment schedule tab should be displayed in header"
    assert ui.verifyApptconfirmationTab() == "Afspraak bevestiging", " Appointment Confirmation tab should be displayed in header "
    assert ui.verifyApptRemindertab() == "Herinnering", "Appointment Reminder tab should be displayed in header "
    assert ui.verifyReschedulingTab() == "Afspraak verzetten", "Rescheduling tab should be displayed in header "
    assert ui.verifyCancellationtab() == "Annuleren", "Cancellation tab should be displayed in header "
    time.sleep(1)
    assert ui.verifyCheckbox() == True, "Check box for standard should be displayed in header "
    assert ui.verifyEmailtemplate() == "E-mail Template", "Block for Email template should be shown. "
    assert ui.verifySmstemplate() == "SMS-sjabloon", "Block for SMS template should be shown ."
    assert ui.verifySavebutton() == True, "Save button below email and sms template should be displayed "
    assert ui.verifyPreviewbutton() == True, "Preview button should be displayed below email and sms template block "
    assert ui.verifyuseDefaultBtn() == True, "Button for use Default template should be displayed "


@allure.title('ID_14: Move appointments types from inactive to active template in Email and SMS Template. ')
def test_moveinactive_active(browser):
    move = moveActiveObj(browser)
    add = addCalendarObj(browser)
    time.sleep(2)
    move.clickOncheckbox()
    time.sleep(4)
    move.moveInactivetoactive()
    time.sleep(1)
    assert add.verifyAlert() == "E-mailsjabloon gewijzigd", "Email template changed message is not showing after " \
                                                          "changing appointment type template from inactive from " \
                                                          "active. "
    time.sleep(2)
    move.clickSavebutton()
    assert add.verifyAlert() == "Template is gewijzigd", "Template is gewijzigd should be displayed in alert " \
                                                            "after save "
    time.sleep(2)
    move.clickAppointmentConfirm()
    time.sleep(3)
    move.moveInactivetoactive()
    time.sleep(1)
    assert add.verifyAlert() == "E-mailsjabloon gewijzigd", "Email template changed message is not showing after " \
                                                            "changing appointment type template from inactive from " \
                                                            "active. "
    time.sleep(2)
    move.clickSavebutton()
    assert add.verifyAlert() == "Template is gewijzigd", "Template is gewijzigd should be displayed in alert " \
                                                            "after save "
    time.sleep(2)
    move.clickappointmentReminder()
    time.sleep(3)
    move.moveInactivetoactive()
    time.sleep(1)
    assert add.verifyAlert() == "E-mailsjabloon gewijzigd", "Email template changed message is not showing after " \
                                                            "changing appointment type template from inactive from " \
                                                            "active. "
    time.sleep(2)
    move.clickSavebutton()
    assert add.verifyAlert() == "Instellingen gewijzigd", "Instellingen gewijzigd should be displayed in alert " \
                                                            "after save "
    time.sleep(2)
    move.clickReschedulingtab()
    time.sleep(3)
    move.moveInactivetoactive()
    time.sleep(1)
    assert add.verifyAlert() == "E-mailsjabloon gewijzigd", "Email template changed message is not showing after " \
                                                            "changing appointment type template from inactive from " \
                                                            "active. "
    time.sleep(2)
    move.clickSavebutton()
    assert add.verifyAlert() == "Template is gewijzigd", "Template is gewijzigd should be displayed in alert " \
                                                            "after save "
    time.sleep(2)
    move.clickCancellationtab()
    time.sleep(3)
    move.moveInactivetoactive()
    time.sleep(1)
    assert add.verifyAlert() == "E-mailsjabloon gewijzigd", "Email template changed message is not showing after " \
                                                            "changing appointment type template from inactive from " \
                                                            "active. "
    time.sleep(2)
    move.clickSavebutton()
    assert add.verifyAlert() == "Template is gewijzigd", "Template is gewijzigd should be displayed in alert " \
                                                            "after save "
    time.sleep(5)



#
