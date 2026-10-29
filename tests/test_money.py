import pytest
from money import CurrencyMismatchError, Money

"""
These tests only proves that only the tested methods works right with this inputs.
But it doesn't prove anything about the other inputs for the methods or other components of the project
"""

def test_str_with_positive():
    assert str(Money(1250, 'TRY'))=='12.50 TRY'

def test_str_with_negative_init_check():
    with pytest.raises(ValueError):
        str(Money(-1250, "TRY"))

def test_allocate_with_sums():
    assert (Money(1000,'TRY')+Money(1000,'TRY')).allocate(3)==[Money(667, 'TRY'), Money(667, 'TRY'), Money(666, 'TRY')]

def test_allocate_zero_amount():
    assert Money(0, 'TRY').allocate(3)==[Money(0, 'TRY'), Money(0, 'TRY'), Money(0, 'TRY')]

def test_allocate_zero_parts_raises_value_error():
    with pytest.raises(ValueError):
        Money(1000, 'TRY').allocate(0)

def test_allocate_with_negative_amount():
    with pytest.raises(ValueError):
        Money(-1000, 'TRY').allocate(3)

def test_allocate_by():
    assert Money(1000, 'TRY').allocate_by([3,1])==[Money(750, 'TRY'), Money(250, 'TRY')]

def test_allocate_by_with_zero():
    with pytest.raises(ValueError):
        Money(1000, 'TRY').allocate_by([1,0])

def test_list_with_same_currency():
    assert sorted([Money(1250,"TRY"),Money(1205,"TRY")])==[Money(1205, 'TRY'), Money(1250, 'TRY')]

def test_list_with_diff_currency():
    with pytest.raises(CurrencyMismatchError):
        sorted([Money(1250,"TRY"),Money(1205,"EUR")])

def test_eq_with_same_curr():
    assert Money(1000,'TRY')==Money(1000,'TRY')

def test_eq_with_differentc_curr():
    assert not Money(1000,'TRY')==Money(1000,'EUR')

def test_eq_with_diff_amount():
    assert not Money(1000,'TRY')==Money(2000,'TRY')

def test_dict_key():
    my_dict={Money(1000,'TRY'):"fee"}
    m=Money(1000,'TRY')
    assert my_dict[m]=="fee"

def test_set():
    s=set([Money(1000,'TRY'), Money(1000,'TRY')])
    assert s=={Money(1000, 'TRY')}

def test_hash():
    assert hash(Money(1000,'TRY'))==hash(Money(1000,'TRY'))

def test_add_with_int():
    with pytest.raises(TypeError):
        Money(1250,'TRY')+(100)

def test_add_with_object():
    with pytest.raises(CurrencyMismatchError):
        Money(1250,'TRY')+(Money(1000,'EUR'))

def test_sub_with_object():
    assert str(Money(1250,'TRY')-(Money(1000,'TRY')))=='2.50 TRY'

def test_sub_with_int():
    with pytest.raises(TypeError):
        Money(1250, 'TRY')-(100)

def test_subtraction_below_zero_raises():
    with pytest.raises(ValueError):
        assert Money(1000, 'TRY')-Money(1250, 'TRY')

def test_mul_with_int():
    assert str(Money(1250,'TRY')*(10))=='125.00 TRY'

def test_mul_with_object():
    with pytest.raises(TypeError):
        Money(1250,'TRY')*(Money(1000,'TRY'))