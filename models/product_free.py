# type: ignore
from odoo import models, fields, api
from datetime import date


################ Product Template ################
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    free_from_date = fields.Date(string="From Date")
    free_to_date = fields.Date(string="To Date")
    free_min_qty = fields.Float(string="Minimum Quantity")

    free_product_1_id = fields.Many2one('product.product', string="Free Product 1")
    free_qty_1 = fields.Float(string="Free Qty 1")

    free_product_2_id = fields.Many2one('product.product', string="Free Product 2")
    free_qty_2 = fields.Float(string="Free Qty 2")

    free_qty_restrict = fields.Boolean(string="Free Quantity Restriction")

    


################ Sale Order Line ################
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    free_qty = fields.Float(string="Free Quantity", readonly=True)
    
    @api.onchange('product_id', 'product_uom_qty')
    def _apply_free_product_date_check(self):

        if not self.product_id:
            return

        # Step 1: Get order date
        order_date = self.order_id.date_order.date() if self.order_id.date_order else fields.Date.today()

        # Step 2: Get configured date
        template = self.product_id.product_tmpl_id
        from_date = template.free_from_date
        to_date = template.free_to_date

        # Step 3: Check condition
        if from_date and to_date:
            if not (from_date <= order_date <= to_date):
                # ❌ Stop execution
                return

        # ✅ If valid → continue your free product logic
        print("Date condition satisfied → apply free product")



class PayrollWizard(models.TransientModel):
    _name = 'payroll.wizard'
    _description = 'Payroll Wizard'

    from_date = fields.Date(string="From Date", required=True)
    to_date = fields.Date(string="To Date", required=True)
    branch_id = fields.Many2one('res.branch', string="Branch")

    def action_generate_payroll(self):
        # You can add your logic here
        print("Payroll Generated")