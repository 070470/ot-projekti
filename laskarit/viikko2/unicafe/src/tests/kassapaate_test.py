import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class testKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_rahan_ja_myytyjen_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(((self.kassapaate.maukkaat)+ (self.kassapaate.edulliset)), 0)

    def test_riittava_kateismaksu_maukkaasta_nostaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_riittava_kateismaksu_edullisesta_nostaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_riittava_kateismaksu_antaa_oikean_vaihtorahan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_riittava_kateismaksu_nostaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_riittamaton_kateismaksu_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_riittamaton_kateismaksu_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_riittamaton_kateismaksu_myytyjen_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(((self.kassapaate.maukkaat) + (self.kassapaate.edulliset)), 0)

    # Sitten korttimaksut

    def test_riittava_korttimaksu_maukkaasta_laskee_kortin_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

    def test_riittava_korttimaksu_edullisesta_laskee_kortin_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")

    def test_riittava_korttimaksu_nostaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)
                
    def test_korttimaksu_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_riittamaton_korttimaksu_ei_onnistu(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual((self.kassapaate.edulliset) + (self.kassapaate.maukkaat), 0)

    def test_kortille_lataaminen_onnistuu(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 200)
        self.kassapaate.lataa_rahaa_kortille(kortti, -200)
        self.assertEqual(str(kortti), "Kortilla on rahaa 12.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    
