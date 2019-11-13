def get_execution_time():
    return 0


def get_current_timestamp_formated():
    dateTimeObj = datetime.now()
    return str(dateTimeObj.strftime("%d/%m/%Y %H:%M:%S"))
