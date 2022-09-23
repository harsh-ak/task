from odoo import fields, models,api,_
from datetime import date
from random import randint
from odoo.exceptions import ValidationError
import base64,sys


class SaleOrder(models.Model):
	_inherit='sale.order'

	field_1=fields.Char(string="Field 1")
	field_2=fields.Char(string="Field 2")
	# sale_history_ids=fields.One2many(string="Sales History",comodel_name="sale.history.book)


class SaleOrderLine(models.Model):
	_inherit='sale.order.line'

	so_field_1=fields.Char(string="SO Field 1")	
	so_field_2=fields.Char(string="SO Field 2")	
