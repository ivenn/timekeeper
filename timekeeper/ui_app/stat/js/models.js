(function ($, Backbone, _, app) {

    var Sesion = Beckbone.Model.extend({
        default: {
            token: null
        },
        initialize: function (option) {
            this.option = option;
            this.load();
        },
        load: function () {
            var token = localStorage.apiToken;
            if (token){
                this.set('token', token);
            }
        },
        save: function (token) {
            this.set('token', token);
            if (token === null){
                localStorage.removeItem('apiToken');
            } else {
                localStorage.apiToken = token;
            }
        },
        delete: function () {
            this.save(null);
        },
        authenticated: function () {
            return this.get('toke') !== null;
        }

    });

    app.session = new Sesion();

})(jQuery, Backbone, _, app);