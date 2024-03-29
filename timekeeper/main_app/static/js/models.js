(function ($, Backbone, _, app) {
    // CSRF helper functions taken directly from Django docs
    function csrfSafeMethod(method){
        // these HTTP methods do no require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/i.test(method))
    }

    function getCookie(name){
        var cookieValue = null;
        if (document.cookie && document.cookie != ''){
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++){
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(
                        cookie.substring(name.length + 1));

                    break;
                }
            }
        }
        return cookieValue;
    }

    // Setup jQuerry ajax calls to handle CSRF
    $.ajaxPrefilter(function (settings, originalOptions, xhr){
        var csrftoken;
        if (!csrfSafeMethod(settings.type) && !this.crossDomain){
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader('X-CSRFToken', csrftoken)
        }

    });


    var Session = Backbone.Model.extend({
        defaults: {
            token: null
        },
        initialize: function (option) {
            this.option = option;
            $.ajaxPrefilter($.proxy(this._setupAuth, this));
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
            console.log('Current token is: ' + this.get('token'));
            return this.get('token') !== null;
        },
        _setupAuth: function (settings, originalOptions, xhr) {
            if (this.authenticated()){
                xhr.setRequestHeader(
                    'Authorization',
                    'Token ' + this.get('token')
                );
            }
        }

    });

    app.session = new Session();

    // REST API description

    var BaseModel = Backbone.Model.extend({
        url: function () {
            var links = this.get('links'),
                url = links && links.self;
            if (!url) {
                url = Backbone.Model.prototype.url.call(this);
            }
            return url;
        }
    })

    app.models.UserSetting = BaseModel.extend({});
    app.models.Task = BaseModel.extend({
        idAttributemodel: 'name'
    });
    app.models.Category = BaseModel.extend({});

    var BaseCollection = Backbone.Collection.extend({
        parse : function (response) {

            // this._next = response.next;
            // this._previous = response.previous;
            // this._count = response.count;
            // return response.results || [];
            return response;
        }
    });

    app.collections.ready = $.getJSON(app.apiRoot);
    app.collections.ready.done(function (data) {
        app.collections.Tasks = BaseCollection.extend({
            model: app.models.Task,
            url: data.tasks,
        });
        app.tasks = new app.collections.Tasks;
        app.collections.Categories = BaseCollection.extend({
            model: app.models.Category,
            url: data.category
        });
        app.categories = new app.collections.Categories();
        app.collections.UserSettings = Backbone.Collection.extend({
            model: app.models.UserSetting,
            url: data.settings
        });
        app.settings = new app.collections.UserSettings();
    })

})(jQuery, Backbone, _, app);
