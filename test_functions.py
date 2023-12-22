from functions import salary,hello_who

'''def test_hello_who_max():
    assert hello_who('Max') == 'Hello,Max'
    assert hello_who('CHO') == 'Hello,CHO'
    assert hello_who('Kolobok') == 'Hello,Kolobok'
    assert hello_who('123') == 'Hello,123'''''

def test_salary():
    assert salary(2,2) != 8
    assert salary(3,1) != 6