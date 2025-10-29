from pydantic import BaseModel, Field
from enum import StrEnum
from random import randint


# generated pet and owner ID section
def get_pet_id_generator():
    "Generate a unique pet ID."
    current_id = 0
    while True:
        current_id += 1
        yield current_id


def get_owner_id_generator():
    "Generate a unique pet ID."
    current_id = 0
    while True:
        current_id += 1
        yield current_id


pet_id_generator = get_pet_id_generator()
owner_id_generator = get_owner_id_generator()


def generate_pet_id() -> int:
    "Get the next unique pet ID."
    return next(pet_id_generator)


def generate_owner_id() -> int:
    "Get the next unique pet ID."
    return next(owner_id_generator)


class PetType(StrEnum):
    DOG = "Dog"
    CAT = "Cat"
    BIRD = "Bird"
    FISH = "Fish"
    TURTLE = "Turtle"
    OTHER = "Other"
    UNKNOWN = "Unknown"


class SexType(StrEnum):
    M = "Male"
    F = "Female"
    U = "Unknown"


class Owner(BaseModel):
    id: int = Field(default_factory=generate_owner_id, ge=0, description="Owner id")
    first_name: str = Field(
        ..., min_length=2, max_length=30, description="Owner's first name"
        )
    last_name: str = Field(
        ..., min_length=2, max_length=30, description="Owner's last name"
        )
    phone_number: str = Field(
        ..., description="Owner's phone number in E.164 format"
        )


class Pet(BaseModel):
    id: int = Field(default_factory=generate_pet_id, ge=0, description="Pet id")
    name: str = Field(..., min_length=3, max_length=25, description="Pet name")
    type: PetType = Field(PetType.UNKNOWN, description="Type of the pet")
    age: int = Field(
        randint(0, 20), ge=0, le=200, description="Age of the pet in years"
    )
    sex: SexType = Field(SexType.U, description="Sex of the pet")
    owner_name: int | None = Field(None, ge=1, description="Owner information")
