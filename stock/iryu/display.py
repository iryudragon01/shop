from user.models import User_Start_Date
from stock.models import Item, Log_Sheet, Top_up
from django.utils import timezone


class Display:
    def getdisplay(self, request):
        content = {'user': request.user}
        all_item = Item.objects.all()

        # create log sheet if not exist
        if Log_Sheet.objects.all().count() == 0:
            for item in all_item:
                new_log_sheet = Log_Sheet(item=item,
                                          version=1,
                                          Last_stock=0,  # stock last value
                                          date_log=timezone.now(),
                                          start_log_version=1,
                                          end_log_version=1)
                new_log_sheet.save()
        # retrieve data from log sheet
        user = User_Start_Date.objects.get(username=request.user)
        log_sheet_starts = Log_Sheet.objects.filter(version=user.version_log)
        log_sheet_ends = Log_Sheet.objects.filter(version=Log_Sheet.objects.last().version)
        items_name = []
        items_first = []
        items_last = []
        items_price = []
        items_sale_volume = []
        items_money = []
        items_sum = []
        all_top_up = Top_up.objects.filter(date_log__gt=user.date_log)
        # fill up start log sheet with top up.
        for top_up in all_top_up:
            for log_sheet in log_sheet_starts:
                if log_sheet.item == top_up.item:
                    log_sheet.Last_stock += top_up.volume
        # set data to items
        for log_sheet, log_sheet_end in zip(log_sheet_starts, log_sheet_ends):
            items_name.append(log_sheet.item.name)
            items_price.append(log_sheet.item.price)
            if log_sheet.item.type == 1:
                items_first.append(log_sheet.Last_stock)
                items_last.append(log_sheet_end.Last_stock)
                items_sale_volume.append(log_sheet_end.Last_stock - log_sheet.Last_stock)
                items_money.append(log_sheet.item.price * (log_sheet_end.Last_stock - log_sheet.Last_stock))
            elif log_sheet.item.type == 2:
                items_first.append(0)
                items_last.append(log_sheet_end.Last_stock - log_sheet.Last_stock)
                items_sale_volume.append(log_sheet_end.Last_stock - log_sheet.Last_stock)
                items_money.append(log_sheet.item.price * (log_sheet_end.Last_stock - log_sheet.Last_stock))
            else:
                items_first.append(log_sheet.Last_stock)
                items_last.append(log_sheet_end.Last_stock)
                items_sale_volume.append(log_sheet.Last_stock - log_sheet_end.Last_stock)
                items_money.append(log_sheet.item.price * (log_sheet.Last_stock - log_sheet_end.Last_stock))

            # sum items
        sum_money = 0
        for money in items_money:
            sum_money += money
            items_sum.append(sum_money)

        items = zip(items_name, items_first, items_last, items_price, items_sale_volume, items_money,items_sum)
        content['items'] = items
        return content
