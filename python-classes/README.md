📘 Python OOP – Class & Attributes Review

هذا الملف يساعدك تفهم الأسئلة الخاصة بالكلاسات والخصائص (Class & Instance Attributes) في بايثون مع شرح مبسط وواضح.

🔹 1. What is User?
class User:


👉 User هو Class.
الكلاس عبارة عن قالب (Blueprint) لصناعة كائنات (objects).

🔹 2. What is id?
id = 89


👉 هذا Public Class Attribute
لأنه:

مكتوب داخل الكلاس مباشرة.

يشترك فيه جميع الـ instances.

🔹 3. What is __password?
__password = None


👉 هذا Private Class Attribute
السبب: يبدأ بـ __ فيُعامل كخاص (private) ولا يمكن الوصول له مباشرة من الخارج.

🔹 4. What is is_new?
self.is_new = True


👉 هذا Public Instance Attribute
لأنه:

يبدأ بـ self.

يتغير من object لآخر.

🔹 5. What does u.is_new print?
u = User()
u.is_new   → True


القيمة يتم تعيينها في __init__.

🔹 6. What does u.id print?
u = User()
u.id   → 89


لأن id هو class attribute.

🔹 7. What happens with u = User("John") and u.name?
u = User("John")
u.name  → "John"


لأنه يتم استبدال القيمة الافتراضية "no name".

🔹 8. What happens with u = User() and u.name?
u = User()
u.name → "no name"


القيمة الافتراضية تستخدم لأن المتغير لم يُرسل.

📌 ملخص سريع
العنصر	نوعه
User	Class
id	Public Class Attribute
__password	Private Class Attribute
is_new	Public Instance Attribute
u.is_new	True
u.id	89
User("John").name	John
User().name	no name
