(function ($, Backbone, _, app){

    var TemplateView = Backbone.View.extend({
        templateName: '',
        initialize: function(){
            this.template = _.template($(this.templateName).html());
        },
        render: function () {
            var context = this.getContext()
            var html = this.template(context);
            this.$el.html(html);
        },
        getContext: function () {
            return {};
        }
    });

    var FormView = TemplateView.extend({
        events: {
            'submit form' : 'submit'
        },
        errorTemplate: _.template('<div class="alert alert-danger alert-dismissible error" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Error!</strong> <%- msg %></div>'),
        clearErrors: function () {
            $('.error', this.form).remove();
        },
        showErrors: function (errors) {
            console.log("Errors on login: " + errors);
            _.map(errors, function (fieldErrors, name) {
                var field = $(':input[name='+name+']', this.form),
                    label = $('label[for=' + field.attr('id')+']', this.form);
                if (label.length === 0) {
                    label = $('label', this.form).first();
                }
                function appendError(msg) {
                    label.before(this.errorTemplate({msg: msg}));
                }
                _.map(fieldErrors, appendError, this);
            }, this);
        },
        serializeForm: function (form) {
            return _.object(_.map(form.serializeArray(), function (item) {
                // Convert object ot tuple of (name, value)
                return [item.name, item.value];
            }));
        },
        submit: function (event) {
            event.preventDefault();
            this.form = $(event.currentTarget);
            this.clearErrors();
        },
        failure: function (xhr, status, error) {
            var errors = xhr.responseJSON;
            this.showErrors(errors);
        },
        done: function (event) {
            if (event){
                event.preventDefault();
            }
            this.trigger('done');
            this.remove();
        }


    });

    var SettingsView = TemplateView.extend({
        templateName: '#setttings-template',
        initialize: function (options) {
            var self = this;
            TemplateView.prototype.initialize.apply(this, arguments)
        }
    });

    var HomepageView = TemplateView.extend({
        templateName: '#home-template',
        initialize: function (options) {
            var self = this;
            TemplateView.prototype.initialize.apply(this, arguments)
            app.collections.ready.done(function () {
                app.tasks.fetch({
                    success: $.proxy(self.render, self)
                });
            });
        },
        getContext: function () {
            return {'tasks': app.tasks || null};
        }

    });

    var LoginView = FormView.extend({
        id: 'login',
        templateName: '#login-template',
        errorTempate: _.template('<span class="error"><%-msg %></span>'),
        events: {
            'submit form' : 'submit'
        },
        submit: function (event) {
            var data = {};
            FormView.prototype.submit.apply(this, arguments);
            data = this.serializeForm(this.form);
            $.post(app.apiLogin, data)
                .done($.proxy(this.loginSuccess, this))
                .fail($.proxy(this.failure, this));
        },
        loginSuccess: function (data) {
            app.session.save(data.token);
            this.done();
        }
    });

    var HeaderView = TemplateView.extend({
        templateName: '#header-menu-template',
        tagName: 'ul',
        attributes : {
           id    : 'header-menu',
           class : 'nav navbar-nav navbar-right'
     },
        events: {
            'click a.logout': 'logout',
            'click a#btn_settings': 'openSettings'
        },
        getContext: function (){
            return {authenticated: app.session.authenticated()};
        },
        logout: function (event) {
            event.preventDefault();
            app.session.delete();
            window.location = '/';
        },

        openSettings: function (event) {
            event.preventDefault();
        }
    })

    app.views.HomepageView = HomepageView;
    app.views.LoginView = LoginView;
    app.views.HeaderView = HeaderView;

})(jQuery, Backbone, _, app);
