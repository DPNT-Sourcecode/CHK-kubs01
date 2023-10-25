from lib.solutions.CHK import checkout_solution


class TestCheckout():
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
    
    def test_checkout_XYZ(self):
        assert checkout_solution.checkout('XYZ') == -1
    
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





