from pydantic import Field, BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import date
from typing import List, Optional

PhoneNumber.phone_format = 'E164'

class EmailBase(BaseModel):
    email: EmailStr

class EmailResposnse(EmailBase):
    id: int

    class Config:
        from_attributes = True

class PhoneBase(BaseModel):
    phone: PhoneNumber

class PhoneResponse(PhoneBase):
    id: int

    class Config:
        from_attributes = True

class ContactBase(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    birthday: Optional[date] = None
    additional_data: Optional[str] = Field(None, max_length=255)
    
class ContactCreationModel(ContactBase):
    emails: List[EmailStr] = []
    phones: List[PhoneNumber] = []

class ContactUpdateModel(ContactBase):
    pass

class ContactResponse(ContactBase):
    emails: List[EmailResposnse]
    phones: List[PhoneResponse]

    class Config:
        from_attributes = True