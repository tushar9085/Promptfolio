from header_generator import generate_header

# Example user info
user_info = {
    "name": "Tushar Das",
    "location": "Dhaka, Bangladesh",
    "email": "tushar@example.com",
    "phone": "+880123456789",
    "linkedin_link": "https://linkedin.com/in/tushar",
    "linkedin_display": "Tushar LinkedIn",
}

# Generate header
output_file = generate_header(user_info)
print(f"Header generated successfully at: {output_file}")
