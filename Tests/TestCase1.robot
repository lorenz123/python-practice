*** Settings ***
Documentation    This is my first test case
Library    OperatingSystem

*** Keywords ***
Log My Username
    Log     This is my username - ${MY_DICTIONARY}[username]

Log My Password
    Log     This is my password - ${MY_DICTIONARY}[password]

Log Username And Password 1
    Log     This is my username - ${MY_DICTIONARY}[username]
    Log     This is my password - ${MY_DICTIONARY}[password]

Log Username And Password 2
    Log My Username
    Log My Password

Log My Specific Username
    [Arguments]    ${USERNAME}
    Log            ${USERNAME}

Log My Specific Password
    [Arguments]    ${PASSWORD}
    Log            ${PASSWORD}

Log My Specific Username And Password
    [Arguments]    ${USERNAME}  ${PASSWORD}
    Log            ${USERNAME} - ${PASSWORD}

Log My Specific Username And Password 2
    [Arguments]    ${USERNAME}  ${PASSWORD}
    Log My Specific Username    ${USERNAME}
    Log My Specific Password    ${PASSWORD}


*** Variables ***
${MY_VARIABLE}      my test variable
@{MY_LIST}      test1   test2  test3
&{MY_DICTIONARY}        username=test123    password=Aaaa1234#
&{MY_DICTIONARY2}        username=test321    password=Aaaa321#

*** Test Cases ***
TEST
    [Tags]    demo1
    Log     This is ${MY_VARIABLE} a sample test case
    Log     This is ${MY_LIST} a sample test case
    Log     This is ${MY_LIST}[0] a sample test case
    Log     This is ${MY_DICTIONARY} a sample test case
    Log My Username
    Log My Password
    Log Username And Password 1
    Log Username And Password 2
    Log My Specific Username        ${MY_DICTIONARY}[username]
    Log My Specific Username        ${MY_DICTIONARY2}[username]
    Log My Specific Username And Password   ${MY_DICTIONARY2.username}  ${MY_DICTIONARY2.password}
    Log My Specific Username And Password 2     ${MY_DICTIONARY2.username}  ${MY_DICTIONARY2.password}
