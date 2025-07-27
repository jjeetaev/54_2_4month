from django import forms
from .models import Category, Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image"]

class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(required=True , max_length=256)
    content = forms.CharField(required=True, max_length=256)

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError("Title cannot be Python")
        return title
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title and content and title.lower() == content.lower():
            raise forms.ValidationError("title content cannot be same")
        if content and content.isdigit():
            raise forms.ValidationError("Content cannot be a number")
        return cleaned_data
    
class SearchForm(forms.Form):
    search = forms.CharField(required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    orderings = (
        ("rate", "Rate"),
        ("-rate", "Rate (desc)"),
        ("created_at", "Created at"),
        ("-created_at", "Created at (desc)"),
        ("updated_at", "Updated at"),
        ("-updated_at", "Updated at (desc)"),
        (None, None)
    )
    
    ordering = forms.ChoiceField(choices=orderings, required=False)
