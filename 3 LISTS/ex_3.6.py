''' 3-6. More Guests: You just found a bigger dinner table, so now more space is 
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the 
end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list. '''

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