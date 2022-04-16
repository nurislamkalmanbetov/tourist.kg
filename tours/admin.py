
from django.contrib import admin


# Register your models here.
from tours.models import Tour, RegularTour, TourBooking

# admin.site.register(TourBooking)
@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):
    list_display = [
        'regulat_tour',
        'place_count',
        'mobile',
        'status',
        'is_paid',
        'created',
        'update'
    ]
    list_filter = [
        'status',
        'created',
        'is_paid'
    ]
    list_editable = [
        'status',
        'is_paid',
    ]
    search_fields = [
        "mobile",
        "notice",
        "user__first_name", #обращаемся к полю через _ _ нижний слещ
        "user__last_name"
    ]
    readonly_fields = [
        "mobile",
        "notice",
        "user",
    ]


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = [
        "title", 
        "price", 
        "created", 
        "updated" ,
        "is_active",
        ]
    list_filter = [
        "created",
        "is_active", 
        "price"]
    search_fields = [
        "title", 
        "created", 
        "description"
        ]
    list_editable = [
        "is_active",
        "price"    
    ]


@admin.register(RegularTour)
class RegularTourAdmin(admin.ModelAdmin):
    list_display = [
        'tour',
        'start',
        'end',
        'places_count',
        'status',
    ]
    list_filter = [
        "start",
        "end",
        "status",
    ]
    search_fields = [
        "tour__title",
        "start",
        "end",
    ]
    list_editabe = [
        "status", 
        "start",
        "end",
        "places_count",
    ]

