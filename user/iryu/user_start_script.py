from user.models import User_Start
from stock.models import Log_Sheet,Top_up,Tempexpense,Incomelog,Expenselog


class User_Start_Handle:
    def user_superior(self,request):
        users = User_Start.objects.all()
        for user in users:
            if user.user_superior>User_Start.objects.get(username=request.user).user_superior:
                self.edit_user_start(self,user)

    def edit_user_start(self, user):
        log_sheet=Log_Sheet.objects.last()
        user.version_log = log_sheet.version
        user.date_log = log_sheet.date_log
        user.version_temp = Tempexpense.objects.all().count()
        user.version_top_up = Top_up.objects.all().count()
        user.version_income = Incomelog.objects.all().count()
        user.version_expense = Expenselog.objects.all().count()
        user.save()


