from datetime import datetime
import pytz
from pytz import timezone

date_e_hora_atuais = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')
data_e_hora_sp = date_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sp_em_texto = data_e_hora_sp.strftime('%d/%m/%Y %H:%M')


for tz in pytz.all_timezones:
    print(tz)