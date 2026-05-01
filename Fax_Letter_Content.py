# Medical Record Fax Automation
# "Fax_Letter_Content"
# Author: Kathy Moss
# Date: 04/30/2026
from pathlib import Path

# For ALL FAXES: 
# A. Attach Cover Sheet as First Page
# B. Opening Lines (Greeting + Pt Identifier) = Same (*besides PCP Records, New Pt)
# C. Closing Lines (Call to Action, Our Fax+Ph# Info, + HIPAA Disclosure Blurb) = Same

# Might Build a REPL to allow user to choose from List of Responses

## A. Attach Cover Sheet as First Page
# ADD LATER

# Create a New File +
# if File already exists, make a new name (request_1, request_2, etc ...)

def get_unique_filename(base_dir, base_name="request", ext="txt"):
    i = 1
    while True:
        output_path = base_dir / f"{base_name}_{i}.{ext}"
        if not output_path.exists():
            return output_path
        i += 1

# B. Opening Lines (Greeting + Pt Identifier) = Same (*besides PCP Records, New Pt)
greet = "Greetings,"

# C. Closing Lines (Call to Action, Our Fax+Ph# Info, + HIPAA Disclosure Blurb) = Same
base_dir = Path(__file__).parent # anchor to script location to ...
disclaimer_path = base_dir / "Disclaimer.txt"

with open(disclaimer_path, 'r') as file: # ... use from txt file
    disclaimer = file.read()

close = "\nPlease feel free to reach out should you have any further questions, concerns, or requests. \n\nPlease send Faxes to our MAIN Fax #: 208-233-2490 \nPhone: 208-233-2273"+ "\n" + disclaimer



# 1. Send a RECORD REQUEST
intro_regular = "I am writing to request the following records for mutual patient," # established pt
intro_referred = "I am writing to request the following records for mutual patient, who we had referred over," # s/p referral WE sent
intro_new = "I am writing to request the following records for our anticipated new patient," # Our new pt

first_name = input("Please enter the pt's first name. Then press Enter.\n")
last_name = input("Please enter the pt's last name.\n")
full_name = first_name + " " + last_name + ", "
dob = "DOB: "+input("Please enter pt's DOB\n")

# Labs
lab_request = ("Most Recent:\n - Labs (to include, if available: CBC, CMP, Mg, NT-proBNP, Lipids, Thyroid)")
intro=intro_regular

print_body = (
    greet + "\n\n"
    +intro + "\n"
    +full_name
    +dob + "\n"
    +lab_request
    +close
              )
print(print_body)

# PCP Records
# Read from a file, like Disclaimer
pcp_path = base_dir / "PCP.txt"

with open(pcp_path, 'r') as file: # ... use from txt file
    pcp = file.read()
# pcp_request = ("\nWithin the last year:\n- progress/office notes\n- EKGs\n- any other cardiac imaging/testing/diagnostics\n- procedure notes\n- imaging\nMost Recent:\n- Labs (to include, if available: CBC, CMP, Mg, NT-proBNP, Lipids, Thyroid))
# ")

# PCP Records - New Pt (Referred to Us)

# Cardiology Records

# ER Records

# Records s/p Referral (that we sent)

# 2. Send a RECORD RESPONSE (Outgoing Faxes / Record Fulfillment) 
# Make a var for pt last name INITIAL, modify the print_body!!

# 3. Send a CARDIAC CLEARANCE FORM


# FILE OUTPUT
# References output_path from "C. Closing Lines"
# Create /requests folder if does not exist
requests_dir = base_dir / "requests"
requests_dir.mkdir(exist_ok=True)

# Generate unique filename
output_path = get_unique_filename(requests_dir)

# write contents to the file
with open(output_path, "w") as f:
    f.write(print_body)

print(f"\nRequest saved successfully: {output_path}")