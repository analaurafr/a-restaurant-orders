from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


def test_ingredient():
    ingredient_1 = Ingredient("frango")
    ingredient_2 = Ingredient("ovo")
    ingredient_3 = Ingredient("frango")
    assert ingredient_1 == ingredient_3
    assert ingredient_1 != ingredient_2
    assert hash(ingredient_1) != hash(ingredient_2)
    assert hash(ingredient_1) == hash(ingredient_3)
    assert ingredient_1.name == "frango"
    assert repr(ingredient_1) == "Ingredient('frango')"
    assert ingredient_1.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
