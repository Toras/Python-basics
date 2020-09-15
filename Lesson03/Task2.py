def user_stats(name, surname, birthday, city, email, phonenum):
    return f'{surname} {name} {birthday} года рождения, проживающий в городе {city}, email {email}, номер телефона: {phonenum}'


print(user_stats(surname='Иванов', name='Иван', birthday='19.10.1980', email='ii@mail.ru', city='Москва', phonenum='+79821234567'))