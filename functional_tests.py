from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.geckodriver_path = 'C:/Users/emilb/Documents/geckodriver.exe'
        self.browser = webdriver.Firefox(executable_path=self.geckodriver_path)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Eddy and Ed bothered Edddy about an online to-do website so much he went to check it
        # so they would shut up
        self.browser.get('http://localhost:8000')

        # He noticed page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('You haven\'t finished writing this test!')

        # He is invited to enter a to-do item straight away

        # He types "Buy peacock feathers" ( he likes tying fly-fishing lures when he is stoned )

        # When he hits Enter, the page updates, and now page lists
        #  '1: Buy peacock feathers' as a to-do item in the list

        # There is still a text box inviting him to enter another to-do item.
        # He types 'Use peacock feathers to make a fly' ( he is unexpectedly methodical)

        # The page updates again and now he can see both to-do items in the list

        # Ed wonders wether the site will remember his list. Then he sees that the site 
        # has generated a unique URL for him -- there is some explanatory text to that effect

        # He visits the URL - his to-do list is alive and well staring at his face

unittest.main()