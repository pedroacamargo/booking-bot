from datetime import datetime

def get_iterations_to_right(target_date):
    current_date = str(datetime.now().date()).split('-')
    target_date = target_date.split('-')
    target_date = { "year": int(target_date[0]), "month": int(target_date[1]) }
    origin_date = { "year": int(current_date[0]), "month": int(current_date[1]) }

    year_to_months = (target_date["year"] - origin_date["year"]) * 12
    final_result = year_to_months + (target_date["month"] - origin_date["month"])
    
    return final_result - 1
