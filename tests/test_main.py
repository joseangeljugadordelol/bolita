import pytest

from main import calcular_area_triangulo


def test_area_trianguo():
    actual_result = calcular_area_triangulo(13, 3)

    assert actual_result == pytest.approx(19.39, abs=0.01)