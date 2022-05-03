import datetime

from django.shortcuts import render

# Create your views here.
import csv

from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

# Create your views here.
from CSV.sirma.models import CSVfiles, Employees

class Helper:
    pass



class StartPage(views.CreateView):

    model = CSVfiles
    fields = '__all__'
    template_name = 'index.html'
    """find the longest time in one project"""
    all_project_id = Employees.objects.filter().values_list('ProjectID', flat=True).distinct()
    list_all_project_id = list(all_project_id)

    id_of_max_pair=0
    time_first_employees = 0
    time_second_employees = 0

    current_max_time_together_work_on_same_project=0
    final_max_time=datetime.timedelta(1900,10,10,10,10,10,10)
    final_project_id=0
    final_emp_ids=[]


    for each_project_id in list_all_project_id:
        list_time_both_empl = []
        result_set=Employees.objects.filter(ProjectID=each_project_id)
        ids_of_current_pair=[x.EmpID for x in result_set]
        if len(result_set)==2:
            for each_emp in result_set:
                # calculate time for current pair
                time_working_on_project=abs(each_emp.DateFrom-each_emp.DateTo)
                #print(f"{each_emp.EmpID} = {time_working_on_project}")
                list_time_both_empl.append(time_working_on_project)
            current_max_time_together_work_on_same_project= max(list_time_both_empl) - min(list_time_both_empl)
            print(f"ProjectID: {each_project_id}= {current_max_time_together_work_on_same_project}( {ids_of_current_pair})")
            if current_max_time_together_work_on_same_project > final_max_time:
                final_max_time=current_max_time_together_work_on_same_project
                final_project_id=each_project_id
                final_emp_ids=ids_of_current_pair



    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        """ clear the db for every new file"""
        delete_all_data = Employees.objects.all()
        delete_all_data.delete()

        context = super().get_context_data(**kwargs)
        file_to_show=CSVfiles.objects.all().last()
        all_emp=Employees.objects.all()

        """ store the all data to the db"""
        if file_to_show:
            with open(f'{file_to_show.file}', newline='') as csvfile:
                # chetene file
                reader = csv.reader(csvfile)
                for row in reader:
                    emp=row[0]
                    project=row[1]
                    date_from=row[2].strip()
                    date_to=row[3].strip()

                    if date_to=='NULL':
                        date_to='2022-05-03'
                    new_emp=Employees(
                        EmpID=emp,
                        ProjectID=project,
                        DateFrom=date_from,
                        DateTo=date_to,
                    )
                    new_emp.save()

        """return the result ot render on html page"""
        context['employees'] = all_emp
        context['result'] = self.list_all_project_id
        context['result_set'] = self.result_set
        context['longest_pair_project_id'] = self.final_project_id
        context['duration'] = self.final_max_time
        context['ids_winners'] = ','.join([str(x) for x in self.final_emp_ids])
        return context







