import unittest
from kassapaate import Kassapaate

class testKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahan_ja_myytyjen_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 10000)
        self.assertEqual(((self.kassapaate.maukkaat)+ (self.kassapaate.edulliset)), 0)

    
