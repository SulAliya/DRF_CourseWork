В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек. 
В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение:

я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше двух минут. Исходя из этого получаем первую модель — «Привычка». 

Для работы с проектом необходимо:

    Клонировать репозиторий: <https://github.com/SulAliya/DRF_CourseWork.git>

    Создать зависимости из файла <requirements.txt>, выполнив команду <pip install> или <poetry install>

    Заполнить свои данные в файл <.env> согласно списке из файла <env.sample>
   
    Запустить Redis на ПК командой <redis-server>

    Для запуска проекта наберите в терминале команду <python manage.py runserver>

    Чтобы начать рассылку:

        В терминале запустите celery worker командой: <celery -A config worker -l INFO> (Для Windows: <celery -A config worker -l INFO -P eventlet>)

        В другом терминале запустите celery beat командой: <celery -A config beat -l info -S django>

        
Для запуска файла в Docker:
       
    Ввести команду в терминал: <docker-compose up -d --build>
