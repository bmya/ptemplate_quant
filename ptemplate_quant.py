# -*- coding: utf-8 -*-
from openerp import models, fields, api
import time
import logging
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

class ptemplate_quant(models.Model):

    _name = 'stock.quant'
    _inherit = 'stock.quant'

    product_tmpl_name = fields.Char('Plantilla',compute='_compute_ptemplate')
    product_variant = fields.Char('Variantes',compute='_compute_pvariant')

    @api.depends('product_id')
    def _compute_ptemplate(self):
        for x in self:
            x.product_tmpl_name = x.product_id.product_tmpl_id.name

    @api.depends('product_id')
    def _compute_pvariant(self):
        for x in self:
            #i = x.product_id.name.index('(')+1
            #j = x.product_id.name.index(')')
            try:
                x.product_variant = x.product_id.name[x.product_id.name.index('(')+1:x.product_id.name.index(')')]
            except:
                x.product_variant = 'Unico'
            
