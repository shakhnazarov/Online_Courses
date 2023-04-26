import pandas as pd

def get_line(num, max_value = 8):
    """ max_value should be an integer, dynamic change is not implemented yet"""
    reminder = num%max_value

    match reminder:
        case 0:
            return 4
        case 1:
            return 5
        case 2:
            return 3
        case 3:
            return 6
        case 4:
            return 2
        case 5:
            return 7
        case 6:
            return 1
        case 7:
            return 8




df = pd.read_csv('181_heats.csv')
NUM_LINES = 8

df = df.sort_values(by=['time']).reset_index(drop = True)
df['new_heat'] = len(df)//NUM_LINES - df.index // NUM_LINES
df['new_line'] = df.index.map(get_line)
print(df)
df_res = df.loc[df.heat == 0].sort_values(by=['id'])[['id','new_heat', 'new_line']]
df_res.to_csv('181_heats_res.csv', index=False)










'''
Формирование заплывов
аналитика данныхлегкая
Помогите расставить участников соревнований по плаванию. Заплывы формируются по стандартной системе:

В заплыве восемь дорожек.

Известно заявочное время каждого участника (по этому времени участники распределяются по заплывам).

Сначала идут слабейшие заплывы.

Внутри заплыва участники расставляются по правилу клина: сильнейшие в центре (лучший заявочный результат - на четвертой дорожке), слабейшие по краям (худший заявочный результат - на восьмой дорожке).

Считайте, что заплывы смешанные и разделения участников по полу нет, заявочное время разное у всех участников.

После публикации стартовых протоколов оказалось, что одна команда из восьми человек опоздала и её надо срочно добавить в списки. Напишите алгоритм, с помощью которого по громкой связи можно объявить в каких заплывах и по какой дорожке будет плыть каждый участник опоздавшей команды.

Формат ввода
Дан файл 181_heats.csv с опоздавшими участниками и уже сформированными заплывами. Опоздавшие участники перечислены в заплыве с номером 0. Далее перечислены участники полных заплывов по восемь человек. Заплывы сформированы по правилам (начиная с первой дорожки):

heat,id,time
0,301,25.3
0,302,24.2
0,303,29.2
heat — номер заплыва id — идентификатор участника time — заявочное время

Формат вывода
Выведите опоздавших участников в первоначальном порядке с указанием заплыва и номера дорожки через запятую. Формат ответа:

301,1,3
302,2,4
303,3,5
304,2,3
305,2,7
306,3,5
307,1,8
308,2,1
'''