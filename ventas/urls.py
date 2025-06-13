from django.urls import path
from .views import registrar_venta, lista_ventas, detalle_venta, reporte_lista_ventas_pdf,reporte_detalle_venta_pdf

urlpatterns = [
    path('', lista_ventas, name='lista_ventas'),
    path('<int:venta_id>/', detalle_venta, name='detalle_venta'),
    path('registrar/', registrar_venta, name='registrar_venta'),
    path('reporte-ventas/', reporte_lista_ventas_pdf, name='reporte_lista_ventas_pdf'),
    path('<int:venta_id>/reporte-detalle/', reporte_detalle_venta_pdf, name='reporte_detalle_venta'),

]
