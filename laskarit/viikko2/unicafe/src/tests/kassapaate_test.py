import unittest
from kassapaate import Kassapaate

class testKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahan_ja_myytyjen_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(((self.kassapaate.maukkaat)+ (self.kassapaate.edulliset)), 0)

    def test_riittava_maksu_nostaa_kassan_rahamaaraa(self):
        kassa = Kassapaate(100000)
        kassa.syo_maukkaasti_kateisella(kassa, 500)
        self.assertEqual(kassa.kassassa_rahaa, 100400)
        kassa.syo_edullisesti_kateisella(kassa, 500)
        self.assertEqual(kassa.kassassa_rahaa, 100250)

    def test_riittava_maksu_nostaa_myytyjen_lounaiden_maaraa(self):
        kassa = Kassapaate(100000)
        self.assertEqual(kassa.syo_maukkaasti_kateisella(kassa, 500), 100)
        self.assertEqual(kassa.syo_edullisesti_kateisella(kassa, 500), 250)

    
