<?php

/**
 * Features context.
 */
class FeatureContext extends Behat\MinkExtension\Context\MinkContext
{

    /**
     * @Then /^I wait for the page title to include "([^"]*)"$/
     */
    public function iWaitForTheKensingtonLinkToAppear($argument)
    {
        $this->getSession()->wait(5000, "document.title.indexOf('$argument')>-1");
    }
}
