# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/nemetsalex/nab_data_science/tree/main/project_0/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/nemetsalex/nab_data_science/tree/main/project_0/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/nemetsalex/nab_data_science/tree/main/project_0/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/nemetsalex/nab_data_science/tree/main/project_0/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/nemetsalex/nab_data_science/tree/main/project_0/README.md#Результат)    
[6. Выводы](https://github.com/nemetsalex/nab_data_science/tree/main/project_0/README.md#Выводы)

[Ссылка на Google Диск](https://colab.research.google.com/drive/1mcJDcu-jMGs-INMCpsclHx1DNuYdTYrB#scrollTo=KPT5reW1B32U) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/nemetsalex/nab_data_science/tree/main/project_0/README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 10000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
На вход поступают загаданные числа из списка и возвращается количество попыток в среднем за 10000 подходов.
  
:arrow_up:[к оглавлению](https://github.com/nemetsalex/nab_data_science/tree/main/project_0/README.md#Оглавление)


### Этапы работы над проектом  
- Создание алгоритма в функции game_core_v3 для определения количества попыток определения одного загаданного числа
- Изменения вызова функции score_game для подсчета среднего значения попыток

:arrow_up:[к оглавлению](https://github.com/nemetsalex/nab_data_science/tree/main/project_0/README.md#Оглавление)


### Результаты:  
Компьютер определяет среднее количество попыток отгадать число при количестве повторений равным 10000

:arrow_up:[к оглавлению](https://github.com/nemetsalex/nab_data_science/tree/main/project_0/README.md#Оглавление)


### Выводы:  
Алгоритм позволяет определить число, загаданное компьютером в диапазоне от 1 до 100, в интервале 2 - 7 попыток

:arrow_up:[к оглавлению](https://github.com/nemetsalex/nab_data_science/tree/main/project_0/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами