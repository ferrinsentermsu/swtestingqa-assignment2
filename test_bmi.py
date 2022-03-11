from bmi import calc_bmi
import pytest

# Testing using weak n x 1 boundary testing

# Testing values for underweight
test_info_kn = calc_bmi(64,135)
test_info_under = calc_bmi(50,89)
test_info_over = calc_bmi(50,89.5)

@pytest.mark.parametrize("input,expected",[(test_info_kn['Category'],"normal"),(test_info_under['Category'],"underweight"),(test_info_over['Category'],"normal")])
def test_underweight_bmi(input,expected):
    #Known passing case 
    assert  input == expected



# Testing Values for Normal
test_info_kn = calc_bmi(64,135)
test_info_under = calc_bmi(66,164.5)
test_info_over = calc_bmi(66,165.0)

@pytest.mark.parametrize("input,expected",[(test_info_kn['Category'],"normal"),(test_info_under['Category'],"normal"),(test_info_over['Category'],"overweight")])
def test_normal_weight_bmi(input,expected):
    #Known passing case 
    assert  input == expected



# Testing Values for Overweight
test_info_kn = calc_bmi(64,135)
test_info_under = calc_bmi(65,198.0)
test_info_over = calc_bmi(65,198.5)

@pytest.mark.parametrize("input,expected",[(test_info_kn['Category'],"normal"),(test_info_under['Category'],"overweight"),(test_info_over['Category'],"obese")])
def test_overweight_bmi(input,expected):
    #Known passing case 
    assert  input == expected