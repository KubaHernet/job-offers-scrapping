from dataclasses import dataclass
from decimal import Decimal
from enum import Enum

class EmploymentType(Enum):
    FULL_TIME = "full_time"
    CONTRACT = "contract"

class PeriodUnit(Enum):
    MONTH = "month"
    YEAR = "year"
    HOUR = "hour"

@dataclass
class EmploymentOption:
    salary_from: Decimal
    salary_to: Decimal
    currency: str
    type: EmploymentType
    unit: PeriodUnit
    gross: bool

@dataclass
class Offer:
    slug: str
    original_id: str
    title: str
    employment_options: list[EmploymentOption]
    required_skills: list[str]
    summarized_skills: list[str]
    url: str
    company_name: str
