from modeltranslation.translator import translator, TranslationOptions

from .models import Post


class PostTranslationOptions(TranslationOptions):
    # List of translatable model field.
    fields = ('title', 'body',)

    # control which translation fields are required.
    required_languages = ('en', 'ko')


translator.register(Post, PostTranslationOptions)
