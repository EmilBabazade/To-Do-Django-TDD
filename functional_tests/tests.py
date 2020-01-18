from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.geckodriver_path = 'C:/Users/emilb/Documents/geckodriver.exe'
        self.browser = webdriver.Firefox(executable_path=self.geckodriver_path)
        
    def tearDown(self):
        self.browser.quit()
        # delete everything in db (just for now)
        # Item.objects.all().delete()

    def check_for_text_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Eddy and Ed bothered Edddy about an online to-do website so much he went to check it
        # so they would shut up
        self.browser.get(self.live_server_url)

        # He noticed page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Buy peacock feathers" ( he likes tying fly-fishing lures when he is stoned )
        input_box.send_keys('Buy peacock feathers.')

        # When he hits Enter, the page updates, and now page lists
        #  '1: Buy peacock feathers' as a to-do item in the list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1) # wait for page to update
        self.check_for_text_in_list_table('1: Buy peacock feathers.')
        # There is still a text box inviting him to enter another to-do item.
        # He types 'Use peacock feathers to make a fly.' ( he is unexpectedly methodical)
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly.')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again and now he can see both to-do items in the list
        self.check_for_text_in_list_table('1: Buy peacock feathers.')
        self.check_for_text_in_list_table('2: Use peacock feathers to make a fly.')
        # Ed wonders wether the site will remember his list. Then he sees that the site 
        # has generated a unique URL for him -- there is some explanatory text to that effect
        self.fail('Finish the test!')

        # He visits the URL - his to-do list is alive and well staring at his face

