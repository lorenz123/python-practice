*** Settings ***

*** Variables ***
&{MY_DICTIONARY2}        username=test321    password=Aaaa321#

*** Keywords ***
Log My Specific Username
    [Arguments]    ${USERNAME}
    Log            ${USERNAME}

Log My Specific Password
    [Arguments]    ${PASSWORD}
    Log            ${PASSWORD}

Log My Specific Username And Password 2
    [Arguments]    ${USERNAME}  ${PASSWORD}
    Log My Specific Username    ${USERNAME}
    Log My Specific Password    ${PASSWORD}