from django.urls import path
from api.views import registerUser, loginUser, MyProtectedView, LogoutView, ListUsers, addBooks, booksListView, booksUpdate, deleteBook, pdfReport, hello

urlpatterns = [
    path('v1/user/hello', hello.as_view()),
    path('v1/user/register', registerUser.as_view()),
    path('v1/user/login', loginUser.as_view()),
    path('v1/user/check', MyProtectedView.as_view()),
    path('v1/user/logout', LogoutView.as_view()),
    path('v1/user/details', ListUsers.as_view()),
    path('v1/user/report', pdfReport.as_view()),

    path('v1/books/register', addBooks.as_view()),
    path('v1/books/list', booksListView.as_view()),
    path('v1/books/update/<int:pk>', booksUpdate.as_view()),
    path('v1/books/delete/<int:pk>', deleteBook.as_view()),
]    