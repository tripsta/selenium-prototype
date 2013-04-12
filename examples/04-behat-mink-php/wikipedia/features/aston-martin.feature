Feature: Wikipedia Aston Martin
In order to check navigation in Wikipedia
As an end User
I would like to search and navigate by clicking links

@javascript
Scenario: Visit Wikipedia
  Given I am on "http://google.co.uk"
  When I fill in "q" with "aston martin wikipedia"
  And I press "btnG"
  Then I wait for the page title to include "aston martin"
  When I follow "Aston Martin - Wikipedia, the free encyclopedia"
  Then I wait for the page title to include "Aston Martin"
  When I follow "Kensington"
  Then I wait for the page title to include "Kensington"


