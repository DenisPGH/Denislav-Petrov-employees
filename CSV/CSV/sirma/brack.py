# class ShowResult(views.ListView):
#     def get_context_data(self, **kwargs):
#         dict_to_show={}
#         list_show=[]
#         context = super().get_context_data(**kwargs)
#         file_to_show=CSVfiles.objects.all().last()
#
#         if file_to_show:
#             print(file_to_show.file)
#             with open(f'{file_to_show.file}', newline='') as csvfile:
#                 # chetene file
#                 reader = csv.reader(csvfile)
#                 for row in reader:
#                     dict_to_show['EmpID']=row[0]
#                     dict_to_show['ProjectID']=row[1]
#                     dict_to_show['DateFrom']=row[1]
#                     dict_to_show['DateTo']=row[1]
#                     list_show.append(dict_to_show)
#
#         context['files'] = list_show
#         return context


""" funk"""

# """find the longest time in one project"""
#     all_project_id = Employees.objects.filter().values_list('ProjectID', flat=True).distinct()
#     list_all_project_id = list(all_project_id)
#
#     id_of_max_pair=0
#     time_first_employees = 0
#     time_second_employees = 0
#
#     current_max_time_together_work_on_same_project=0
#     final_max_time=datetime.timedelta(1900,10,10,10,10,10,10)
#     final_project_id=0
#     final_emp_ids=[]
#
#
#     for each_project_id in list_all_project_id:
#         list_time_both_empl = []
#         result_set=Employees.objects.filter(ProjectID=each_project_id)
#         ids_of_current_pair=[x.EmpID for x in result_set]
#         if len(result_set)==2:
#             for each_emp in result_set:
#                 # calculate time for current pair
#                 time_working_on_project=abs(each_emp.DateFrom-each_emp.DateTo)
#                 #print(f"{each_emp.EmpID} = {time_working_on_project}")
#                 list_time_both_empl.append(time_working_on_project)
#             current_max_time_together_work_on_same_project= max(list_time_both_empl) - min(list_time_both_empl)
#             print(f"ProjectID: {each_project_id}= {current_max_time_together_work_on_same_project}( {ids_of_current_pair})")
#             if current_max_time_together_work_on_same_project > final_max_time:
#                 final_max_time=current_max_time_together_work_on_same_project
#                 final_project_id=each_project_id
#                 final_emp_ids=ids_of_current_pair
#
#
