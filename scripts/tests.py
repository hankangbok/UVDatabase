import os
import unittest
    
class checkForRequiredFolders(unittest.TestCase):
    def test_Custom_Modules(self):
        customModulesExists = os.path.isdir(os.path.join('../../','Custom Modules'))
        print customModulesExists
        self.assertTrue(customModulesExists)
    def test_custommodules(self):
        customModulesExists = os.path.isdir(os.path.join('../../','custom modules'))
        print customModulesExists
        self.assertTrue(customModulesExists)
  
    def test_profiles(self):
        
        profilesExists = os.path.isdir(os.path.join('../../','profiles'))
        print profilesExists
        self.assertTrue(profilesExists)
    def test_for_Profiles(self):
        
        ProfilesExists = os.path.isdir(os.path.join('../../','Profiles'))
        print ProfilesExists
        self.assertTrue(ProfilesExists)

#if __name__ == '__main__':
 #       unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(checkForRequiredFolders)
unittest.TextTestRunner(verbosity=2).run(suite)
#Note, paths don't have to be case sensitive for 'isdir' apparently 
