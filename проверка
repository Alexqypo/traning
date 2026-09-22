import pandas as pd
import numpy as np
import re

df_data = pd.read_excel('C:\\Users\\новый пользователь\\Documents\\Мое\\Програмир\\проект проверки\\f20_L_3336381_2026_07_30.xlsx', header=17, usecols='B:Y')
df_rules = pd.read_excel('C:\\Users\\новый пользователь\\Documents\\Мое\\Програмир\\проект проверки\\rules_v4.xlsx')

df_data['check_result'] = 'OK'
df_data['error_message'] = ''


print(type(df_data))

# --- Правило 1: в столбцах Наименование и Реквизиты документа не должно быть нд??
mask_12 = df_data[11].str.lower() == 'нд'
mask_13 = df_data[12].str.lower() == 'нд'

# Строки, где правило нарушено
mask_nd = mask_12 | mask_13

# Проставляем статус ERROR
df_data.loc[mask_nd, 'check_result'] = 'ERROR'

# --- Правило 2: формат столбца Наименование объекта
valid_pattern = re.compile(
    r'^(?:'
    r'ПС\s+\d+\s+кВ\s+[^,]+'
    r'|ВЛ\s+\d+\s+кВ\s+[^,/]+\s*/\s*ВЛ\s+\d+\s+кВ\s+[^,/]+'
    r'|ВЛ\s+\d+\s+кВ\s+[^,/]+'
    r'|[^,]+\s+МЭС'
    r')$',
    re.IGNORECASE
)

has_comma = df_data[6].str.contains(',', na=False)
matches_format = df_data[6].str.match(valid_pattern, na=False)
mask_format_error = has_comma | ~matches_format

# Группируем строки по объекту
col_obj = df_data.columns[5]
grouped = df_data.groupby(col_obj, dropna=False)

# --- Записываем ошибки ---
all_errors = mask_nd | mask_format_error
df_data.loc[all_errors, 'check_result'] = 'ERROR'



# Формируем понятные сообщения об ошибках
for idx in df_data.index[all_errors]:
    msgs = []

    # ошибка в Наименование и Реквизиты документа
    if mask_12.loc[idx]:
        msgs.append(f"В колонке Наименование документа указано 'нд'")
    if mask_13.loc[idx]:
        msgs.append(f"В колонке Реквизиты документа указано 'нд'")

    # ошибки в Наименование объекта
    if has_comma.loc[idx]:
        msgs.append(f"В колонке Наименование объекта обнаружено перечисление (запятая)")
    elif not matches_format.loc[idx]:
        msgs.append(f"В колонке Наименование объекта неверный формат записи")
    
    df_data.at[idx, 'error_message'] = '; '.join(msgs)

# Сохраняем результат в новый Excel
output_path = r'C:\Users\новый пользователь\Documents\Мое\Програмир\проект проверки\checked_result.xlsx'
df_data.to_excel(output_path, index=False)
