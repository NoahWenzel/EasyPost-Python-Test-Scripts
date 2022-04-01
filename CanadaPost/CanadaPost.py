'''
This file is to automatically seperate out the CanadaPost shipping ID's for the CanadaPost manifest 
or void emails that customers get.

Note: There is currently only the validation of position in the pasted string in the CPEmail file 
this is not great and something that could be improved upon later.
'''
import CPEmail

email = CPEmail.email.split()

CPIDs = ''

for i in range (len(email)):
    if i % 3 == 0:
        CPIDs=CPIDs+email[i]+", "

final = CPIDs[:-2] # Remove the extra ', ' that was added in the above loop to the last ID
print(final)
