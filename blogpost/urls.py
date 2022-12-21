from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import homepage, post, about, search, postlist, allposts, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about,name = 'about' ),
    path('contact/', contact,name = 'contact' ),
    path('search/', search, name = 'search'),
    path('postlist/<slug>/', postlist, name = 'postlist'), 
    # path('author/<author_id>/', postlist_author, name = 'postlistauthor'),
    path('posts/', allposts, name = 'allposts'),
    # path('tag/<slug:tag_slug>', post_list, name='post_tag')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
