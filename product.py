# This file is part of stock_product_location_package module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Product']
__metaclass__ = PoolMeta


class Product:
    "Product Variant"
    __name__ = "product.product"
    default_loc_rack = fields.Function(fields.Char('Rack'), 'get_default_loc')
    default_loc_row = fields.Function(fields.Char('Row'), 'get_default_loc')
    default_loc_case = fields.Function(fields.Char('Case'), 'get_default_loc')

    def get_default_loc(self, name):
        '''
        Default location (rack-row-case) in warehouse
        '''
        for location in self.locations:
            if location.warehouse.type == 'warehouse':
                if name == 'default_loc_rack':
                    return location.loc_rack
                if name == 'default_loc_row':
                    return location.loc_row
                if name == 'default_loc_case':
                    return location.loc_case
        return ''
