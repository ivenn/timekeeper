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

    var HomepageView = TemplateView.extend({
        templateName: '#home-template',
    });

    var LoginView = TemplateView.extend({
        id: 'login',
        templateName: '#login-template',
    });

    app.views.HomepageView = HomepageView;
    app.views.LoginView = LoginView;

})(jQuery, Backbone, _, app);

