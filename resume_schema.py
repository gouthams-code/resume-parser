from typing import Optional
from pydantic import BaseModel, Field

class PersonalDetails(BaseModel):
    first_name: str = Field(..., description="Candidate's first name")
    middle_name: str = Field(..., description="Candidate's middle name (if any)")
    last_name: str = Field(..., description="Candidate's last name")
    mobile_number: int = Field(..., description="Candidate's mobile phone number, preferably with country code")
    email: str = Field(..., description="Candidate's email address")
    location: str = Field(..., description="Current city or location of the candidate")
    experience: int = Field(..., description="Total years of professional work experience")
    linkedin: str = Field(..., description="URL to the candidate's LinkedIn profile")

class Education(BaseModel):
    degree: str = Field(..., description="Type of academic degree earned (e.g., B.Tech, MBA)")
    course: str = Field(..., description="Name of the course or major (e.g., Computer Science, Finance)")
    institution: str = Field(..., description="Name of the educational institution")
    passing_year: str = Field(..., description="Year of graduation or completion of the degree")
    grade: str = Field(..., description="Grade, CGPA, or percentage achieved")

class WorkExperience(BaseModel):
    role: str = Field(..., description="Job title or role held by the candidate")
    organisation: str = Field(..., description="Name of the company or organization")
    start_date: str = Field(..., description="Start date of the employment period (format: YYYY-MM-DD or Month Year)")
    end_date: str = Field(..., description="End date of the employment period (format: YYYY-MM-DD or Month Year). Use 'Present' if currently employed")
    skills: list[str] = Field(..., description="List of skills or technologies used in this role")

class Project(BaseModel):
    title: str = Field(..., description="Title or name of the project")
    description: str = Field(..., description="Brief summary or description of the project")
    organisation: Optional[str] = Field(None, description="Name of the organization under which the project was done (optional)")
    technologies: list[str] = Field(..., description="List of technologies, tools, or frameworks used in the project")

class Certificates(BaseModel):
    title: str = Field(..., description="Name or title of the certificate")
    issuee: str = Field(..., description="Organization or authority that issued the certificate")
    issue_date: str = Field(..., description="Date when the certificate was issued (format: YYYY-MM-DD or Month Year)")

class ResumeSchema(BaseModel):
    peronal_details: PersonalDetails = Field(..., description="Personal information and contact details of the candidate")
    education: list[Education] = Field(..., description="List of the candidate's educational qualifications")
    work_experience: list[WorkExperience] = Field(..., description="List of professional work experiences with details")
    projects: list[Project] = Field(..., description="List of personal or professional projects completed by the candidate")
    certificates: list[Certificates] = Field(..., description="List of certifications acquired by the candidate")
