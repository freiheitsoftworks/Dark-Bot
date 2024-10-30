from datetime import datetime

# Dicionário que mapeia os meses abreviados em português
months_mapping = {
    "jan.": 1,
    "fev.": 2,
    "mar.": 3,
    "abr.": 4,
    "maio": 5,
    "jun.": 6,
    "jul.": 7,
    "ago.": 8,
    "set.": 9,
    "out.": 10,
    "nov.": 11,
    "dez.": 12,
}

def yt_date_to_datetime(yt_date):
    parts = yt_date.split(" ")

    # Extrai o dia e o ano
    day = int(parts[0])  # Dia como inteiro
    month_abbrev = parts[2]  # O mês abreviado
    year = int(parts[4])  # Ano como inteiro

    # Converte o mês abreviado para o número do mês
    month = months_mapping.get(month_abbrev)

    # Retorna um objeto datetime
    if month:
        start_date = datetime(year, month, day)
        return start_date
    else:
        raise ValueError("Mês não reconhecido na data.")