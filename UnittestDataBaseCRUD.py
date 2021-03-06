import unittest
import DataBaseCRUD

class TestDataBaseCRUD(unittest.TestCase):
    def TestInsert(self):
        self.assertAlmostEqual(DataBaseCRUD.insertInDatabase(6,6000,"October"),True)
        self.assertAlmostEqual(DataBaseCRUD.insertInDatabase(1,100,"Jun"),False)
        self.assertRaises(Exception,DataBaseCRUD.insertInDatabase("dsda","sadad","sda"))
    def TestDelete(self):
        self.assertAlmostEqual(DataBaseCRUD.deleteFromDatabase(1),True)
        self.assertAlmostEqual(DataBaseCRUD.deleteFromDatabase(434),False)
        self.assertRaises(Exception, DataBaseCRUD.deleteFromDatabase("dsda"))
    def TestUpdates(self):
        self.assertAlmostEqual(DataBaseCRUD.updateInDatabase(1,0,"February"),True)
        self.assertAlmostEqual(DataBaseCRUD.updateInDatabase(89,2000,"January"),False)
        self.assertAlmostEqual(DataBaseCRUD.updateInDatabase(1,5000,"December"),False)
        self.assertRaises(Exception, DataBaseCRUD.updateInDatabase("prvi", "drugi", "treci"))
    def TestConsumptionForBrojilo(self):
        self.assertRaises(Exception,DataBaseCRUD.consumptionForBrojilo("rec"))
    def TestInsertInBrojilo(self):
        self.assertRaises(Exception,DataBaseCRUD.insertInBrojilo("sadas",213,123,312,231,312))
        self.assertRaises(DataBaseCRUD.insertInBrojilo(1,"","","",1000,""),False)
        self.assertRaises(DataBaseCRUD.insertInBrojilo(99,"","","",8000,""),True)
    def TestDeleteInBrojilo(self):
        self.assertRaises(Exception,DataBaseCRUD.deleteInBrojilo("dasd"))
        self.assertAlmostEqual(DataBaseCRUD.deleteInBrojilo(1),True)
        self.assertAlmostEqual(DataBaseCRUD.deleteInBrojilo(99931),False)

if __name__ == "__main__":
    unittest.main()