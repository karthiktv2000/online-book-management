from django.urls import path
from api.views import registerUser, loginUser, MyProtectedView, LogoutView, StudentDetailView, addBooks, booksListView, booksUpdate

urlpatterns = [
    path('v1/user/register', registerUser.as_view()),
    path('v1/user/login', loginUser.as_view()),
    path('v1/user/check', MyProtectedView.as_view()),
    path('v1/user/logout', LogoutView.as_view()),
    path('v1/user/details', StudentDetailView.as_view()),

    path('v1/books/register', addBooks.as_view()),
    path('v1/books/list', booksListView.as_view()),
    path('v1/books/update/<int:pk>', booksUpdate.as_view())
]