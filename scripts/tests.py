import os
import unittest


#print os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))+'/custom modules'
#print 'Is /custom modules a valid folder visible to this program?'
#print (os.path.isdir(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))+'/custom modules'))


#print os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))+'/Custom Modules'
#print 'Is /Custom Modules a valid folder visible to this program?'
#print (os.path.isdir(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))+'/Custom Modules'))


#print os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))+'/profiles'
#print 'Is /profiles a valid folder visible to this program?'
#print (os.path.isdir(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))+'/profiles'))



    
class checkForRequiredFolders(unittest.TestCase):
    def test_Custom_Modules(self):
        customModulesExists = os.path.isdir(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))+'/Custom Modules')
        print customModulesExists
        self.assertTrue(customModulesExists)
    def test_custommodules(self):
        customModulesExists = os.path.isdir(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))+'/custom modules')
        print customModulesExists
        self.assertTrue(customModulesExists)
  
    def test_profiles(self):
        profilesExists = os.path.isdir(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))+'/profiles')
        print profilesExists
        self.assertTrue(profilesExists)
    def test_for_Profiles(self):
        ProfilesExists = os.path.isdir(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))+'/Profiles')
        print ProfilesExists
        self.assertTrue(ProfilesExists)

if __name__ == '__main__':
        unittest.main()
