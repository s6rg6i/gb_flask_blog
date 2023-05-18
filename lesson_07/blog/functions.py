from flask import render_template
import imghdr

from blog.models import Category, Tag


def render_with_common_dict(template, **context):
    cats = [(category, len(category.posts)) for category in Category.query.all()]
    tags = Tag.query.all()
    return render_template(template, **context, cats=cats, tags=tags)


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    return imghdr.what(None, header)



