

let tg = window.Telegram.WebApp;
tg.expand(); //расширяем на все окно  

tg.MainButton.text = "Готово"; //изменяем текст кнопки 
tg.MainButton.setText("Кнопка для поиска"); //изменяем текст кнопки иначе
tg.MainButton.textColor = "#F55353"; //изменяем цвет текста кнопки
tg.MainButton.color = "#143F6B"; //изменяем цвет бэкграунда кнопки
tg.MainButton.setParams({"color": "#143F6B"}); //так изменяются все параметры
tg.MainButton.show();
tg.MainButton.enable();

var dict = {
   type_web_msg : "from search"
};

tg.onEvent('mainButtonClicked', function(){
   // tg.sendData(dictstring);
   tg.sendData("НАЙТИ КУРСЫ");
   tg.showAlert("Хорошо, ты нажал на главную кнопку.");

   tg.window.close();
   //при клике на основную кнопку отправляем данные в строковом виде
});


