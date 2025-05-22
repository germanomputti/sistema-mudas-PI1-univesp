from django.contrib import admin
from django.urls import path
from catalogo.views import mudas_disponiveis



from catalogo.views import cadastrar_muda
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mudas_disponiveis, name='mudas_disponiveis'),
    path('cadastrar/', cadastrar_muda, name='cadastrar_muda'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='mudas_disponiveis'), name='logout'),
]


from catalogo.views import deletar_muda

urlpatterns += [
    path('deletar/<int:muda_id>/', deletar_muda, name='deletar_muda'),
]

from catalogo.views import editar_muda

urlpatterns += [
    path('editar/<int:muda_id>/', editar_muda, name='editar_muda'),
]

from catalogo.views import rodar_migrate

urlpatterns += [
    path('rodar-migrate/', rodar_migrate),
]