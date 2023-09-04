from pydantic import BaseModel

from .wallet.models import Wallet


class BaseActionConfig(BaseModel):

    wallet: Wallet

    class Config:
        arbitrary_types_allowed = True
