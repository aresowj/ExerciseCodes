def get_percentage(self, numerator, denominator):
    try:
        percentage = float(math.ceil(numerator / denominator * 10000) / 100)
    except ZeroDivisionError:
        percentage = 0

    return percentage
    
