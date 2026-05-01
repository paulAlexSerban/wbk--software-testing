Feature: Demo Feature

  # Unit-testing analogy
  # 1. Given - setup
  # 2. When - action
  # 3. Then - assertion
  # 4. And - additional assertions
  # 5. But - negative assertions

  @Demo
  Scenario: Run first demo feature
    Given DuckDuckGo page is opened
    When I search with <SearchItem>
    Then I click on the first search result
    Then The URL should match <ExpectedURL>

    Examples:
      | TestID     | SearchItem    | ExpectedURL           |
      | DEMO_TC001 | paulserban.eu | https://paulserban.eu |

  @TextInputInteractions
  Scenario: Text input interactions
    Given Text inputs page is open
    When Perform text input interactions
    Then The text inputs should be filled

    Examples:
      | TestID    |
      | WEB_TC002 | 

  @DropdownInteractions
  Scenario: Dropdown interactions
    Given Dropdown page is open
    When Check the default dropdown value
    When Perform dropdown interaction - select option 1
    Then The new dropdown value should be 1
    When Perform dropdown interaction - select option 2
    Then The new dropdown value should be 2
    When Perform dropdown interaction - select option 1 of 2
    Then The new dropdown value should be 1 again

    Examples:
      | TestID    |
      | WEB_TC003 |

  @CheckboxInteractions
  Scenario: Checkbox interactions
    Given Checkbox page is open
    When Check selected checkbox value
    When Perform checkbox interaction - select unselected checkbox
    Then The first checkbox value should be true

    Examples:
      | TestID    |
      | WEB_TC004 | 

  @WindowInteractions
  Scenario: Window interactions
    Given Web page is open
    When Check webpage is completely loaded by listening for DOM content to be loaded
    When Open another window
    Then Browser should have two windows
    When Switch back to old window
    Then Check the title of the window to be The Internet
    When Switch to window based on title
    Then Check the title of the window to be Home | Elemental Selenium
    When Switch back to the main window

    Examples:
      | TestID    |
      | WEB_TC005 | 

  @ScrollNScreenshot
  Scenario: Scroll and Screenshot
    Given eCommerce web page is open
    When Scroll to the bottom of the page
    Then Take a screenshot of the page

    Examples:
      | TestID    |
      | WEB_TC006 | 