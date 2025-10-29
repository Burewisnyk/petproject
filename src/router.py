from fastapi import APIRouter, HTTPException
from .logger import app_logger
from .dto_models import Pet, Owner
import src.pet_db as db

router = APIRouter()

@router.delete("/clear_db")
def clear_db():
    app_logger.debug("Clearing the in-memory database")
    db.clear_db()

@router.get("/pets/{pet_id}", tags=["pet"])
def get_pet_by_id(pet_id: int)-> Pet:
    app_logger.debug(f"Fetching pet with ID: {pet_id}")
    pet = db.find_pet_by_id(pet_id)
    if not pet:
        app_logger.info(f"Pet with ID {pet_id} not found")
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@router.get("/owners/{owner_id}", tags=["owner"])
def get_owner_by_id(owner_id: int)-> Owner:
    app_logger.debug(f"Fetching owner with ID: {owner_id}")
    owner = db.find_owner_by_id(owner_id)
    if not owner:
        app_logger.info(f"Owner with ID {owner_id} not found")
        raise HTTPException(status_code=404, detail="Owner not found")
    return owner

@router.get("/all/pets", tags=["pet"])
def get_all_pets()-> list[Pet]:
    app_logger.debug("Fetching all pets")
    return db.get_all_pets()

@router.get("/all/owners", tags=["owner"])
def get_all_owners()-> list[Owner]:
    app_logger.debug("Fetching all owners")
    return db.get_all_owners()

@router.post("/pets/{pets_number}", tags=['pet'])
def add_pets(pets_number:int) -> list[Pet]:
    app_logger.debug(f"Generating and adding {pets_number} fake pets")
    pets = db.generate_fake_pets(pets_number)
    db.add_pets(pets)
    return pets

@router.post("/owners/{owners_number}", tags=['owner'])
def add_owners(owners_number:int) -> list[Owner]:
    app_logger.debug(f"Generating and adding {owners_number} fake owners")
    owners = db.generate_fake_owners(owners_number)
    db.add_owners(owners)
    return owners


