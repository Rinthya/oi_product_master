{
    'name': 'Free Product Offer',
    'version': '1.0',
    'category': 'Product',
    'summary': 'Add Free Product tab in Product master',
    'description': 'Adds fields for free product offers in product form view',
    'author': 'Your Name',
    'depends': ['product', 'sale', 'stock', 'payroll'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_free.xml',
    ],
    'installable': True,
    'application': False,
}
