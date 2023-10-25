from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_STX(self):
        assert checkout_solution.checkout('STX') == 45
    
    def test_checkout_STXZZ(self):
        assert checkout_solution.checkout('STXZZ') == 82

    def test_checkout_AAAB(self):
        assert checkout_solution.checkout('AAAB') == 160

    def test_checkout_CDBA(self):
        assert checkout_solution.checkout('CDBA') == 115
    
    def test_checkout_AA(self):
        assert checkout_solution.checkout('AA') == 100
    
    def test_checkout_AAA(self):
        assert checkout_solution.checkout('AAA') == 130
    
    def test_checkout_ABCD(self):
        assert checkout_solution.checkout('ABCD') == 115
    
    def test_checkout_a(self):
        assert checkout_solution.checkout('a') == -1
    
    def test_checkout_E(self):
        assert checkout_solution.checkout('E') == 40
    
    def test_checkout_EE(self):
        assert checkout_solution.checkout('EE') == 80
    
    def test_checkout_EEE(self):
        assert checkout_solution.checkout('EEE') == 120
    
    def test_checkout_EEEE(self):
        assert checkout_solution.checkout('EEEE') == 160

    def test_checkout_AAAEE(self):
        assert checkout_solution.checkout('AAAEE') == 210
    
    def test_checkout_AAAAAEE(self):
        assert checkout_solution.checkout('AAAAAEE') == 280
    
    def test_checkout_AAAAAAEE(self):
        assert checkout_solution.checkout('AAAAAAEE') == 330
    
    def test_checkout_AAAAAAAAAAAAAAA(self):
        assert checkout_solution.checkout('AAAAAAAAAAAAAAA') == 600
    
    def test_checkout_EEB(self):
        assert checkout_solution.checkout('EEB') == 80
    
    def test_checkout_EEEB(self):
        assert checkout_solution.checkout('EEEB') == 120
    
    def test_checkout_EEEEBB(self):
        assert checkout_solution.checkout('EEEEBB') == 160
    
    def test_checkout_FF(self):
        assert checkout_solution.checkout('FF') == 20
    
    def test_checkout_FFF(self):
        assert checkout_solution.checkout('FFF') == 20
    
    def test_checkout_FFFFFF(self):
        assert checkout_solution.checkout('FFFFFF') == 40
    
    def test_checkout_HHHHH(self):
        assert checkout_solution.checkout('HHHHH') == 45
    
    def test_checkout_HHHHHHHHHH(self):
        assert checkout_solution.checkout('HHHHHHHHHH') == 80
    
    def test_checkout_KK(self):
        assert checkout_solution.checkout('KK') == 150
    
    def test_checkout_NNNM(self):
        assert checkout_solution.checkout('NNNM') == 120
    
    def test_checkout_PPPPP(self):
        assert checkout_solution.checkout('PPPPP') == 200
    
    def test_checkout_QQQ(self):
        assert checkout_solution.checkout('QQQ') == 80
    
    def test_checkout_RRRQ(self):
        assert checkout_solution.checkout('RRRQ') == 150
    
    def test_checkout_UUUU(self):
        assert checkout_solution.checkout('UUUU') == 120
    
    def test_checkout_VV(self):
        assert checkout_solution.checkout('VV') == 90
    
    def test_checkout_VVV(self):
        assert checkout_solution.checkout('VVV') == 130
    
    def test_checkout_VVVVVV(self):
        assert checkout_solution.checkout('VVVVVV') == 260


