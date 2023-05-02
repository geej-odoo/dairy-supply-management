from odoo import fields,models
from datetime import date
from datetime import time
from dateutil.relativedelta import relativedelta

class Product(models.Model):
    _name='product'
    _description='Dairy products'
    _log_access=False

    name=fields.Char()
    type_of_buyer=fields.Selection(
        selection=[
            ('whole_sale','Whole sale'),
            ('retail_sale','Retail sale'),
            ('order_sale','Order sale'),
            
        ],
        string='Type',

    )
    order_status=fields.Selection(
        selection=[
            ('new','New'),
            ('offer_recieved','Offer Recieved'),
            ('offer_accepted','Offer Accepted'),
            ('sold','Sold'),
            ('canceled','Canceled'),
        ],
        string="Status",
        default="new",
        required=True 
        ,copy=False,
         
        
    )
    postcode=fields.Char()
    date_availability=fields.Date(copy=False,default=lambda self:fields.Date.today()+ relativedelta(months=3))
    selling_price=fields.Float(readonly=True,copy=False)
    buyer_name=fields.Char()


    tag_ids = fields.Many2many("estate.property.tag", string="tags")


    

    

    
        




