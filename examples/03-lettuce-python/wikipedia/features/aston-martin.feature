Feature: Wikipedia Aston Martin

Scenario: Visit Wikipedia
  Given I go to "http://google.co.uk"
  When I fill in "q" with "aston martin"
  and I press "btnG"
  Then I should see "Wikipedia" within 2 seconds
  When I click "Aston Martin - Wikipedia, the free encyclopedia"
  Then I should see "Kensington" within 2 seconds


