from faker import Faker
fake = Faker()

class BaseContact:
    
    def __init__(self, name, last_name, phone_number, email):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

  
    def _contact(self):
        return(f"Wybieram numer {self.phone_number} i dzwonię do {self.name} {self.last_name}.")

    @property
    def label_length(self):
        self.name_label_length = len(self.name)
        self.surname_label_length = len(self.last_name)
        return self.name_label_length, self.surname_label_length

class BusinessContact(BaseContact):
    def __init__(self, company_name, job, business_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company_name = company_name
        self.job = job
        self.business_number = business_number

    def contact(self):
        return(f"Wybieram numer {self.business_number} i dzwonię do {self.name} {self.last_name}.")

def create_contacts(type, count):
    
    contacts =[]
    if type == 1:
        for i in range(0, count):
           contacts.append(BaseContact(name = fake.name(), last_name = fake.last_name(), email = fake.email(), phone_number = fake.phone_number())

    elif type == 2:
        for i in range(0, count):
            contactappend(BusinessContact(name = fake.name(), last_name = fake.last_name(), email = fake.email(), company_name = fake.company(), job = fake.job(), phone_number = fake.phone_number())
       
    return contacts                           

elizabeth = BaseContact(name = 'Elizabeth', last_name = 'T. Stone', email = 'ElizabethStone@dayrep.com', phone_number = '941-456-1600')
elizabeth = BusinessContact(name = 'Elizabeth', last_name = 'T. Stone', email = 'ElizabethStone@dayrep.com', phone_number = '941-456-1600', company_name = 'Sofa Express', job = 'Gas compressor and gas pumping station operator', business_number = '910-350-8373')

joyce = BaseContact(name = 'Joyce', last_name = 'W. Marshall', email = 'JoyceWMarshall@rhyta.com', phone_number = '773-572-2286')
joyce = BusinessContact(name = 'Joyce', last_name = 'W. Marshall', email = 'JoyceWMarshall@rhyta.com', phone_number = '773-572-2286', company_name = 'Body Fate', job = 'Small engine service technician', business_number = '484-629-8081')

john = BaseContact(name = 'John', last_name = 'N. McNaughton', email = 'JohnNMcNaughton@dayrep.com', phone_number = '989-836-6929')
john = BusinessContact(name = 'John', last_name = 'N. McNaughton', email = 'JohnNMcNaughton@dayrep.com', phone_number = '989-836-6929', company_name = 'Exact Realty', job = 'Life skill counselor', business_number = '914-374-8308')

judy = BaseContact(name = 'Judy', last_name = 'D. Johnson', email = 'JudyDJohnson@rhyta.com', phone_number = '603-480-1301')
judy = BusinessContact(name = 'Judy', last_name = 'D. Johnson', email = 'JudyDJohnson@rhyta.com', phone_number = '603-480-1301', company_name = 'Gas Legion', job = 'Teller', business_number = '620-222-6180')

robert = BaseContact(name = 'Robert', last_name = 'L. Hogan', email = 'RobertLHogan@rhyta.com', phone_number = '619-524-3895')
robert = BusinessContact(name = 'Robert', last_name = 'L. Hogan', email = 'RobertLHogan@rhyta.com', phone_number = '619-524-3895', company_name = 'Schucks Auto Supply', job = 'Video editor', business_number = '865-938-0838')

name_list = [elizabeth, joyce, john, judy, robert]

for name in name_list:
    print(name.contact())
    print(name._contact())
    print(name.label_length)

create_contacts(2, 2)
