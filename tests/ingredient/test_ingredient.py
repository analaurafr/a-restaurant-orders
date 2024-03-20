from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    pass


def test_ingredient_init():
    ingredient = Ingredient("bacon")
    assert ingredient.name == "bacon"


def test_ingredient_restrictions():
    ingredient = Ingredient("bacon")
    assert ingredient.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }


def test_ingredient_repr():
    ingredient = Ingredient("bacon")
    assert repr(ingredient) == "Ingredient('bacon')"


def test_ingredient_eq_same_object():
    ingredient1 = Ingredient("bacon")
    ingredient2 = ingredient1
    assert ingredient1 == ingredient2


def test_ingredient_eq_different_objects_same_name():
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("bacon")
    assert ingredient1 == ingredient2


def test_ingredient_eq_different_objects_different_names():
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("salmão")
    assert not ingredient1 == ingredient2


def test_ingredient_hash():
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("bacon")
    assert hash(ingredient1) == hash(ingredient2)


def test_ingredient_name():
    ingredient = Ingredient("bacon")
    assert ingredient.name == "bacon"


def test_ingredient_restrictions_correct_values():
    ingredient = Ingredient("bacon")
    assert ingredient.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }


def test_ingredient_failure_different_hash_same_ingredient():
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("bacon")
    assert hash(ingredient1) != hash(ingredient2)


def test_ingredient_failure_same_hash_different_ingredients():
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("salmão")
    assert hash(ingredient1) != hash(ingredient2)
