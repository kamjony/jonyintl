from django.contrib import admin

from .models import Service, About, GalleryImage, Employee, Client, SpecialisedItem

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_title']


class AboutAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(About, AboutAdmin)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name']

@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['gallery_name']

@admin.register(SpecialisedItem)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['item_name']
