# This file is part of stock_product_location_package module for Tryton.
# The COPYRIGHT file at the top level of this repository contafroms
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['Move']


class Move(metaclass=PoolMeta):
    __name__ = 'stock.move'
    from_location_rack = fields.Function(fields.Char('From Location Rack'),
        'get_from_location_wharehose')
    from_location_row = fields.Function(fields.Char('From Location Row'),
        'get_from_location_wharehose')
    from_location_case = fields.Function(fields.Char('From Location Case'),
        'get_from_location_wharehose')
    to_location_rack = fields.Function(fields.Char('To Location Rack'),
        'get_to_location_wharehose')
    to_location_row = fields.Function(fields.Char('To Location Row'),
        'get_to_location_wharehose')
    to_location_case = fields.Function(fields.Char('To Location Case'),
        'get_to_location_wharehose')

    def get_from_location_wharehose(self, name):
        '''Location (rack-row-case) in From Location and Warehouse'''
        ProductLocation = Pool().get('stock.product.location')

        if not self.from_location:
            return None
        if not self.from_location.parent:
            return None
        if not self.from_location.parent.type == 'warehouse':
            return None
        if not self.product:
            return None

        prod_locations = ProductLocation.search([
            ('product', '=', self.product),
            ('warehouse', '=', self.from_location.parent),
            ('location', '=', self.from_location),
            ], limit=1)
        if not prod_locations:
            return None
        prod_location, = prod_locations
        if name == 'from_location_rack':
            return prod_location.loc_rack
        if name == 'from_location_row':
            return prod_location.loc_row
        if name == 'from_location_case':
            return prod_location.loc_case
        return None

    def get_to_location_wharehose(self, name):
        '''Location (rack-row-case) in To Location and Warehouse'''
        ProductLocation = Pool().get('stock.product.location')

        if not self.to_location:
            return None
        if not self.to_location.parent:
            return None
        if not self.to_location.parent.type == 'warehouse':
            return None
        if not self.product:
            return None

        prod_locations = ProductLocation.search([
            ('product', '=', self.product),
            ('warehouse', '=', self.to_location.parent),
            ('location', '=', self.to_location),
            ], limit=1)
        if not prod_locations:
            return None
        prod_location, = prod_locations
        if name == 'to_location_rack':
            return prod_location.loc_rack
        if name == 'to_location_row':
            return prod_location.loc_row
        if name == 'to_location_case':
            return prod_location.loc_case
        return None
