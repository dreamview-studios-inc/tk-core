# Copyright (c) 2017 Autodesk.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.
"""
Module to support Web login via a web browser and automated session renewal.
"""

from __future__ import print_function

# pylint: disable=import-error
from PySide.QtGui import (
    QApplication,
    QDialog,
    QGridLayout,
    QLineEdit,
    QLabel,
    QDialogButtonBox,
)


# pylint: disable=too-few-public-methods
class UsernamePasswordDialog(QDialog):
    """Simple dialog to request a username and password from the user."""

    def __init__(self):
        super(UsernamePasswordDialog, self).__init__()

        # For now we fix the GUI size.
        self.setWindowTitle("Authentication Required")
        self.setMinimumWidth(420)
        self.setMinimumHeight(120)

        # set up the layout
        form_grid_layout = QGridLayout(self)

        # initialize the username combo box so that it is editable
        self._edit_username = QLineEdit(self)

        # initialize the password field so that it does not echo characters
        self._edit_password = QLineEdit(self)
        self._edit_password.setEchoMode(QLineEdit.Password)

        # initialize the labels
        label_username = QLabel(self)
        label_password = QLabel(self)
        label_username.setText("Username:")
        label_password.setText("Password:")

        # initialize buttons
        buttons = QDialogButtonBox(self)
        buttons.addButton(QDialogButtonBox.Ok)
        buttons.addButton(QDialogButtonBox.Cancel)
        buttons.button(QDialogButtonBox.Ok).setText("Login")
        buttons.button(QDialogButtonBox.Cancel).setText("Cancel")

        # place components into the dialog
        form_grid_layout.addWidget(label_username, 0, 0)
        form_grid_layout.addWidget(self._edit_username, 0, 1)
        form_grid_layout.addWidget(label_password, 1, 0)
        form_grid_layout.addWidget(self._edit_password, 1, 1)
        form_grid_layout.setRowStretch(2, 1)
        form_grid_layout.addWidget(buttons, 3, 1)

        self.setLayout(form_grid_layout)

        buttons.button(QDialogButtonBox.Ok).clicked.connect(self._on_enter_credentials)
        buttons.button(QDialogButtonBox.Cancel).clicked.connect(self.close)

    @property
    def username(self):
        """Getter for username."""
        return self._edit_username.text()

    @username.setter
    def username(self, username):
        """Setter for username."""
        self._edit_username.setText(username)

    @property
    def password(self):
        """Getter for password."""
        return self._edit_password.text()

    @password.setter
    def password(self, password):
        """Setter for password."""
        self._edit_password.setText(password)

    def _on_enter_credentials(self):
        """Callback when clicking Ok."""
        if self._edit_username.text() == "":
            self._edit_username.setFocus()
            return

        if self._edit_password.text() == "":
            self._edit_password.setFocus()
            return

        self.accept()


def main():
    """Simple test"""
    _ = QApplication([])
    login_dialog = UsernamePasswordDialog()
    login_dialog.username = "TheUsername"
    login_dialog.password = "ThePassword"
    login_dialog.show()
    login_dialog.raise_()
    if login_dialog.exec_():
        print("Username: %s" % login_dialog.username)
        print("Password: %s" % login_dialog.password)
    else:
        print("Canceled the operation")


if __name__ == "__main__":
    main()