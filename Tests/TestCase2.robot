*** Settings ***
Library    OperatingSystem
Resource    ../Resource/resources.robot

*** Keywords ***


*** Variables ***

*** Test Cases ***
TEST2
    [Tags]    demo2
    Log My Specific Username And Password 2     ${MY_DICTIONARY2.username}  ${MY_DICTIONARY2.password}