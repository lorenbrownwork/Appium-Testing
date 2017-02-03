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

class DrawerTests(unittest.TestCase):
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

    def swipe_right(self):
        self.driver.swipe(start_x=5, start_y=300, end_x=500, end_y=300, duration=800)

    def swipe_left(self):
        self.driver.swipe(start_x=500, start_y=300, end_x=5, end_y=300, duration=800)

    def test_drawer_hamburger_button_from_segment_view(self):
        # Wait for app to launch
        sleep(STARTUP_SLEEP)

        # Find and click the 'Hamburger' button on the toolbar
        el = self.driver.find_element_by_name('RiderVerification')
        self.assertIsNotNone(el)
        el.click()

        # Wait for XML to load
        sleep(XML_SLEEP)

        # Check our location (Open Drawer)
        self.assert_text_on_screen('My Segments')

        # Check our location (Open Drawer)
        self.assert_text_on_screen('Segment Details')

        # Check our location (Open Drawer)
        self.assert_text_on_screen('Alerts')

        # Check our location (Open Drawer)
        self.assert_text_on_screen('Riders')

        # Check our location (Open Drawer)
        self.assert_text_on_screen('Logout')

        # Find and click the 'Back' button on the toolbar
        el = self.driver.find_element_by_name('RiderVerification')
        self.assertIsNotNone(el)
        el.click()

        # Wait for XML to load
        sleep(XML_SLEEP)

        # Check our location (Segment View)
        self.assert_text_on_screen('My Segments - Bus 0')

    def test_drawer_swipe_from_segment_view(self):
        # Wait for app to launch
        sleep(STARTUP_SLEEP)

        # Open Drawer (Swipe)
        self.swipe_right()

        # Wait for XML to load
        sleep(XML_SLEEP)

        # Check our location (Open Drawer)
        self.assert_text_on_screen('My Segments')

        # Check our location (Open Drawer)
        self.assert_text_on_screen('Segment Details')

        # Check our location (Open Drawer)
        self.assert_text_on_screen('Alerts')

        # Check our location (Open Drawer)
        self.assert_text_on_screen('Riders')

        # Check our location (Open Drawer)
        self.assert_text_on_screen('Logout')

        # Close Drawer (Swipe)
        self.swipe_left()

        # Wait for XML to load
        sleep(XML_SLEEP)

        # Check our location (Segment View)
        self.assert_text_on_screen('My Segments - Bus 0')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DrawerTests)
    unittest.TextTestRunner(verbosity=2).run(suite)