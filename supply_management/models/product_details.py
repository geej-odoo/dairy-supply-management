from odoo import models,fields

class ProductDetails(models.Model):
    _name ="product.details"
    _description="Product Details"
    _log_access=False

    name=fields.Char(required=True)