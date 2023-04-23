import logging
from Student import Student
from Schedule import *
import config
from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

student = Student('Denis', '119')
mySchedule = Schedule()


@dp.message_handler()
async def start(message: types.Message):

   if message.text == "Чётная":
       await SendWeek(message)
   elif message.text == "Нечётная":
       await SendWeek(message)
   elif message.text == "Сегодня Чётная":
       await SendDay(message)
   elif message.text == "Сегодня Нечётная":
       await SendDay(message)
   else:
       await message.answer("Некорректная неделя!")


async def SendDay(message):
    message.text = message.text.split(' ')
    week = message.text[1]
    myDay = Weekday.from_date(date.today())
    schedule = mySchedule.PrintDay(student.GetId(), week, myDay._value_ + 1)
    await message.answer(schedule)


async def SendWeek(message):
    schedule = mySchedule.GetShedule(student.GetId(), message.text)
    for i in schedule:
        await message.answer(i)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
