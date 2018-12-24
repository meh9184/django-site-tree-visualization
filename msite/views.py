from django.shortcuts import render_to_response
from msite.models import Url

def mainpage(request):

    querySet = Url.objects.filter(depth=3)
    parentList = [{'name': str(url.noUrl), 'parent': str(url.noParent), 'children': []} for url in querySet]

    depth = 3
    while depth > 0 :

        depth -= 1
        childrenList = parentList

        querySet = Url.objects.filter(depth=depth)
        parentList = [{'name': str(url.noUrl), 'parent' : str(url.noParent), 'children': []} for url in querySet]


        i = 0
        j = 0
        while i < len(childrenList) :
                if (childrenList[i])['parent'] == (parentList[j])['name'] :
                    ((parentList[j])['children']).append(childrenList[i])
                    i += 1
                else :
                    j += 1




    data = str(parentList)[1:-1]


    return render_to_response("treeVisualization.html", {"data": data})