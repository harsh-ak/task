from odoo import fields, models,api,_
from datetime import date
from random import randint
from odoo.exceptions import ValidationError
import base64,sys


class Invoice(models.Model):
	_inherit='account.move'

	field_1_invoice=fields.Char(string="Field 1 Invoice")
	field_2_invoice=fields.Char(string="Field 2 Invoice")


# class InvoiceLine(models.Model):
# 	_inherit='account.move.line'

# 	field_1_invoice_line=fields.Char(string="Field 1 Invoice Line")
# 	field_2_invoice_line=fields.Char(string="Field 2 Invoice Line")

