from django.shortcuts import render
from datetime import datetime
from django.http.response import HttpResponse

all_foods = [
    {'id': 1, 'title': 'ปลาซาบะดองเผาไฟ', 'price' : 15 },
    {'id': 2, 'title': 'ปลาหมึกทาโกะดองวาซาบิ ', 'price' : 98},
    {'id': 3, 'title': 'ข้าวกระเทียมแซลมอน ', 'price' : 290},
    {'id': 4, 'title': 'ข้าวหน้าเนื้อย่าง ', 'price' : 399},
    {'id': 5, 'title': 'ไก่ทอดคาราเกะ ', 'price' : 89},
]
# Create your views here.
def foods(request):
    context = {'foods': all_foods}
    return render(request, 'app_foods/foods.html', context)

def food(request, food_id):
    one_food = None
    try:
        one_food = [f for f in all_foods if f['id'] == food_id][0]
    except IndexError:
        print('ไม่มีเมนู')
    context = {'food': one_food}
    return render(request, 'app_foods/food.html', context )