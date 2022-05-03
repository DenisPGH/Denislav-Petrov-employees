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
        list_start_date_both_emp=[]
        list_end_date_both_emp=[]
        result_set = Employees.objects.filter(ProjectID=each_project_id)
        ids_of_current_pair = [x.EmpID for x in result_set]
        if len(result_set) == pair:
            for each_emp in result_set:
                # calculate time for current pair
                list_start_date_both_emp.append(each_emp.DateFrom)
                list_end_date_both_emp.append(each_emp.DateTo)
            # calculation time togheter
            connected_latest_start_data=max(list_start_date_both_emp)
            connected_earliest_end_data=min(list_end_date_both_emp)
            current_max_time_together_work_on_same_project=abs(connected_latest_start_data-connected_earliest_end_data)
            #print(f" tog= {current_max_time_together_work_on_same_project}")
            #overlap=max(0,current_max_time_together_work_on_same_project)

            #if a.start < b.end and b.start < a.end:
            # if min(list_start_date_both_emp) < max(list_end_date_both_emp) and \
            #         max(list_start_date_both_emp) < min(list_end_date_both_emp):
            if (result_set[0].DateFrom<result_set[1].DateTo and result_set[1].DateFrom<result_set[0].DateTo) or\
                    (result_set[0].DateFrom>result_set[1].DateTo and result_set[1].DateFrom>result_set[0].DateTo):
                #print(f"{each_project_id}='true'")
                if current_max_time_together_work_on_same_project > final_max_time:
                    final_max_time = current_max_time_together_work_on_same_project
                    final_project_id = each_project_id
                    final_emp_ids = ids_of_current_pair
    #print(ids_of_current_pair)
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


        if ids_emp:
            context['has'] = True
            context['duration'] = duration
            context['employee_id_1'] = ids_emp[0]
            context['employee_id_2'] = ids_emp[1]
        else:
            context['has'] = False

        return context

    success_url = reverse_lazy('result')







