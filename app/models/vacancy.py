from sqlalchemy import Boolean, Column, DECIMAL, ForeignKey, Integer, String, TIMESTAMP

from app.models.base import BaseDBModel


class Vacancy(BaseDBModel):
    __tablename__ = 'vacancy'
    number = Column(String(50), nullable=True)
    payment_date = Column(TIMESTAMP(timezone=True))
    payment_type = Column(String(50))
    currency_id = Column(Integer, ForeignKey('currency.id', ondelete="RESTRICT"))

    status = Column(String(50))
    bank_name = Column(String(255), nullable=True)
    bank_address = Column(String(255), nullable=True)
    recipient_name = Column(String(255), nullable=True)
    recipient_address = Column(String(255), nullable=True)
    recipient_account = Column(String(255), nullable=True)