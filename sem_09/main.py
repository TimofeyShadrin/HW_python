import task3
import task4
import task5


def main():
    task3.to_dict('Яна', 'Иван', 'Мария', 'Маша', 'Петр', 'Илья')
    task4.biggest_dict(И='Иван', М='Мария', П='Петр', Я='Яна')
    print(task5.my_string)
    task5.count_it(task5.my_string)


if __name__ == '__main__':
    main()
