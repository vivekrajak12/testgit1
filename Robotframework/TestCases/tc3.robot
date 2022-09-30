*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${url}      https://flipkart.com
${browser}      chrome

*** Test Cases ***
Validationtestcase
    open browser    ${url}      ${browser}
    maximize browser window
    title should be    Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!
    ${input_text}      set variable    xpath:/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input
    element should be enabled    ${input_text}
    element should be visible    ${input_text}
    input text      ${input_text}       vivek@g.com
    sleep    3
    clear element text    xpath:/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input
    sleep    3
    close browser




*** Keywords ***
