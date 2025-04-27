from pydantic import BaseModel


class EventSubmission(BaseModel):
    event_type: str
    noised_value: int
