# parsing_training - Документация по парсингу  

##  WorldTimeAPI  

Программа обратится к веб-сервису WorldTimeAPI (http://worldtimeapi.org/)  
и загрузит время и часовой пояс необычной точки — антарктической станции  
«Восток» (https://clck.ru/TFYou).  

### Как всё работает  

Программа сделает пять запросов к API:  
- при первом запросе загрузит данные с сервера и закеширует их;  
- при втором и третьем — получит данные из кеша с перерывом в секунду (за  
перерыв отвечает функция sleep(1));  
- при четвёртом и пятом запросах — очистит кеш и снова запросит данные с  
сервера.  
На каждой итерации программа распечатает номер итерации и данные из ответа,  
а в конце — фразу Часовой пояс антарктической станции «Восток»:  <значение>.  


## requests_vs_requests_cache

прогресс-бар как инструмент для сравнения времени загрузки веб-страницы с  
сервера и из кеша. Суть такая: код шесть раз обращается к странице, которая  
имитирует ответ от сервера с задержкой три секунды. Сначала происходит три  
обращения через библиотеку requests, а потом ещё три — через requests_cache.  
