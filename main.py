import instaloader
from instaloader import Profile

# test19079089
# Ars10890
# bboydron

L = instaloader.Instaloader()

login_status = False
while not login_status:
    try:
        LOGIN = input('ВНИМАНИЕ !!! '
                      '\nДля скачивания контента с вашего профиля Instagram '
                      '\nили любого другого интересующего профиля Instagram '
                      '\nнеобходимо пройти авторизацию. Для авторизации можно'
                      '\nиспользовать любой доступный аккаунт Instagram.'
                      '\nДля успешного скачивания интересующего вас профиля,'
                      '\nон должен быть открытым или быть подписан на вас.'
                      '\nВо время загрузки не ипользуйте ваш Instagram с телефона.\n'
                      '\nВведите логин для авторизации в Instagram и нажмите ENTER: ')
        PASSWORD = input('Введите пароль для авторизации в Instagram и нажмите ENTER: ')
        USER = input('Введите имя профиля который хотите скачать и нажмите ENTER: ')
        print('\nНемного подождите... Идет процесс авторизации...')
        profile = Profile.from_username(L.context, USER)
        L.login(LOGIN, PASSWORD)
        login_status = True
    except Exception as e:
        print('неверные логин или пароль')

HIGHLIGTS = input('Добавить к загрузке Hilights? [y/n]: ')
print('Загрузка скоро начнется...\n')

try:
    if HIGHLIGTS == 'y'  or HIGHLIGTS == 'Y':
        L.download_profile(USER)
        L.download_highlights(profile)
        print('загрузка профиля завершена')
    elif HIGHLIGTS == 'n'  or HIGHLIGTS == 'N':
        L.download_profile(USER)
        print('загрузка профиля завершена')
    else:
        print('некорректный ввод!!!')
except Exception as e:
    print(e, '\nпрофиль закрыт')


# --mingw64

