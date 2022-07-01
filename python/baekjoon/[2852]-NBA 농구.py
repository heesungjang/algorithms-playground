import datetime

start = "48:00"
end = "12:00"

s = datetime.datetime.strptime(start, "%hh:%mm")

print(s)

"""
경시 시간: 48:00


"""
