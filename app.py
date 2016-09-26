from flask import Flask,flash,render_template,redirect,url_for,json,make_response,request
from flask_graphql import GraphQLView
from Schema import schema

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))



if __name__ == "__main__":
    app.run(debug = True)
