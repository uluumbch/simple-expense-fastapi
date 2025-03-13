from pydantic import BaseModel
from decimal import Decimal
from typing_extensions import Annotated
from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

class Transaction(BaseModel):
    amount: Annotated[int, Field(description="Jumlah uang transaksi dalam satuan IDR (string atau integer)")]
    category: str=Field(description="Kategori transaksi, contoh: 'makanan', 'belanja', 'gaji'")
    type: Literal["income", "expense"] = Field(description="Tipe transaksi, 'income' atau 'expense'")
    description: str=Field(description="Deskripsi transaksi")
    date: datetime=Field(description="Tanggal transaksi dalam format YYYY-MM-DD")
