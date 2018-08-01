# urls.py
from django.conf.urls import url
from otree.urls import urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from image_upload import gallery
from django.views.generic import TemplateView

urlpatterns.append(url(r'^InstructionsEmployer/$', TemplateView.as_view(template_name='InstructionsEmployer.html'), name="InstructionsEmployer"))

urlpatterns.append(url(r'^gallery/$', 'image_upload.gallery.gallery'))
