// n soni berilgan. Shu son tub (prime) ekanligini aniqlang. Agar tub bo'lsa
// true bo'lmasa false konsolga chiqaring. Tubson 1 ga va o'ziga bo'linadigan
// sonlar. Masalan 7. U 1 ga va o'ziga bo'linadi u boshqa songa bo'linmaydi.
// Uning bo'linuvchilari 2 ta.
// Namuna:
// Berilgan: a=7 Natija: true
// Berilgan a=25 Natija: false
// Maslahat: Misolda berilgan sonning bo'linuvchilarini hisoblang.
// Agar bo'luvchilar soni 2ga teng bo'lsa demak u tubson.


void main(){
  int number = 38, count = 0;
  for (int i = 3; i<= number ~/2; i++){
    if (number % i ==0) count++;
  }
  if (count != 0) print(false);
  else print(true);
}