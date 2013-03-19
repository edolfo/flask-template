import controllers.accounts  as accountsCtrl
import controllers.root      as rootCtrl

def createRoutes():
    accountsCtrl.views.add_url_rule('/signup', view_func = accountsCtrl.signup)
    accountsCtrl.views.add_url_rule('/login', view_func = accountsCtrl.login)
    accountsCtrl.views.add_url_rule('/login/handler', view_func = accountsCtrl.login_handler)
    
    rootCtrl.views.add_url_rule('/', view_func = rootCtrl.index)