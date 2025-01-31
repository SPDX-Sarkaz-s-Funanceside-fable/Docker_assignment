*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${SERVER}         localhost:5000
${BROWSER}        Chrome
${DELAY}          0
${VALID USER}     demo
${VALID PASSWORD}    mode
${HOME URL}      http://${SERVER}/
${CONGRATS URL}      http://${SERVER}/congrats

*** Test Cases ***
Open Browser To Home Page
    Open Browser    ${HOME URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Home Page Should Be Open
    Title Should Be    Calculator

Test one plus one
    Click button    //button[13]
    Click Button    //button[8]
    Click Button    //button[13]
    Click Button    //button[12]
    ${text}    Get Text    id=answer
    Should Be Equal    ${text}    2

Go To congrats Page
    Go To    ${CONGRATS URL}
    Title Should Be    Congratulations! 🎉

# Input Username
#     [Arguments]    ${username}
#     Input Text    username_field    ${username}

# Input Password
#     [Arguments]    ${password}
#     Input Text    password_field    ${password}

# Submit Credentials
#     Click Button    login_button

# Welcome Page Should Be Open
#     Location Should Be    ${WELCOME URL}
#     Title Should Be    Welcome Page


# Verify Calculator Addition
#     Open Browser To Home Page
#     Test one plus one