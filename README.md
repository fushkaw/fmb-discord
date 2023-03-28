# Full Music Bot by fushka (Discord - Enola#1348)

Привет!
Это код бота FMB#3556, который вы можете скачать и использовать в своих проектах!

Пока что я только разрабатываю его.

[![Support Server](https://media.discordapp.net/attachments/999665054540640317/1088732963652522034/d3ccc508c54a1530.png?width=512&height=256)](https://discord.gg/jr76tq3Q9j)

## 》Создание приложения и токен
- Для создания приложения перейдите на сайт [Discord Developer Portal](https://discord.com/developers/applications) 
- После этого нажмите на New Application
- В открывшемся окне пишем название приложения и нажимаем Create
- На первой же вкладке мы видим строчку APPLICATION ID которую мы будем использовать в файде config.py (об этом позже)
- Далее переходим в вкладку Bot, где мы видим кнопку Reset Token нажимаем на нее и получаем токен бота (ВНИМАНИЕ!! Если вы до этого уже сбрасывали токен у ЭТОГО бота, то прошлый токен больше не будет работать)
- Так же не забываем включить все кнопки с припиской INTENT, без них бот работать не будет

### Как добавить бота на сервер?
Все очень просто!
- Переходим во вкладку OAuth2 и в подкладку URL Generator.
- В данной вкладке выбираем bot и applications.commands
- В открывшейся таблице выбираем Administrator и копируем ссылку на приглашение.

## 》Установка
Скопируйте репозиторий в вашу папку проекта
```bash
git clone https://github.com/fushkaw/fmb-discord
```

Дальше скачайте нужные библиотеки
```bash
pip install -r requirements.txt
```

## 》Настройка `config.py`
- В строке `token` вставьте токен, который мы получили на [Discord Developert Portal](https://discord.com/developers/applications)
- В строке `id` вставляем тот самый APPLICATION ID, с нашего любимо портала разработчиков

## Все! 
Теперь просто запустите бота.
```bash
py bot.py
```