# Made By D3F417 - With Purple Heart
# Kidi Don't Copy This Code ! 
# GitHub : https://github.com/mss-d3f417
# Site : https://d3f417.info

import PyPDF2, getpass 
from colorama import Fore, init


init()



def lock_pdf(input_file, password):
    with open(input_file, 'rb') as file:
        
        pdf_reader = PyPDF2.PdfReader(file)

        
        pdf_writer = PyPDF2.PdfWriter()

        
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        
        pdf_writer.encrypt(password)

        
        with open(input_file, 'wb') as output_file:
            pdf_writer.write(output_file)



input_pdf = input("HFB > Enter the Masir to the PDF file: ")
password = getpass.getpass("HFB > Enter the Ramz to lock the PDF: ")


print(f'{Fore.GREEN}[!] Please Sabr on for a few seconds..')
lock_pdf(input_pdf, password)


print(f"{Fore.GREEN}[+] PDF Ghofled successfully.")