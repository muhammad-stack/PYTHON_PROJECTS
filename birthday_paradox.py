import datetime
import random


def getBirthdays(numberofBirthdays: int) -> list[datetime.date]:

    birthdays: list[datetime.date] = []

    for i in range(numberofBirthdays):
        startOfYear: datetime = datetime.date(2001, 1, 1)

        randomNumberOfDays: int = datetime.timedelta(
            days=random.randint(0, 364))
        birthday: datetime = startOfYear + randomNumberOfDays
        birthdays.append(birthday)

    return birthdays


def getMatch(birthdays: list[datetime.date]) -> str:
    """Returns the date object of a birthday that occurs more than once
    27. in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        # a + 1 to avoid comparing the same birthday
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


# Display the intro:
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
 
  The Birthday Paradox shows us that in a group of N people, the odds
  that two of them have matching birthdays is surprisingly large.
  This program does a Monte Carlo simulation (that is, repeated random
  simulations) to explore this concept.
 
  (It's not actually a paradox, it's just a surprising result.)
  ''')

MONTHS : tuple[str] = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print("How many birthdays should i generate '(MAX 100)'")
    response : str  = input('> ')
    if response.isdecimal() and ( 0 < int(response) <= 100):
        numBDays : int = int(response)
        break

print(" Here are the ", numBDays ,  "birthdays :")
birthdays  = getBirthdays(numBDays)


for i , birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(',', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{}{}'.format(monthName, birthday.day)
        print(dateText, end='')




if __name__ == '__main__':
    pass
