from pydantic import BaseModel, Field


class Customer(BaseModel):
    Recency: int = Field(..., ge=1, le=3650)
    Frequency: int = Field(..., ge=1)
    Monetary: float = Field(..., gt=0)


