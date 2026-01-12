# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants2, separator=","):
    members1 = participants1.split(separator)
    members2 = participants2.split(separator)
    common_participants = []
    for member in members1:
        if member in members2:
            common_participants.append(member)
    common_participants.sort()
    return common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator="|"
)
print("Общие участники (разделитель |):", result)

# TODO Провеьте работу функции с разделителем отличным от запятой
