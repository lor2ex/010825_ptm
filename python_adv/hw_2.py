from pydantic import (
    Field,
    field_validator,
    model_validator,
    BaseModel,
    EmailStr,
    ValidationError,
)


class Address(BaseModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    house_number: int = Field(gt=0)


class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    is_employed: bool
    address: Address


    class Config:
        str_strip_whitespace = True

    @field_validator('name')
    @classmethod
    def validate_name(cls, value: str) -> str:
        # value = value.strip()
        if not value.isalpha():
            raise ValueError("Name must contain only letters")
        return value

    @model_validator(mode='after')
    def validate_age_and_employment(self) -> 'User':
        if self.is_employed and not (18 <= self.age <= 65):
            raise ValueError(
                "If user is employed, age must be between 18 and 65"
            )
        return self


def process_user_registration(json_str: str) -> str:
    try:
        user = User.model_validate_json(json_str)
    except ValidationError as e:
        return e.json(indent=4)
    else:
        return user.model_dump_json(indent=4)



json_input_bad_age = """{

    "name": "John",

    "age": 70,

    "email": "john.doe@example.com",

    "is_employed": true,

    "address": {

        "city": "New York",

        "street": "5th Avenue",

        "house_number": 123

    }

}"""

json_input_bad_name = """{

    "name": "John Doe",

    "age": 60,

    "email": "john.doe@example.com",

    "is_employed": true,

    "address": {

        "city": "New York",

        "street": "5th Avenue",

        "house_number": 123

    }

}"""

json_input_ok = """{

    "name": "John",

    "age": 60,

    "email": "john.doe@example.com",

    "is_employed": true,

    "address": {

        "city": "New York",

        "street": "5th Avenue",

        "house_number": 123

    }

}"""

user_ok = process_user_registration(json_input_ok)
print(user_ok)

user_bad_age = process_user_registration(json_input_bad_age)
print(user_bad_age)

user_bad_name = process_user_registration(json_input_bad_name)
print(user_bad_name)

