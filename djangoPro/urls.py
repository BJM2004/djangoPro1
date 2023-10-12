from django.urls import path, include
import Trobinoscoop.views
from Trobinoscoop.views import login,welcome,register,add_friend,show_profile, modify_profile
from django.contrib import admin
from  Trobinoscoop.views import ajax_check_email_field,ajax_add_friend
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path('admin/', admin.site.urls),
    path("addFriend/", add_friend, name="addFriend"),
    path("showProfile/", show_profile, name="showProfile"),
    path("ajaxCheckEmailField", ajax_check_email_field,name="ajaxCheckEmailField"),
    path("ajax/addFriend",ajax_add_friend, name='ajax/addFriend'),
]

urlpatterns += [
    path("welcome/", welcome, name="welcome"),
    path("", welcome, name="welcome"),
    path("modifyProfile/", modify_profile, name="modifyProfile")

]

