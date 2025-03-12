from tkinter import Frame
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, filters
from .filters import BemorFilter
from .models import Bemor
from .serializers import BemorSerializer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class BemorCreateView(generics.CreateAPIView):
    queryset = Bemor.objects.all()
    serializer_class = BemorSerializer
    permission_classes = [IsAdminUser]


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response



class BemorUpdateView(generics.UpdateAPIView):
    queryset = Bemor.objects.all()
    serializer_class = BemorSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'uid'
    parser_classes = [MultiPartParser, FormParser]

class BemorDeleteView(generics.DestroyAPIView):
    queryset = Bemor.objects.all()
    serializer_class = BemorSerializer
    lookup_field = 'uid'
    permission_classes = [IsAdminUser]

class BemorListView(generics.ListAPIView):
    queryset = Bemor.objects.all().order_by('-uid')
    serializer_class = BemorSerializer
    permission_classes = [IsAdminUser]





class BemorSearchView(generics.ListAPIView):
    queryset = Bemor.objects.all()
    serializer_class = BemorSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = BemorFilter

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, description="F.I.Sh", type=openapi.TYPE_STRING),
            openapi.Parameter('tugilgan', openapi.IN_QUERY, description="Tug'ilgan sana (YYYY-MM-DD)", type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class BemorRetrieveView(generics.RetrieveAPIView):
    queryset = Bemor.objects.all()
    serializer_class = BemorSerializer
    lookup_field = 'uid'

# class BemorRetrieveView(generics.RetrieveAPIView):
#     queryset = Bemor.objects.all()
#     serializer_class = BemorSerializer
#     lookup_field = 'uid'
#
#     def get(self, request, *args, **kwargs):
#         bemor = self.get_object()
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = f'attachment; filename=Bemor_{bemor.uid}.pdf'
#
#         doc = SimpleDocTemplate(response, pagesize=A4,
#                                 rightMargin=2*cm, leftMargin=2*cm,
#                                 topMargin=2*cm, bottomMargin=2*cm)
#
#         styles = getSampleStyleSheet()
#         styles.add(ParagraphStyle(name='Heading', fontSize=16, alignment=TA_CENTER, spaceAfter=20))
#         styles.add(ParagraphStyle(name='Section', fontSize=12, spaceAfter=10, leading=15))
#         styles.add(ParagraphStyle(name='SubHeading', fontSize=13, leading=16, spaceBefore=12, spaceAfter=6,
#                                   fontName='Helvetica-Bold'))
#
#         elements = []
#
#         elements.append(Paragraph("Respublika ixtisoslashtirilgan urologiya "
#
#                                   "ilmiy-amaliy tibbiyot markazi Farg\'ona filiali  ", styles['Heading']))
#         elements.append(Paragraph(f"Konsultativ poliklinika № 147966", styles['SubHeading']))
#
#         elements.append(Paragraph(f"<b>Ism:</b> {bemor.name}", styles['Section']))
#         elements.append(Paragraph(f"<b>Sana:</b> {bemor.sana.strftime('%Y-%m-%d %H:%M')}", styles['Section']))
#         elements.append(Paragraph(f"<b>Tug\'ilgan Sana:</b> {bemor.tugilgan.strftime('%Y-%m-%d %H:%M')}", styles['Section']))
#         elements.append(Paragraph(f"<b>Kasallik:</b> {bemor.kasallik}", styles['Section']))
#         elements.append(Paragraph(f"<b>Anamnezis morbi:</b> {bemor.anamnesis_m}", styles['Section']))
#         elements.append(Paragraph(f"<b>Anamnezis vitae:</b> {bemor.anamnesis_v}", styles['Section']))
#         elements.append(Paragraph(f"<b>status praesens:</b> {bemor.praesens}", styles['Section']))
#         elements.append(Paragraph(f"<b>Tekshiruv:</b> {bemor.tekshiruv}", styles['Section']))
#         elements.append(Paragraph(f"<b>Tashxis:</b> {bemor.tashxis}", styles['Section']))
#         elements.append(Paragraph(f"<b>Tavsiya:</b> {bemor.tavsiya}", styles['Section']))
#         elements.append(Paragraph(f"<b>Shifokor:</b> {bemor.doctor}", styles['Section']))
#         elements.append(Paragraph(f"<b>Mudir:</b> {bemor.mudir}", styles['Section']))
#
#         doc.build(elements)
#         return response


# class BemorDocxDownloadView(generics.RetrieveAPIView):
#     queryset = Bemor.objects.all()
#     serializer_class = BemorSerializer
#     lookup_field = 'uid'
#     permission_classes = []  # Open access
#
#     def retrieve(self, request, *args, **kwargs):
#         bemor = self.get_object()
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = f'attachment; filename=Bemor_{bemor.uid}.pdf'
#
#         doc = SimpleDocTemplate(response, pagesize=A4,
#                                 rightMargin=2*cm, leftMargin=2*cm,
#                                 topMargin=2*cm, bottomMargin=2*cm)
#
#         styles = getSampleStyleSheet()
#         styles.add(ParagraphStyle(name='Heading', fontSize=16, alignment=TA_CENTER, spaceAfter=20))
#         styles.add(ParagraphStyle(name='Section', fontSize=12, spaceAfter=10, leading=15))
#         styles.add(ParagraphStyle(name='SubHeading', fontSize=13, leading=16, spaceBefore=12, spaceAfter=6,
#                                   fontName='Helvetica-Bold'))
#
#         elements = []
#
#         elements.append(Paragraph("Respublika ixtisoslashtirilgan urologiya "
#
#                                   "ilmiy-amaliy tibbiyot markazi Farg\'ona filiali  ", styles['Heading']))
#
#         elements.append(Paragraph(f"Konsultativ poliklinika № 147966", styles['SubHeading']))
#
#         elements.append(Paragraph(f"<b>Ism:</b> {bemor.name}", styles['Section']))
#         elements.append(Paragraph(f"<b>Sana:</b> {bemor.sana.strftime('%Y-%m-%d %H:%M')}", styles['Section']))
#         elements.append(Paragraph(f"<b>Tug\'ilgan Sana:</b> {bemor.tugilgan.strftime('%Y-%m-%d %H:%M')}", styles['Section']))
#         elements.append(Paragraph(f"<b>Kasallik:</b> {bemor.kasallik}", styles['Section']))
#         elements.append(Paragraph(f"<b>Anamnezis morbi:</b> {bemor.anamnesis_m}", styles['Section']))
#         elements.append(Paragraph(f"<b>Anamnezis vitae:</b> {bemor.anamnesis_v}", styles['Section']))
#         elements.append(Paragraph(f"<b>Praesens:</b> {bemor.praesens}", styles['Section']))
#         elements.append(Paragraph(f"<b>Tekshiruv:</b> {bemor.tekshiruv}", styles['Section']))
#         elements.append(Paragraph(f"<b>Tashxis:</b> {bemor.tashxis}", styles['Section']))
#         elements.append(Paragraph(f"<b>Tavsiya:</b> {bemor.tavsiya}", styles['Section']))
#         elements.append(Paragraph(f"<b>Shifokor:</b> {bemor.doctor}", styles['Section']))
#         elements.append(Paragraph(f"<b>Mudir:</b> {bemor.mudir}", styles['Section']))
#
#         doc.build(elements)
#         return response


