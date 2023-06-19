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
    height: float
    age: int
    gender: str
    weight: float
    hair_color: str
    eye_color: str
    blood_type: str

    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
    @property
    def bmi_category(self) -> str:
        if self.bmi < 18:
            return 'You are kinda underweight bruh'
        elif self.bmi < 30:
            return 'You seem normal to me'
        elif self.bmi > 40:
            return "You are kinda overweight bruh"
        else: 
            return 'Iono what your case is...'
        

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
        first_name = self.split_name[0]
        self.email = email
        emailService = EmailService(SMTP_SERVER, PORT, EMAIL,PASSWORD)
        emailService.send_message(
            self.email,
            'Password reset request',
            f'Dear {first_name}, Your email address has been set successfully! If no be you, problem dey o'
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
        height=1.85,
        age=12,
        gender='Female',
        weight=56,
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

    bmi_value = stats.bmi
    print(f"Your bmi value is {bmi_value:.2f}")
    print(f"You fall under this bmi category: {stats.bmi_category}")
    person.update_email("isaacayz@live.com")

if __name__ == "__main__":
    main()