# Created by tymos at 12/21/2023
Feature: Enter information on registration page

  Scenario: The user can enter the information into the input fields on the registration page
    Given Open the registration page
    Then Enter some test information in the input fields
    And Verify the right information is present
