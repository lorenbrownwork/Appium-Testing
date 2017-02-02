import os
from time import sleep
import unittest
from appium import webdriver

STARTUP_SLEEP = 4
XML_SLEEP = 1

#path to UI Automator Viewer
#C:\Users\loren.brown\AppData\Local\Android\sdk\tools\uiautomatorviewer.bat

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SegmentPreviewTests(unittest.TestCase):
    #runs before every test
    def setUp(self):
        desired_caps = {}
        desired_caps['noReset'] = True
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            'C:/Users/loren.brown/Documents/Zonar/Rider-Verification/app/build/outputs/apk/app-emulator-debug.apk'
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # runs after every test
    def tearDown(self):
        # end the session
        self.driver.quit()

    # Asserts the supplied text field is on screen
    def assert_text_on_screen(self, text):
        el = self.driver.find_element_by_android_uiautomator('text("' + text + '")')
        self.assertIsNotNone(el)

    # Navigates to the Segment Preview Screen
    def segment_preview_navigate_to(self):
        # Find the 'AM Segment 1' card
        el = self.driver.find_element_by_name('AM Segment 1')
        self.assertIsNotNone(el)
        el.click()

        # Wait for XML to load
        sleep(XML_SLEEP)

        # Check our location (Segment Preview)
        self.assert_text_on_screen('Segment Preview - AM Segment 1')

    def test_segment_preview_navigate_to(self):
        # Wait for app to launch
        sleep(STARTUP_SLEEP)

        # Navigate to the Segment Preview Screen
        self.segment_preview_navigate_to()

    def test_segment_preview_start_segment_button(self):
        # Wait for app to launch
        sleep(STARTUP_SLEEP)

        # Navigate to the Segment Preview Screen
        self.segment_preview_navigate_to()

        # Find and click the 'Start Segment' button
        el = self.driver.find_element_by_android_uiautomator('text("Start Segment")')
        self.assertIsNotNone(el)
        el.click()

        # Wait for XML to load
        sleep(XML_SLEEP)

        # Check our location (Segment Preview)
        self.assert_text_on_screen('Segment - AM Segment 1')

    def test_segment_preview_back_button(self):
        # Wait for app to launch
        sleep(STARTUP_SLEEP)

        # Navigate to the Segment Preview Screen
        self.segment_preview_navigate_to()

        # Find and click the 'Back' button on the toolbar
        el = self.driver.find_element_by_name('Navigate up')
        self.assertIsNotNone(el)
        el.click()

        # Wait for XML to load
        sleep(XML_SLEEP)

        # Check our location (Segment List)
        self.assert_text_on_screen('My Segments - Bus 0')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SegmentPreviewTests)
    unittest.TextTestRunner(verbosity=2).run(suite)