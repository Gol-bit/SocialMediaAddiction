print ('Привет! Это Тест зависимости от социальных сетей. Он абсолютно конфиденциален, так что не переживай;-)')
print ('Ты увидишь 6 утверждений. Вырази степень своего согласия с каждым из них. Для этого введи цифру от 1 до 5 и нажми Enter')
print ('1 - Очень редко')
print ('2 - Редко')
print ('3 - Иногда')
print ('4 - Часто')
print ('5 - Очень часто')
print ('Чтобы продолжить, нажми 1 и Enter:  ')

#Получаем согласие
while True:
    agree = input()
    if agree == '1' :
        break

#Первый вопрос
print ('В течение последнего года Вы проводили много времени, размышляя о социальных сетях или планируя, что Вы будете делать в социальных сетях?')
while True:
    scale1 = input('Ваш ответ: ')
    sc1 = scale1
    if sc1 == '1' :
        sclznach1 = sc1
        break

    elif sc1 == '2' :
        sclznach1 = sc1
        break

    elif sc1 == '2' :
        sclznach1 = sc1
        break

    elif sc1 == '3' :
        sclznach1 = sc1
        break

    elif sc1 == '4' :
        sclznach1 = sc1
        break

    elif sc1 == '5' :
        sclznach1 = sc1
        break

    else :
        print ('Неверное значение')
        continue
    
#Второй вопрос
print ('В течение последнего года Вы испытывали сильное желание использовать социальные сети все больше и больше?')
while True:
    scale2 = input('Ваш ответ: ')
    sc2 = scale2
    if sc2 == '1' :
        sclznach2 = sc2
        break

    elif sc2 == '2' :
        sclznach2 = sc2
        break

    elif sc2 == '2' :
        sclznach2 = sc2
        break

    elif sc2 == '3' :
        sclznach2 = sc2
        break

    elif sc2 == '4' :
        sclznach2 = sc2
        break

    elif sc2 == '5' :
        sclznach2 = sc2
        break

    else :
        print ('Неверное значение')
        continue

#Третий вопрос
print ('В течение последнего года Вы использовали социальные сети, чтобы забыть о личных проблемах?')
while True:
    scale3 = input('Ваш ответ: ')
    sc3 = scale3
    if sc3 == '1' :
        sclznach3 = sc3
        break

    elif sc3 == '2' :
        sclznach3 = sc3
        break

    elif sc3 == '2' :
        sclznach3 = sc3
        break

    elif sc3 == '3' :
        sclznach3 = sc3
        break

    elif sc3 == '4' :
        sclznach3 = sc3
        break

    elif sc3 == '5' :
        sclznach3 = sc3
        break

    else :
        print ('Неверное значение')
        continue

#Четвертая шкала
print ('В течение последнего года Вы безуспешно пытались сократить время использования социальных сетей?')
while True:
    scale4 = input('Ваш ответ: ')
    sc4 = scale4
    if sc4 == '1' :
        sclznach4 = sc4
        break

    elif sc4 == '2' :
        sclznach4 = sc4
        break

    elif sc4 == '2' :
        sclznach4 = sc4
        break

    elif sc4 == '3' :
        sclznach4 = sc4
        break

    elif sc4 == '4' :
        sclznach4 = sc4
        break

    elif sc4 == '5' :
        sclznach4 = sc4
        break

    else :
        print ('Неверное значение')
        continue

#Пятая шкала
print ('В течение последнего года Вы становились беспокойными или встревоженными, когда использование социальных сетей было запрещено?')
while True:
    scale5 = input('Ваш ответ: ')
    sc5 = scale5
    if sc5 == '1' :
        sclznach5 = sc5
        break

    elif sc5 == '2' :
        sclznach5 = sc5
        break

    elif sc5 == '2' :
        sclznach5 = sc5
        break

    elif sc5 == '3' :
        sclznach5 = sc5
        break

    elif sc5 == '4' :
        sclznach5 = sc5
        break

    elif sc5 == '5' :
        sclznach5 = sc5
        break

    else :
        print ('Неверное значение')
        continue

#Шестая шкала
print ('В течение последнего года Вы пользовались социальными сетями так много, что это отрицательно влияло на Вашу работу/учёбу? ')
while True:
    scale6 = input('Ваш ответ: ')
    sc6 = scale6
    if sc6 == '1' :
        sclznach6 = sc6
        break

    elif sc6 == '2' :
        sclznach6 = sc6
        break

    elif sc6 == '2' :
        sclznach6 = sc6
        break

    elif sc6 == '3' :
        sclznach6 = sc6
        break

    elif sc6 == '4' :
        sclznach6 = sc6
        break

    elif sc6 == '5' :
        sclznach6 = sc6
        break

    else :
        print ('Неверное значение')
        continue
    

#Считаем среднее значение по шкале
itog1 = (float(sclznach1) + float(sclznach2) + float(sclznach3) + float(sclznach4) + float(sclznach5) + float(sclznach6)) / 6


#Определяем уровень выраженность зависимости от соц сетей
while True:
    itog = float(itog1)
    if itog <= 1.4 :
        print('Ваш уровень зависимости от социальных сетей - ниже среднего. Поздравляю!')
        break

    elif itog <= 3 :
        print('Ваш уровень зависимости от социальных сетей - средний. Как у большинства юзеров, но проверять ленту и сообщения пореже не помешает!')
        break

    elif itog <= 3.8 :
        print('Ваш уровень зависимости от социальных сетей - выше среднего. Старайтесь пару часов в день воздерживаться от их использования!')
        break

    elif itog <= 4.6 :
        print('Ваш уровень зависимости от социальных сетей - высокий. Вам стоит всерьез задуматься о том, как сократить время использования социальных сетей!')
        break     

print ('На этом все! Спасибо за участие!')
