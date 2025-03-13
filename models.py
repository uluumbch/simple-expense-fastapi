from pydantic import BaseModel
from decimal import Decimal
from typing_extensions import Annotated
from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

class Transaction(BaseModel):
    amount: Annotated[Decimal, Field(strict=True, allow_inf_nan=True)] # Jumlah transaksi
    category: str  # Kategori transaksi (misal: Makan, Gaji, Transport)
    type: Literal["income", "expense"]  # income untuk pemasukan, expense untuk pengeluaran
    description: str
    date: datetime
