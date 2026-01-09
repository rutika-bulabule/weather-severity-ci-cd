# test_weather_severity.py

from weather_severity import analyze_severity

def test_extreme():
    avg, level = analyze_severity([95, 92, 94])
    assert level == "Extreme"

def test_mild():
    avg, level = analyze_severity([55, 58, 52])
    assert level == "Mild"

def test_normal():
    avg, level = analyze_severity([30, 35, 38])
    assert level == "Normal"