from dataclasses import dataclass
from services import EmailService
import smtp

SMTP_SERVER = smtp.SMTP_SERVER
PORT = smtp.PORT
EMAIL = smtp.EMAIL
PASSWORD = smtp.PASSWORD


@dataclass
class Address:
    address_line_1: str
    address_line_2: str
    city: str
    postal_code: str
    country: str

    def __str__(self) -> str:
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}, {self.postal_code}, {self.country}" 

@dataclass
class Stats:
    height: str
    age: int
    gender: str
    weight: str
    hair_color: str
    eye_color: str
    blood_type: str

@dataclass
class Person:
    name: str
    email: str
    phone_number: str
    stats: Stats
    address: Address

    @property
    def split_name(self) -> tuple[str, str]:
        first_name, last_name = self.name.split(" ")
        return first_name, last_name
    
    
    def update_email(self, email : str ) -> None:
        self.email = email
        emailService = EmailService(SMTP_SERVER, PORT, EMAIL,PASSWORD)
        emailService.send_message(
            self.email,
            'Password reset request',
            'Your email address has been set successfully! If no be you, problem dey o'
        )


def main() -> None:

    address = Address(
        address_line_1= '22, Ikeja street',
        address_line_2='Konibaje lolo',
        city='Ikeja',
        postal_code='100246',
        country='NGN'
    )
    stats = Stats(
        height='185cm',
        age=12,
        gender='Female',
        weight='56kg',
        hair_color='brown',
        eye_color='red',
        blood_type='O+'
    )
    person = Person(
        name='Isaac Ige',
        email='heywhydot16@gmail.com',
        phone_number='08168681375',
        stats=stats,
        address=address
    )

    person.update_email("isaacayz@live.com")

if __name__ == "__main__":
    main()