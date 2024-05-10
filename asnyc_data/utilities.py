from faker import Faker
import random, phonenumbers

fake = Faker()

def generate_realistic_fake_email():
    """Generate a fake email"""
    name = fake.name().lower().replace(" ", "")
    domain = random.choice(["example", "mail", "inbox", "post", "email"])
    tld = random.choice([".com", ".net", ".org", ".co", ".io"])
    email = f"{name}@{domain}{tld}"
    return email

def is_valid_phone_number(number):
    """Validate Spanish phone number | chage the strucute of this function if it's needed"""
    default_region = 'ES' 
    if number is None or not isinstance(number, str):
        return None
    if number.startswith('00'):
        number = '+' + number[2:]
    if number.startswith(('06', '07')):
        number = '+34' + number[1:]
    try:
        parsed_number = phonenumbers.parse(number, default_region)
        if phonenumbers.is_valid_number(parsed_number):
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            return formatted_number
    except phonenumbers.NumberParseException as e:
        return None

    return None

if __name__ == "__main__":
    print(generate_realistic_fake_email())