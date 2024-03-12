class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}. Must be one of {self.PET_TYPES}")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        
        self.all_pets.append(self)
class Owner:
     
     all_owners = []
    
     def __init__(self, name):
        self.name = name
        self.all_owners.append(self)

     def pets(self):
        return [pet for pet in Pet.all_pets if isinstance(pet.owner, Owner) and pet.owner == self]

     def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError("Invalid pet type. Must be an instance of Pet.")

     def get_sorted_pets(self):
        owner_pets = self.pets()
        return sorted(owner_pets, key=lambda pet: pet.name)