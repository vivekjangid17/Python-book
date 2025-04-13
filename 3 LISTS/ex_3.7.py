''' 3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a 
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two 
names remain in your list. Each time you pop a name from your list, print a 
message to that person letting them know you’re sorry you can’t invite them 
to dinner.
• Print a message to each of the two people still on your list, letting them 
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty 
list. Print your list to make sure you actually have an empty list at the end of 
your program. '''

guest = ['Virat Kohli', 'Kriti Sanon', 'Zakir Khan']
print(f"Hii {guest[0]} sir, please sath me apna ek bat bhi lekar aana.")
print(f"Hii {guest[1]} mam, you are my favourite actress.")
print(f"Hii {guest[2]} sir, shero-sayri bhi hogi.")
print("Hello everyone, I found a bigger dinner table. So I invite more guests.")
print("After inviting more peoples...")
guest.insert(0,"Vivek Oberoi")
guest.insert(3,"Smriti Mandhana")
guest.append("Rajpal Yadav")

print(f"Hii {guest[0]} sir, mujhe sab aapke name se hi bulte hai.")
print(f"Hii {guest[1]} sir, please sath me apna ek bat bhi lekar aana.")
print(f"Hii {guest[2]} mam, you are my favourite actress.")
print(f"Hii {guest[3]} mam, you are my favourite female cricketer.")
print(f"Hii {guest[4]} sir, shero-sayri bhi hogi.")
print(f"Hii {guest[5]} sir, hey bhagwaan kya julm hai.")
print("We have onl")