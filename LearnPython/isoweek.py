# import datetime as dt
#
#
# def generate_weeks(year):
#     week_in_year = []
#     for month in range(1, 13):
#         _, start, _ = dt.datetime(year, month, 1).isocalendar()
#         for d in (31, 30, 29, 28):
#             try:
#                 _, end, _ = dt.datetime(year, month, d).isocalendar()
#             except ValueError:  # skip attempts with bad dates
#                 pass
#
#         if end:
#             if start > 50:  # spillover from previous year
#                 week_in_year.append([start] + list(range(1, end + 1)))
#             else:
#                 week_in_year.append(list(range(start, end + 1)))
#
#     week_in_year = [item for sublist in week_in_year for item in sublist]
#
#     year_suffix = str(year)[2:4]
#     format_week_in_year = []
#     for week in week_in_year:
#         if week>50 and len(format_week_in_year) == 0:
#             new_year_suffix = str((year)-1)[2:4]
#             format_week_in_year.append(new_year_suffix + str(week))
#         elif len(str(week)) == 1:
#             format_week_in_year.append(year_suffix + "0" + str(week))
#         else:
#             format_week_in_year.append(year_suffix + str(week))
#
#     return format_week_in_year
# # week_in_year = []
# # for month in range(1, 13):
# #     print(month, generate_weeks(2021, month))
# #     week_in_year.append(generate_weeks(2021, month))
#
# # week_in_year = [item for sublist in week_in_year for item in sublist]
#

from datetime import datetime, timedelta

current_week = datetime(2021, 1, 1).isocalendar().week
timedelta = timedelta(weeks=20)
diff = datetime.now() + timedelta
print(diff.isocalendar().week)
print(diff)
print(type(current_week))
print(type(timedelta))
print(str(timedelta))