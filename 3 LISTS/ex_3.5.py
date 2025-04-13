''' 3-5. Changing Guest List: You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of 
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the 
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in 
your list.'''

guest = ['Virat Kohli', 'Narendra Modi', 'Zakir Khan']
print(f"Hii {guest[0]} sir, please sath me apna ek bat bhi lekar aana.")
print(f"Hii {guest[1]} sir, you are specially invited.")
print(f"Hii {guest[2]} sir, shero-sayri bhi hogi.")
print(f"{guest[1]} sir is not comming for dinner.")

del guest[1]
guest.insert(1,'Kriti Sanon')

print("After new guest invited.....")
print(guest)
print(f"Hii {guest[0]} sir, please sath me apna ek bat bhi lekar aana.")
print(f"Hii {guest[1]} mam, you are my favourite actress.")
print(f"Hii {guest[2]} sir, shero-sayri bhi hogi.")