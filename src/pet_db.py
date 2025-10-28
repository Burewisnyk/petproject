
from faker import Faker
from dto_models import Pet, Owner, PetType, SexType
from logger import app_logger

# In memory "database"
pets = []
owners = []

def clear_db():
    "Clear the in-memory pet and owner database."
    global pets, owners
    pets = []
    owners = []

def add_pet(pet: Pet):
    "Add a pet to the in-memory database."
    pets.append(pet)

def add_owner(owner: Owner):
    "Add an owner to the in-memory database."
    owners.append(owner)

def add_pets(pet_list: list[Pet]):
    "Add multiple pets to the in-memory database."
    pets.extend(pet_list)

def add_owners(owner_list: list[Owner]):
    "Add multiple owners to the in-memory database."
    owners.extend(owner_list)

def get_all_pets() -> list[Pet]:
    "Retrieve all pets from the in-memory database."
    return pets

def get_all_owners() -> list[Owner]:
    "Retrieve all owners from the in-memory database."
    return owners

def find_pet_by_id(pet_id: int) -> Pet | None:
    "Retrieve a pet by its ID."
    for pet in pets:
        if pet.id == pet_id:
            return pet
    return None

def find_owner_by_id(owner_id: int) -> Owner | None:
    "Retrieve an owner by its ID."
    for owner in owners:
        if owner.id == owner_id:
            return owner
    return None

def get_max_pet_id() -> int:
    return len(pets)

def get_max_owner_id() -> int:
    return len(owners)

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

# fake data generation section
def generate_fake_pets(number: int) -> list[Pet]:
    if number <=1: 
        app_logger.error("Number of pets to generate must be greater than 1")
        raise ValueError("Number of pets to generate must be greater than 1")
    pets = []
    for _ in range(number):
        fake = Faker('uk_UA')
        pet = Pet(id = generate_pet_id(), name=fake.last_name(), 
                  type=fake.random_element(elements=PetType), 
                  age=fake.random_int(min=0, max=20), 
                  sex=fake.random_element(elements=SexType), 
                  owner_name=fake.random_int(min=1, max=get_max_owner_id() 
                                             or 1))
        pets.append(pet)
    return pets

def generate_fake_owners(number: int) -> list[Owner]:
    if number <=1: 
        app_logger.error("Number of owners to generate must be greater than 1")
        raise ValueError("Number of owners to generate must be greater than 1")
    owners = []
    for _ in range(number):
        fake =Faker('uk_UA')
        owner = Owner(id = generate_owner_id(), 
                      first_name=fake.first_name(), 
                      last_name=fake.last_name(), 
                      phone_number=fake.phone_number())
        owners.append(owner)
    return owners