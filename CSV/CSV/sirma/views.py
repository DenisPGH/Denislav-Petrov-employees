from django.shortcuts import render

# Create your views here.
import csv

from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

# Create your views here.
from CSV.sirma.models import CSVfiles, Employees


class StartPage(views.CreateView):
    delete_all_data = Employees.objects.all()
    delete_all_data.delete()
    model = CSVfiles
    fields = '__all__'
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        dict_to_show={}
        list_show = []
        context = super().get_context_data(**kwargs)
        file_to_show=CSVfiles.objects.all().last()

        if file_to_show:
            print(file_to_show.file)
            with open(f'{file_to_show.file}', newline='') as csvfile:
                # chetene file
                reader = csv.reader(csvfile)
                for row in reader:
                    emp=row[0]
                    project=row[1]
                    date_from=row[2].strip()
                    date_to=row[3].strip()
                    dict_to_show['EmpID']=emp
                    dict_to_show['ProjectID']=project
                    dict_to_show['DateFrom']=date_from
                    dict_to_show['DateTo']=date_to
                    list_show.append(dict_to_show)
                    if date_to=='NULL':
                        date_to='2022-05-03'

                    new_emp=Employees(
                        EmpID=emp,
                        ProjectID=project,
                        DateFrom=date_from,
                        DateTo=date_to,
                    )
                    new_emp.save()


        context['files'] = list_show
        return context







