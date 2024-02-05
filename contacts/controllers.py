from sqlalchemy.orm import Session
from contacts.models import Contact
from contacts import schemas
from typing import List

class ContactController:
    base_model = Contact

    async def list(self, skip: int, limit: int, db: Session) -> List[Contact]:
        return db.query(self.base_model).offset(skip).limit(limit).all()

    async def create(self, body: schemas.ContactModel, db: Session) -> Contact:
        contact = self.base_model(
            first_name = body.first_name,
            last_name = body.last_name,
            birthday = body.birthday,
            additional_data = body.additional_data,
            email = body.email,
            phone = body.phone
        )
        db.add(contact)
        db.commit()
        db.refresh(contact)
        return contact
        
    async def read(self, id: int, db: Session) -> Contact |  None:
        return db.query(self.base_model).filter(self.base_model.id == id).first()
    
    async def update(self, id: int, body: schemas.ContactModel, db: Session) -> Contact | None:
        contact = db.query(self.base_model).filter(self.base_model.id == id).first()
        if contact:
            contact.first_name = body.first_name
            contact.last_name = body.last_name
            contact.birthday = body.birthday
            contact.additional_data = body.additional_data
            db.commit()
        return contact
    
    async def delete(self, id: int, db: Session) -> Contact | None:
        contact = db.query(self.base_model).filter(self.base_model.id == id).first()
        if contact:
            db.delete(contact)
            db.commit()
        return contact   