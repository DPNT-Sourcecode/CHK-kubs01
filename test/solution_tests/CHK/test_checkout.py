from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_AAAB(self):
        assert checkout_solution.checkout('AAAB') == 205

    def test_checkout_CDBA(self):
        assert checkout_solution.checkout('CDBA') == 135
    
    def test_checkout_AA(self):
        assert checkout_solution.checkout('AA') == 100
    
    def test_checkout_AAA(self):
        assert checkout_solution.checkout('CDBA') == 130
    
    def test_checkout_ABCD(self):
        assert checkout_solution.checkout('CDBA') == 115
