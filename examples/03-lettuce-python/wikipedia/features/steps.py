from lettuce import *
from selenium import webdriver
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager
from lettuce_webdriver.webdriver import *

@before.all
def setup_browser():
    world.browser = webdriver.Firefox()

@after.all
def close_browser(result):
	world.browser.close();
