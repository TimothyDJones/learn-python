# human_readable_duration_format.py
# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_unit(value, unit):
    result = ""
    if value:
        result = str(value) + " " + unit
        if value > 1:
            result += "s"
    return result

def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    time_dict = {"minute": 60, "hour": (60*60), "day": (24*60*60), "year": (365*24*60*60)}

    years, time_left = divmod(seconds, time_dict["year"])
    days, time_left = divmod(time_left, time_dict["day"])
    hours, time_left = divmod(time_left, time_dict["hour"])
    minutes, seconds = divmod(time_left, time_dict["minute"])
    
    result = y = d = h = m = s = ""
    if years: y = format_unit(years, "year")
    if days: d = format_unit(days, "day")
    if hours: h = format_unit(hours, "hour")
    if minutes: m = format_unit(minutes, "minute")
    if seconds: s = format_unit(seconds, "second")
    #print(y, d, h, m, s)
    result = ", ".join([i for i in [y, d, h, m, s] if i != ''])
    if result.rfind(", ") > 0:
        result = result[:result.rfind(", ")] + " and" + result[result.rfind(", ") + 1:]
    #print(result)
    return result
    
if __name__ == "__main__":
    print(format_duration(1))
    print(format_duration(60))
    print(format_duration(3762+86400))
