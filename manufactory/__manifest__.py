{
    'name': 'manufactory',
    'version': '1.0',
    'depends': ['mrp'],
    'author': 'TPD',
    'category': 'Manufacturing',
    'summary': 'Custom fields and behavior for MRP',
    'data': [
        "security/ir.model.access.csv",
        "views/fish_weight_menu.xml",
        "views/fish_weight.xml"
    ],
    'installable': True,
    'application': False,
}
