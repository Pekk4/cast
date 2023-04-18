*** Variables ***

*** Settings ***
Resource        ../../resources/common.resource
Suite Setup     ${SETUP}

*** Test Cases ***

Scenario: As a visitor I can see the projects card on profile page
  Refresh & Navigate to Profile Page
  Wait Until Page Contains Element  projectscard

Scenario: As a visitor I can't edit other user's projects
  Go To  ${SERVER}
  Wait until page contains element  search
  Click element  search
  Wait Until Page Contains Element  searchresults
  Sleep  2s
  Click Link  Janet
  Wait Until Page Contains Element  projectscard
  Page Should Not Contain Button  editProjectsButton

Scenario: As a visitor I can see correct projects in project info on profile page
  Refresh & Navigate to Profile Page
  Wait Until Page Contains Element  projectscard
  Table Cell Should Contain  locator=projectTable  row=1  column=1  expected=Project
  Table Cell Should Contain  locator=projectTable  row=2  column=1  expected=JawCorp
  Table Cell Should Contain  locator=projectTable  row=3  column=1  expected=KeutzCorp

Scenario: As a visitor I can see correct allocation-% in project info on profile page
  Refresh & Navigate to Profile Page
  Wait Until Page Contains Element  projectscard
  Table Cell Should Contain  locator=projectTable  row=1  column=2  expected=Allocation-%
  Table Cell Should Contain  locator=projectTable  row=2  column=2  expected=50%
  Table Cell Should Contain  locator=projectTable  row=3  column=2  expected=50%

Scenario: As a visitor I can see correct participation period in project info on profile page
  Refresh & Navigate to Profile Page
  Wait Until Page Contains Element  projectscard
  Table Cell Should Contain  locator=projectTable  row=1  column=3  expected=Participation from | until
  Table Cell Should Contain  locator=projectTable  row=2  column=3  expected=2023-03-31 | 2024-12-31
  Table Cell Should Contain  locator=projectTable  row=3  column=3  expected=2023-08-01 | 2025-12-31