# Lettuce Python

[Lettuce] [1] is a BDD python tool inspired by [Cucumber] [4].

# Setup
[Install] [3] lettuce:

`sudo pip install lettuce`

Then install lettuce webdriver to use selenium.

`sudo pip install lettuce_webdriver`

Nose is required for the testingbot example
`sudo pip install nose`




# Run
## Lettuce example
There is a simple example doing BDD on a function that calculates the factorial of a number
To run go to directory `examples/03-lettuce-python/factorial-example` then type

`lettuce`
You should see something like this

```
1 feature (1 passed)
5 scenarios (5 passed)
15 steps (15 passed)
```

## Selenium Example 
To run go to directory `examples/03-lettuce-python/wikipedia` then type
`lettuce`

You should see something like this

```
1 feature (1 passed)
1 scenario (1 passed)
6 steps (6 passed)
```

I used this code to get to the page
```cucumber
  Given I go to "http://google.co.uk"
  When I fill in "q" with "aston martin"
  and I press "btnG"
```

instead of this
```cucumber
  Given I go to "http://en.wikipedia.org"
  When I fill in "searchInput" with "aston martin"
  and I press "searchButton"
```
I was getting this exception `assert_false(step, text_field is False,'Can not find a field named "%s"' % field_name)`
and this is why google was used for the search.



[1]: http://lettuce.it/ "Official Site"
[2]: https://github.com/gabrielfalcao/lettuce "Github"
[3]: http://lettuce.it/intro/install.html "installation Instructions"
[4]: http://cukes.info/ "Cucumber Official Site"
[5]: http://lettuce.it/tutorial/simple.html#tutorial-simple "Simple Example"