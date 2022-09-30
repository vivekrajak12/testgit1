*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${url}  https://www.techlistic.com/p/selenium-practice-form.html
${browser}  chrome
*** Test Cases ***
checkbox_radiobutton
    open browser    ${url}      ${browser}
    maximize browser window
    set selenium speed    2

    #radiobutton
    select radio button    sex      Female
    select radio button    exp      4


    #select check boxes
    select checkbox    Manual Tester
    select checkbox    QTP
    select checkbox    Selenium Webdriver
    unselect checkbox  Selenium Webdriver
    close browser


*** Keywords ***
