from enum import StrEnum


class Category(StrEnum):
    FOOD = "food"
    HOUSING = "housing"
    HEALTH = "health"
    OTHER = "other"

    def label(self):
        return self.value.title()

def budget(category):
    if category is Category.FOOD:
        return 400
    elif category is Category.HOUSING:
        return 1500
    else:
        return 100


print(budget(Category.FOOD))
print(budget(Category.HOUSING))
print(Category.FOOD.label())
print(f"{Category.FOOD}")
