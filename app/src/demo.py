# import os

# vscode_injection = os.environ.get("APP_ENV","dev")
# if not vscode_injection:
#     raise Exception("vscode_injection not set!")

# try:
#     vscode_injection = int(vscode_injection)
# except ValueError:
#     raise Exception("vscode_injection should be INT!")

###################################

from decouple import config

vscode_injection = config(
    "NEW_VARIABLE",
    cast=int
)
