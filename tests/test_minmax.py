import pytest


from data_prepare.minmax import calculate


@pytest.mark.parametrize('scope', ['months', 'years'])
def test_pass_not_callable_to_calc(scope):
    with pytest.raises(ValueError) as exc_info:
        calculate('not_callable', 'some/path', scope=scope)
    print(exc_info)
