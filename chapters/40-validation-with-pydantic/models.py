# /// script
# dependencies = ["pydantic"]
# ///
import datetime as dt
from pydantic import BaseModel, Field, ValidationError, field_validator


class Transaction(BaseModel):
    date: dt.date
    description: str = Field(min_length=1)
    amount: float
    category: str = "other"

    @field_validator("amount")
    @classmethod
    def check_amount(cls, value):
        if value == 0:
            raise ValueError("amount must not be zero")
        return value

    @field_validator("category")
    @classmethod
    def known_category(cls, value):
        if value not in {"food", "housing", "health", "income", "other"}:
            raise ValueError(f"unknown category: {value}")
        return value



