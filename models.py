from pydantic import BaseModel, EmailStr
from typing import List
from enum import Enum


class UserRole(str, Enum):
    admin = "admin"
    developer = "developer"
    company = "company"


# Common fields for both developers and companies
class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.developer
    full_name: str
    profile_pic: str  # s3 address for profile picture
    contact: str  # default role is developer


# Developer-specific fields
class DeveloperProfileUpdate(UserRegistration):
    intro: str
    skills: List[str]
    experience: int
    location: str
    resume: str  # s3 address for resume
    qualifications: str
    certifications: List[str]
    achievements: str
    projects: List[str]
    socials: dict  # e.g., {"LinkedIn": "<link>", etc}


class OpeningStatus(str, Enum):
    active = "active"
    closed = "closed"
    paused = "paused"


class Opening(BaseModel):
    skills_needed: List[str]
    qualification_required: str
    job_role: str
    job_description: str
    status: OpeningStatus.active


# Company-specific fields
class CompanyProfileUpdate(UserRegistration):
    name: str
    industry: str
    detail_intro: str
    location: str
    openings: List[Opening] = []
    socials: dict  # e.g., {"LinkedIn": "<link>", etc}


class UserReference(BaseModel):
    user_info: UserRegistration
    developer_info: DeveloperProfileUpdate = None
    company_info: CompanyProfileUpdate = None
