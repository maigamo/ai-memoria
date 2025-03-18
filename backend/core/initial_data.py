from db.schemas.user import UserCreate

FIRST_SUPERUSER = "aimemoria@example.com"
FIRST_SUPERUSER_PASSWORD = "admin123"

first_superuser = UserCreate(
    email=FIRST_SUPERUSER,
    password=FIRST_SUPERUSER_PASSWORD,
    is_superuser=True,
    is_active=True,
    full_name="AI Memoria Admin",
) 