from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.data import users

user = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")


@user.route("/")
def user_list():
    return render_template("user/users.html", users=users)


# @user.route("/<int:pk>")
# def get_user(pk: int):
#     if pk in USERS:
#         user_raw = USERS[pk]
#     else:
#         raise NotFound("User id:{}, not found".format(pk))
#     return render_template(
#         "users/details.html",
#         user_name=user_raw["name"]
#     )

#
# def get_user_name(pk: int):
#     if pk in USERS:
#         user_name = USERS[pk]["name"]
#     else:
#         raise NotFound("User id:{}, not found".format(pk))
#     return user_name
