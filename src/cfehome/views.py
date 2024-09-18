from django.shortcuts import render

from visit.models import PageVisit

def home_view(request, *args, **kwargs):
    qs_path = PageVisit.objects.filter(path=request.path)
    qs_all = PageVisit.objects.all()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": qs_path.count(),
        "total_visit_count": qs_all.count(),
    }

    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def about_view(request, *args, **kwargs):
    qs_path = PageVisit.objects.filter(path=request.path)
    qs_all = PageVisit.objects.all()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": qs_path.count(),
        "total_visit_count": qs_all.count(),
    }

    html_template = "about.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)
