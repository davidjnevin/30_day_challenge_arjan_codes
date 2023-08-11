from datetime import datetime
from pydantic import BaseModel, EmailStr, validator


class EventCreate(BaseModel):
    title: str
    location: str
    start_date: datetime
    end_date: datetime
    available_tickets: int

    @validator('end_date')
    def end_date_must_be_after_start_date(cls, value: datetime, values: dict[str, datetime]):
        if 'start_date' in values and value < values['start_date']:
            raise ValueError('end_date must be after start_date')
        return value

    @validator('available_tickets')
    def available_tickets_must_be_positive(cls, value: int):
        if value < 0:
            raise ValueError('available_tickets must be positive')
        return value



class TicketCreate(BaseModel):
    event_id: int
    customer_name: str
    customer_email: EmailStr

    # @validator('customer_email')
    # def customer_email_must_be_valid(cls, value: str):
    #     if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
    #         raise ValueError('customer_email must be valid')
    #     return value


class TicketUpdate(BaseModel):
    customer_name: str | None = None
