from django.urls import path
from api.views import registerUser, loginUser, MyProtectedView, LogoutView, StudentDetailView, addBooks, booksListView, booksUpdate, deleteBook, pdf_report

urlpatterns = [
    path('v1/user/register', registerUser.as_view()),
    path('v1/user/login', loginUser.as_view()),
    path('v1/user/check', MyProtectedView.as_view()),
    path('v1/user/logout', LogoutView.as_view()),
    path('v1/user/details', StudentDetailView.as_view()),

    path('v1/books/register', addBooks.as_view()),
    path('v1/books/list', booksListView.as_view()),
    path('v1/books/update/<int:pk>', booksUpdate.as_view()),
    path('v1/books/delete/<int:pk>', deleteBook.as_view()),
    path('v1/books/report', pdf_report.as_view())
]