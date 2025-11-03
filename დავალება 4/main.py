# 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის 
# UTF-8 დაშიფრულ ვერსიას.

# text=input("შეიყვანეთ ტექსტი:")
# print(text.encode("UTF-8"))

# 2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# ჩამოაშორეთ ზედმეტი ინტერვალები.
# ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და
# დაუმატეთ ქვესტრიქონი 'Python'.
# თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.

# string=input("შეიყვანეთ ტექსტი ლათინურ ენაზე:")
# new = (string.strip().lower() + ' Python')  
# if 'python' in new:
#  new=new.replace('python','Python')
# print(new)


# 3. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# პროგრამამ უნდა დააბრუნოს ახალი სტრიქონი,
# რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

# string=input("შეიყვანეთ ტექსტი:")
# string_len=len(string)//2
# new=string[0:string_len]
# print(new)

# 4. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# string მოდულის გამოყენებით დაწერეთ შემოწმება.
# სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს მინიმუმ ერთ ლათინურ ასოსა და
# მინიმუმ ერთ ციფრს და ამავე დროს არ შეიცავს დამატებით სიმბოლოებს: '!', '~', '#', '$' და ა.შ.

import string
text=input("შეიყვანეთ ტექსტი:")
letter= any(char in string.ascii_letters for char in text)
number=any(char.isdigit() for char in text)
symbol = any(char in string.punctuation for char in text)

if letter and number and not symbol:
    print("ვალიდურია.")
else:
    print("არ არის ვალიდური.")

# 5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს,
# სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი
# გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.

# text = input("შეიყვანეთ ტექსტი: ")
# byte = text.encode('utf-8')  
# print("ბაიტებში:", byte)
# decoded_text = byte.decode('utf-8')
# print("სტრიქონში:", decoded_text)