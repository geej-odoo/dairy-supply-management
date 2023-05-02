from odoo import models, fields

class ProductTag(models.Model):
    _name ="product.tag"
    _description="Product Tag"
    _log_access=False

    name=fields.Char(required=True)