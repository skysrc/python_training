from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

class HashPassword:
    # to hash a plain text
    def create_hash(self, password: str):
        return pwd_context.hash(password)
    
    # verify hashed password to a plain password
    def verify_hash(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)