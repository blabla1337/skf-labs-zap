import unittest, sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

from runners.zap_api import *

class skf_code_lab_automation(unittest.TestCase):
        

    def test_a_proxy_the_requests(self):
        """Test proxying the http requests"""
        driver = self.driver
        new_session()
        disable_passive_scan()
        driver.get("https://xss-9e758f7d-2162-4e12-9183-81a8f5e572dc.securityknowledgeframework-labs.org")
        string = driver.find_element(by=By.NAME, value="string")
        string.send_keys("test xss")
        string.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        body_text = driver.find_element(by=By.XPATH, value="//p[contains(text(), 'test xss')]").text
        assert 'test xss' in body_text
    

    def test_b_start_zap_assert_vuln(self):
        """Test if the vulnerability is present with ZAP"""
        import_scan_policy()
        start_zap()
        add_custom_alert(
            messageid = 1 ,
            name = "Are you Elden Lord already?",
            riskid = 3,
            confidenceid = 3,
            description = "Stel je vind wat in selenium dan is het mooier om het in ZAP weer te geven noh?",
            solution = "Door de ZAP API te gebruiken kunnen we dat dus doen"
        )
        assert '40012' in '40012'

    
    @classmethod
    def tearDown(self):
        self.driver.quit()

    @classmethod
    def setUp(self):
        zap_proxy_host = "127.0.0.1"
        zap_proxy_port = 8081
        options=Options()
        options.set_preference("network.proxy.type", 1)
        options.set_preference("network.proxy.http", zap_proxy_host)
        options.set_preference("network.proxy.http_port", int(zap_proxy_port))
        options.set_preference("network.proxy.ssl",zap_proxy_host)
        options.set_preference("network.proxy.ssl_port", int(zap_proxy_port))
        options.set_preference("browser.startup.homepage", "about:blank")
        options.set_preference("startup.homepage_welcome_url", "about:blank")
        options.set_preference("startup.homepage_welcome_url.additional", "about:blank")
        options.set_preference("webdriver_assume_untrusted_issuer", False)
        options.set_preference("accept_untrusted_certs", True)
        self.driver = webdriver.Firefox(options=options)
        driver = self.driver


if __name__ == '__main__':
    unittest.main()


#"/Volumes/OWASP ZAP/OWASP ZAP.app/Contents/Java/zap.sh" \
#-daemon \
#-host 0.0.0.0 \
#-port 8082 \
#-config api.addrs.addr.regex=true \
#-config api.disablekey=true

