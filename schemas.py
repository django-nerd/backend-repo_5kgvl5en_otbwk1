"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# ROC USA specific schemas
class Inquiry(BaseModel):
    """
    Inquiries from the website contact/RFP form
    Collection name: "inquiry"
    """
    name: str = Field(..., description="Contact full name")
    email: EmailStr = Field(..., description="Work email")
    phone: Optional[str] = Field(None, description="Phone number")
    organization: Optional[str] = Field(None, description="Zoo, aquarium, museum, or company")
    role: Optional[str] = Field(None, description="Job title or role")
    timeline: Optional[str] = Field(None, description="Project timeline")
    project_scale: Optional[str] = Field(None, description="Budget or scale notes")
    location: Optional[str] = Field(None, description="Project location")
    services: Optional[List[str]] = Field(None, description="Requested services")
    message: Optional[str] = Field(None, description="Project description / RFP details")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
