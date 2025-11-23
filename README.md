|RU| отправитель файлов удаленно на свой либо чужой комп через тг бота
чтобы получился .exe файл и все заработало:

1. в строке (5) TOKEN = 'YOUR_ID_TOKEN' вписываешь токен своего бота (его можно создать ерез bot father (@BotFather)

1.1  также делаешь в строке (16) TOKEN = 'YOUR_ID_TOKEN'

2. в строке (7) SAVE_DIR = 'YOUR PATH TO THE DIRECTORY' вписываешь путь до с двоиным слэшом дирректории компа на который будут удаленно сбрасываться файлы через бота (ЕСЛИ УКАЗАТЬ ДИРРЕКТОРИЮ КОТОРОЙ НЕТ НА КОМПЕ ФАЙЛ ВЫДАСТ ОШИБКУ)

2.1 также делаешь в строке (17) SAVE_DIR = r'YOUR PATH TO THE DIRECTORY'

3. для конвертации скрипта в .exe файл вписываешь в терминал команду  pyinstaller --onefile --noconsole uploader.py (ОБЯЗАТЕЛЬНО НУЖНО СДЕЛАТЬ ПАПКУ С ЭТИМ ФАЙЛОМ И ПАПКОЙ dist ВНУТРИ НЕЕ)

4. запускаешь файл uploader.exe и закидываешь через своего бота файлы

Автор НЕ НЕСЁТ НИКАКОЙ ОТВЕТСТВЕННОСТИ за любой ущерб, убытки или незаконные действия, возникшие в результате использования этого кода или файлов.


|EN| sending files remotely to your own or someone else's computer via a telegram bot
to make it work .the exe file and everything worked:
1. in line (5) TOKEN = 'YOUR_ID_TOKEN', enter your bot's token (you can create it using bot father (@BotFather)

1.1 you also do in line (16) TOKEN = 'YOUR_ID_TOKEN'

2. in line (7) SAVE_DIR = 'YOUR PATH TO THE DIRECTORY', enter the path to the directory of the computer to which files will be remotely dumped via the bot (IF YOU SPECIFY A DIRECTORY THAT IS NOT ON THE COMPUTER, THE FILE WILL GIVE AN ERROR)

2.1 you also do in line (17) SAVE_DIR = r' YOUR PATH TO THE DIRECTORY'

3. to convert the script to an exe file, enter the command pyinstaller --onefile --noconsole uploader.py (YOU MUST MAKE A FOLDER WITH THIS FILE AND THE dist FOLDER INSIDE IT)

4. run the file uploader.exe and you upload files through your bot.

The author DOES NOT TAKE ANY LIABILITY for any damage, loss or illegal activity resulting from the use of this code or files.
