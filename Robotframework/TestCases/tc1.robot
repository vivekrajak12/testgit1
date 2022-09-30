*** Settings ***

Library  seleniumlibrary
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.google.com
${browser}  chrome

*** Test Cases ***
Google
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    sleep   10
    Close Browser


*** Keywords ***
