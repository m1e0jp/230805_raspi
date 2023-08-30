import win32com.client
import datetime

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

calender = outlook.GetDefaultFolder(9)

items = calender.Items # このitemsが一つ一つの「予定」

select_items = [] # 指定した期間内の予定を入れるリスト

# 予定を抜き出したい期間を指定
start_date = datetime.date(2020, 10, 19) # 2020-10-19
end_date = datetime.date(2023, 10, 23) # 2020-10-23

for item in items:
    if start_date <= item.start.date() <= end_date:
        select_items.append(item)

# 抜き出した予定の詳細を表示
for select_item in select_items:
    print("件名：", select_item.subject)
    print("場所：", select_item.location)
    print("開始時刻：", select_item.start)
    print("終了時刻：", select_item.end)
    print("本文：", select_item.body)
    print("----")
