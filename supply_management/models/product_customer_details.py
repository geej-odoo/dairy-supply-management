from odoo import models,fields

class ProductCustomerDetails(models.Model):
    _name ="product.customer.details"
    _description="Product customer Details"
    _log_access=False

    name=fields.Char(required=True)