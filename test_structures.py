import pytest


class TestList:
    # IndexError
    def test_index_error(self):
        array = [1, 2]
        with pytest.raises(IndexError):
            assert array[3] == 0

    # type conversion
    @pytest.mark.parametrize("value, expected", [([], False), ([1], True)])
    def test_list_type(self, value, expected):
        assert bool(value) == expected


class TestDict:

    # KeyError
    def test_key_error(self):
        dictionary = {"key": "value"}
        with pytest.raises(KeyError):
            assert dictionary["key1"] == "value"

    # update dict
    @pytest.mark.parametrize("dict1, dict2, expected",
                             [({'k': 'v'}, {'b': 'c'}, {'k': 'v', 'b': 'c'}),
                              ({"k": "v"}, {'k': 'v2'}, {'k': 'v2'})])
    def test_dict_type(self, dict1, dict2, expected):
        dict1.update(dict2)
        assert dict1 == expected


class TestFloat:

    # division
    def test_div(self):
        assert float(3.14) / 2 == 1.57
        assert float(3.14) // 2 == 1.0

    # TypeError
    @pytest.mark.parametrize("value", ["string", [], {}, set([1, 2]), ()])
    def test_type_error(self, value):
        with pytest.raises(TypeError):
            assert float(3.14) + value
