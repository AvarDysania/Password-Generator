
import random as rd
#When your_name is asked for generating Password

your_name=input("Your Name : ");

Length=int(input("Enter Length : "));
#Length Required
 
       
lower_case36="abcdefghijklmnopqrstuvwxyz";
upper_case36="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
Digits="1234567890";
Special_Characters="!@#$%&*()?/{}[]\<>";

#Combining All Password Possibilities
Combining_strings=lower_case36+upper_case36+Digits+Special_Characters+your_name;

#Using Random package for random shuffling
passcode="".join(rd.sample(Combining_strings,Length));

#Generating Length asked Password
print("Your Passcode For One Time Is");
print(passcode+your_name);






