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