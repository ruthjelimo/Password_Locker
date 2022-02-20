import pyperclip
import unittest
from credential import Credential
class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test
        '''
        self.new_credential=Credential("Instagram","mimoh","1234")
    def test_init(self):
        self.assertEqual(self.new_credential.account_name, "Instagram")
        self.assertEqual(self.new_credential.username,"mimoh")
        self.assertEqual(self.new_credential.account_password, "1234")

    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual( len(Credential.credential_list), 1)

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        Credential.credential_list=[]

    def test_save_multiple_credentials(self):
        self.new_credential.save_credential()
        test_credential=Credential("Twitter","ruth","cheli")
        test_credential.save_credential()
        self.assertEqual( len(Credential.credential_list), 2)


    def test_confirm_credential_exists(self):
        '''
        confirm that credentials  exists
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "ruth","cheli")
        test_credential.save_credential()
        credential_exists = Credential.credential_exists("Twitter")
        self.assertTrue(credential_exists)


    def test_display_credentials(self):
        '''
        test if  credentials can be displayed
        '''
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)
if __name__ == '__main__':
    unittest.main()