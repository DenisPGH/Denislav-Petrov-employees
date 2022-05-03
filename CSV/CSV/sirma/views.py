import datetime

from django.shortcuts import render

# Create your views here.
import csv

from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

# Create your views here.
from CSV.sirma.models import CSVfiles, Employees

def helper(all_project_ids):
    """ this function help to find the longest time together in one project"""
    list_all_project_id = list(all_project_ids)
    pair=2

    id_of_max_pair = 0
    time_first_employees = 0
    time_second_employees = 0

    final_max_time = abs(datetime.timedelta(1900, 1, 1, 10, 10, 10, 10)-datetime.timedelta(1900, 1, 1, 22, 10, 10, 10))
    final_project_id = 0
    final_emp_ids = []

    for each_project_id in list_all_project_id:
        current_max_time_together_work_on_same_project = 0
        list_time_both_empl = []
        result_set = Employees.objects.filter(ProjectID=each_project_id)
        ids_of_current_pair = [x.EmpID for x in result_set]
        if len(result_set) == pair:
            for each_emp in result_set:
                # calculate time for current pair
                time_working_on_project = abs(each_emp.DateFrom - each_emp.DateTo)
                list_time_both_empl.append(time_working_on_project)
            current_max_time_together_work_on_same_project = \
                max(list_time_both_empl) - min(list_time_both_empl)
            if current_max_time_together_work_on_same_project > final_max_time:
                final_max_time = current_max_time_together_work_on_same_project
                final_project_id = each_project_id
                final_emp_ids = ids_of_current_pair

    return final_emp_ids,final_project_id,final_max_time





class StartPage(views.CreateView):
    model = CSVfiles
    fields = '__all__'
    template_name = 'index.html'
    success_url = reverse_lazy('index')



class ShowResult(views.TemplateView):
    template_name = 'result.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        file_to_show = CSVfiles.objects.all().last()
        all_emp = Employees.objects.all()
        """ clear the db for every new file"""
        delete_all_data = Employees.objects.all()
        delete_all_data.delete()
        """ store the all new data to the db"""
        if file_to_show:
            with open(f'{file_to_show.file}', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    emp = row[0]
                    project = row[1]
                    date_from = row[2].strip()
                    date_to = row[3].strip()

                    if date_to == 'NULL':
                        date_to = datetime.datetime.today()
                    new_emp = Employees(
                        EmpID=emp,
                        ProjectID=project,
                        DateFrom=date_from,
                        DateTo=date_to,
                    )
                    new_emp.save()
        """# give the date for calculation longest team work"""
        all_project_id = Employees.objects.filter().values_list('ProjectID', flat=True).distinct()
        ids_emp, id_project, duration = helper(all_project_id)

        """return the result ot render on html page"""
        context['employees'] = all_emp
        context['longest_pair_project_id'] = id_project
        context['duration'] = duration
        context['employee_id_1'] = ids_emp[0]
        context['employee_id_2'] = ids_emp[1]
        return context

    success_url = reverse_lazy('result')







