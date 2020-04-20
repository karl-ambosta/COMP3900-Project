from rest_framework import permissions
from .models import UserProfile
#from django.db import models
from .models import UserProfile, MenuItem, MenuCategory, OrderList, OrderRequest, Restaurant, OpeningHours
from django.contrib.auth.models import User

class IsUser(permissions.BasePermission): 
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.username == request.user.username
        else:
            return False

class IsCustomer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (UserProfile.objects.get(user=request.user).role) == '1':
            return True
        else: 
            return False

class IsCashier(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (UserProfile.objects.get(user=request.user).role) == '2':
            return True

class IsKitchen(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (UserProfile.objects.get(user=request.user).role) == '3':
            return True
  
class IsManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (UserProfile.objects.get(user=request.user).role) == '4':
            return True

class IsWaiter (permissions.BasePermission): 
    def has_object_permission(self, request, view, obj):
        if (UserProfile.objects.get(user=request.user).role) == '5':
            return True


class MenuItemPermissions(permissions.BasePermission): 
    """
    Menu Items Permissions - Who can create, list, retrieve, update or destroy
    """

    def has_permission(self, request, view):
        user_role = (UserProfile.objects.get(user=request.user).role)
        if view.action == 'create': #CREATE: Kitchen or Manager
            return ((user_role ==3) or (user_role==4))
        elif view.action == 'list': #LIST: All Users
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user_role = (UserProfile.objects.get(user=request.user).role)
        if view.action == 'retrieve': #RETRIEVE: All Users
            return True
        elif view.action in ['update', 'partial_update']: #UPDATE: Kitchen or Manager
            if ((user_role ==3) or (user_role==4)):
                return True
        elif view.action == 'destroy': #DESTROY: Admin, Kitchen or Manager
            return ((request.user.is_staff) or (user_role ==3) or (user_role==4)) 
        else:
            return False

class OpeningHoursPermissions(permissions.BasePermission): 
    """
    Opening Hours Permissions - Who can create, list, retrieve, update or destroy
    """
    
    def has_permission(self, request, view):
        user_role = (UserProfile.objects.get(user=request.user).role)
        if view.action == 'create' and ((request.user.is_staff) or (user_role==4)): #CREATE: Manager
            return True
        elif view.action == 'list': #LIST: All Users
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user_role = (UserProfile.objects.get(user=request.user).role)
        if view.action == 'retrieve': #RETRIEVE: All Users
            return True
        elif view.action in ['update', 'partial_update']:
            if ((request.user.is_staff) or (user_role == 4)): #UPDATE: Admin Account or Manager
                return True
        elif view.action == 'destroy': #DESTROY: Admin Account or Manager
            return ((request.user.is_staff) or (user_role==4)) 
        else:
            return False

class RestaurantAndMenuCategoryPermissions(permissions.BasePermission): 
    """
    Restaurant and Menu Category Permissions - Who can create, list, retrieve, update or destroy
    """

    def has_permission(self, request, view):
        user_role = (UserProfile.objects.get(user=request.user).role)
        if view.action == 'create' and ((user_role ==3) or (user_role==4)): #CREATE: Kitchen or Manager
            return True
        elif view.action == 'list': #LIST: All Users
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        user_role = (UserProfile.objects.get(user=request.user).role)
        if view.action == 'retrieve': #RETRIEVE: All Users
            return True
        elif view.action in ['update', 'partial_update']:
            if user_role == 3 or user_role == 4: #UPDATE: Kitchen or Manager
                return True
        elif view.action == 'destroy': #DESTROY: Admin, Kitchen or Manager
            return ((request.user.is_staff) or (user_role ==3) or (user_role==4)) 
        else:
            return False