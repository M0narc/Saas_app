from django.shortcuts import render

from visit.models import PageVisit

def home_page_view(request, *args, **kwargs):
    # queryset = PageVisit.objects.all()
    qs = PageVisit.objects.filter(path=request.path)
    page_qs = PageVisit.objects.all()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": qs.count(),
        "total_visit_count": page_qs.count(),
    }

    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)
