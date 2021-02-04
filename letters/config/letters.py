from __future__ import unicode_literals
from frappe import _

def get_data():

    return [
        {
            "label": _("Letters"),
            "icon": "octicon octicon-file-directory",
            "items": [
                {
                    "type": "doctype",
                    "name": "Letter",
                    "label": _("Letter"),
                }
            ]
        }
    ]
