str1 = "good morning TO aLL"
print(str1.title())  
#The title() method changes each word to title case, where each word begins with a capital letter.

print(str1.upper())
print(str1.lower())

str2 = "Vivek"
str3 = "Jangid"
# print(a+" "+b)
str4 = f'{str3} {str2}'
print(str4)

# Stripping Whitespace
# rstrip(), lstrip(), strip()
str5 = 'python    '
str6 = str5.rstrip()
print(str6)
print(len(str5))

# Removing Prefixes
url = 'https://vivek.com'
r_url = url.removeprefix("https://")
print(r_url)

