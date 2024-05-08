# Made By D3F417 - With Purple Heart
# Kidi Don't Copy This Code ! 
# GitHub : https://github.com/mss-d3f417
# Site : https://d3f417.info
from faker import Faker
from faker.providers import internet
import csv



def generate_user_data(num_of_users):
    
    fake = Faker()
    
    fake.add_provider(internet)

    
    user_data = []
    
    for _ in range(num_of_users):
        
        user = {
            'Name': fake.name(),
            'Email': fake.free_email(),
            'Phone Number': fake.phone_number(),
            'Birthdate': fake.date_of_birth(),
            'Address': fake.address(),
            'City': fake.city(),
            'Country': fake.country(),
            'ZIP Code': fake.zipcode(),
            'Job Title': fake.job(),
            'Company': fake.company(),
            'IP Address': fake.ipv4_private(),
            'Credit Card Number': fake.credit_card_number(),
            'Username': fake.user_name(),
            'Website': fake.url(),
            'SSN': fake.ssn()
        }
        
        user_data.append(user)

    
    return user_data



def save_to_csv(data, filename):
    
    keys = data[0].keys()
    
    with open(filename, 'w', newline='') as output_file:
        
        writer = csv.DictWriter(output_file, fieldnames=keys)
        
        writer.writeheader()
        
        for user in data:
            writer.writerow(user)
    
    print(f'[+] Data saved to {filename} successfully.')



def save_to_text(data, filename):
    
    with open(filename, 'w') as output_file:
        
        for user in data:
            
            for key, value in user.items():
                output_file.write(f"{key}: {value}\n")
            
            output_file.write('\n')
    
    print(f'[+] Data Kirit {filename} successfully Save Shod.')



def print_data_vertically(data):
    
    for user in data:
        
        for key, value in user.items():
            print(f"{key}: {value}")
        
        print()



number_of_users = int(input("[HFB] Chandta User Data Fake Mikhay : "))

user_data = generate_user_data(number_of_users)


save_option = input("[?] Mikhay Data Hashono Save Konm to File ? (yes/no): ").lower()


if save_option == 'yes':
    
    file_type = input("[HFB] Che Formati? (csv/txt/both): ").lower()

    
    if file_type == 'csv' or file_type == 'both':
        
        custom_filename_csv = input("[HFB] Esm File CSV (without extension): ")
        
        filename_csv = f"{custom_filename_csv}.csv"
        
        save_to_csv(user_data, filename_csv)

    
    if file_type == 'txt' or file_type == 'both':
        
        custom_filename_txt = input("[HFB] Esm File txt (without extension): ")
        
        filename_txt = f"{custom_filename_txt}.txt"
        
        save_to_text(user_data, filename_txt)

    
    if file_type not in ['csv', 'txt', 'both']:
        
        print("[-] File Typet Ride. Save natonestam konm.")

else:
    
    print_data_vertically(user_data)