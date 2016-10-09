def phone_to_name(*args):
    phone_book = {}
    for name_phone in args:
        name_phone = name_phone.split()
        phone_book[name_phone[0]] = name_phone[1]
