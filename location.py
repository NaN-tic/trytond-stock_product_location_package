# This file is part of stock_product_location_package module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = [
    'ProductLocation',
    ]
__metaclass__ = PoolMeta


class ProductLocation:
    __name__ = 'stock.product.location'
    loc_rack = fields.Char('Rack')
    loc_row = fields.Char('Row')
    loc_case = fields.Char('Case')
