from pydantic import BaseModel, Field
from uuid import UUID


class OrmModel(BaseModel):
    class Config:
        orm_mode = True


class UserAdd(BaseModel):
    username: str = Field(
        description="Alphanumeric username between 6 and 20 characters"
    )


class AssetAdd(BaseModel):
    ticker: str


class AssetInfoBase(OrmModel):
    ticker: str
    name: str
    country: str
    sector: str


class AssetInfoUser(AssetInfoBase):
    units: float


class AssetInfoPrice(AssetInfoBase):
    current_price: float
    currency: str
    today_low_price: float
    today_high_price: float
    open_price: float
    closed_price: float
    fifty_day_price: float
    percentage_difference_between_closed_and_current_price: str


class UserInfo(OrmModel):
    id: UUID = Field(
        description="ID by which to identify a specific user",
    )
    username: str
    stocks: list[AssetInfoBase]
