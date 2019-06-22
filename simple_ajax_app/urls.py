from django.urls import path
from simple_ajax_app.views import UserSignUpView, ValidateUsername

urlpatterns = [
    path('simpleajax/', UserSignUpView.as_view(), name='simple_ajax'),
    path('ajax/validate-username/', ValidateUsername.as_view(), name='simple_ajax_validate'),
]