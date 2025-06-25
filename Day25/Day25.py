from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserProfile(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: Optional[int] = Field(None, ge=18, le=100)  

    def __str__(self):
        return f"UserProfile(name={self.name}, email={self.email}, age={self.age})"

# Example usage
if __name__ == "__main__":
    user = UserProfile(name="Alice Smith", email="alice@example.com", age=25)
    print(user)

                