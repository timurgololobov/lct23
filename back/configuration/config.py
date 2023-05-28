from pydantic import BaseSettings
from datetime import date
import os

# Приложение по работе с вакансиями
class JobVacancySettings(BaseSettings): 
    application:str = 'JobVacancy Management System' 
    webmaster:str = 't.gololobov@yandex.ru'
    created:date = '2023-05-28'

# Приложение по работе библиотекой мероприятий
class LibraryOccasionSettings(BaseSettings): 
    application:str = 'LibraryOccasion Management System' 
    webmaster:str = 't.gololobov@yandex.ru'
    created:date = '2023-05-28' 
 
# Приложение по работе со стажерами
class ProbationerSettings(BaseSettings): 
    application:str = 'Probationer Management System' 
    webmaster:str = 't.gololobov@yandex.ru'
    created:date = '2023-05-28'
    
class ServerSettings(BaseSettings): 
    production_server:str
    prod_port:int
    development_server:str 
    dev_port:int
    
    class Config: 
        env_file = os.getcwd() + '/configuration/erp_settings.properties'
        

    
    