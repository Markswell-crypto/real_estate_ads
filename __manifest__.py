{
    "name":"Real Estate Ads",
    "version":"1.0",
    "website":"www.codeonafrica.com",
    "author":"Markswell Ogutu",
    "description":""" 
    Real Estate Module to Show Available Properties
    """,
    "categories":"Sales",
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
        'views/menu_items.xml',
        ],
    "installable": True,
    "application": True,
    "license":"LGPL-3",
    
}