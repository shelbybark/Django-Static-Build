def bodyattrs(request):
    path = request.META['PATH_INFO'].split('/')
    if len(path) == 2:
        body_id = 'home'
        body_classes = 'home'
    else:
        body_id = path[len(path) - 2]
        body_classes = ""
        for part in path:
            body_classes += part + " "
    return {
        'body_id': body_id,
        'body_classes': body_classes,
    }