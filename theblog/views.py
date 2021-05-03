from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category
from .forms import PostForm, EditForm, AddPostForm, AddCategoryForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all().order_by('name')
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        total_likes = stuff.total_likes()
        context['cat_menu'] = cat_menu
        context['likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    # model = Post
    # template_name = 'addblogpost.html'
    # fields = '__all__'
    # fields = ('title', 'body')

    model = Post
    form_class = PostForm
    template_name = 'addblogpost.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'addcategory.html'
    success_url = reverse_lazy('addcategory')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all().order_by('name')
        context = super(AddCategoryView, self).get_context_data(
            *args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class AddCommentView(CreateView):
    model = Comment
    form_class = AddPostForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('article_detail', kwargs={'pk': post_id})
