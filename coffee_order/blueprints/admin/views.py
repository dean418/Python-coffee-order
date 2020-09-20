from flask import Blueprint, render_template, redirect, url_for, request

from .coffee import Coffee
coffee = Coffee()

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin')
def get_admin():
   pass

@admin.route('/create-coffee', methods=['POST'])
def create_coffee():
   pass