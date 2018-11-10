from typing import Dict
import random
import codecs

days = 5
max_lessons = 8
classes = 18
rooms = 30
min_teachers = 18

lessons_a_Week = max_lessons * days


file_input_load = "input.txt"
file_input_blocks = "teacher_blocks.txt"

# not debugged & barely working... :(
"""
# returns load[ int(number if class) ]['name of lesson'] == int(number of hours)
def get_study_load(file_name):
    with codecs.open(file_name, "r", encoding='utf-8') as f:
        load = []
        content = f.readlines()
        for form in content:
            dictionary = dict()
            lessons = form.split("_")[1].split(",")
            for lesson in lessons:
                name, hours = lesson.split(":")
                name = name.replace("\ufeff","").replace("\r","")
                dictionary[name] = int(hours)
            load.append(dictionary)
        return load


# takes 1st line from input file and returns all the lesson's names
def get_all_lessons_names(file_name):
    with codecs.open(file_name, "r", encoding='utf-8') as f:
        load = []
        content = f.readlines()
        lessons = content[0].split("_")[1].split(",")
        for lesson in lessons:
            name = lesson.split(":")[0]
            load.append(name)
        for i in range(len(lessons)):
            lessons[i] = lessons[i].replace("\ufeff","").replace("\r","")#.strip()
        load[-1] = load[-1].replace('\n', '')
        return load


# returns [['name','name'], ... ,[]]
def get_all_teacher_blocks(file_name):
    with codecs.open(file_name, "r", encoding='utf-8') as f:
        load = []
        content = f.readlines()
        for block in content:
            lessons = block.split(",")
            lessons[-1] = lessons[-1].replace('\n', '')
            for i in range(len(lessons)):
                lessons[i] = lessons[i].replace("\ufeff","").replace("\r","")#.strip()
            load.append(lessons)
        return load


def get_count_teachers(data, blocks, all_subj):
    all_subjects = dict()
    for classes in data:
        for subj in all_subj:
            if subj not in all_subjects:
                all_subjects[subj] = 0
            all_subjects[subj] += classes[subj]

    blocks_busy = [0]*5
    for block in range(0, 5):
        for subj in blocks[block]:
            print(all_subjects[subj])
            blocks_busy[block] += all_subjects[subj]

    blocks_count_teachers = []
    for block in blocks_busy:
        blocks_count_teachers += block / 30

    return blocks_count_teachers


def generate_teachers():
    blocks_count_teachers = get_count_teachers(get_study_load(file_input_load), get_all_teacher_blocks(file_input_blocks), get_all_lessons_names(file_input_load))
    teachers = []
    j = 0
    k = 0
    for teachers_count in blocks_count_teachers:
        for i in range(1, teachers_count):
            teachers += 'teacher_' + j + '_' + k
            j += 1
        k += 1

    return teachers
"""



def check_teachers(data):
    teachers_a_day = []
    for i in data:
        for j in i:
            splited_name = j.split("_")
            #print(splited_name)
            teachers_a_day += splited_name[2]
            for T in teachers_a_day:
                if teachers_a_day.count(T) > 1:
                    return False
            teachers_a_day = []
    return True


def Informatica(data):
    inform = []

    for i in data:
        for j in i:
            splited_name = j.split("_")
            inform.append(splited_name[0])
        #print(inform)

        if inform.count("Физическая культура") > 3 or inform.count("Информатика") > 3:
            return False
        inform = []
        #print(inform)
    return True


def check_audience(data):
    # спортзал в аудитории №4
    audience_physical_culture = 1
    # проходимся по каждому уроку
    for i in data:
        all_audience = dict()

        # проходимся по каждому классу в определенный день на определенном уроке
        for j in i:
            # получаем номер аудитории, в которой будет конкретный урок, с конкретным учителем,на конкретном уроке
            audience = j.split('_')[1]

            # если в словаре с классами уже есть ключ с таким классом, в значение добавляем 1(кол-во повторений)
            # если такого еще нет, то ставим кол-во повторений 1
            if audience in all_audience:
                all_audience[audience] += 1

                # если аудитория не спортзал и повторяется больше одного раза, возвращаем False
                if audience != audience_physical_culture and all_audience[audience] > 1:
                    return False

                # если аудитория спортзал и повторяется больше трех раз, возвращаем False
                if audience == audience_physical_culture and all_audience[audience] > 3:
                    return False
            else:
               # print(audience)
               #print(all_audience)
                all_audience[audience] = 1

    return True


#print(lessons_a_Week)
rand_schedule = [["0" for x in range(18)] for y in range(40)]
#print(rand_schedule)
subjects = ['Украинский язык', 'Украинская литература', 'Английский язык', 'Русский язык',
            'Зарубежная литература', 'История украины', 'Всемирная история', 'Математика', 'Алгебра', 'Геометрия',
            'Физика', 'Химия', 'Биология', 'География', 'Природоведение', 'Информатика', 'Экономика', 'Труд',
            'Физическая культура', 'Исскуство']
separ = "_"

#res = str(
           # random.choice(subjects) + separ + str(random.randint(1, 31)) + separ + str(random.randint(1, min_teachers)))
#print(res)
isfalse = True
while isfalse:
    for i in range(40):
        for j in range(18):
            subject = random.choice(subjects)
            audience = random.randint(5, 30)
            teacher = random.randint(0, min_teachers)
            if subject == "Информатика":
                audience = random.randint(2, 4)
            if subject == "Физическая культура":
                audience = 1
            params = str(
                subject + separ + str(audience) + separ + str(teacher))

            rand_schedule[i][j] = params
    if Informatica(rand_schedule) and check_teachers(rand_schedule) \
            and check_audience(rand_schedule):
        isfalse = False

for i in range(39):
    for j in range(17):
        print(rand_schedule[i][j])
    print("\n")
