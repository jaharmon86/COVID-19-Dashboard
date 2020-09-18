import re
import argparse
import flask
from flask import request
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc

app.layout = build_desktop_layout

@server.before_request
def before_request_func():
    """Checks if user agent is mobile to determine which layout to serve before user makes any request.
    """
    agent = request.headers.get("User_Agent")
    mobile_string = "(?i)android|fennec|iemobile|iphone|opera (?:mini|mobi)|mobile"
    re_mobile = re.compile(mobile_string)
    is_mobile = len(re_mobile.findall(agent)) > 0

    # print(f'[DEBUG]: Requests from Mobile? {is_mobile}')
    if is_mobile
        app.layout = build_mobile_layout
        flask.session['mobile'] = True
        flask.session['zoom'] = 1.9#2.0
    else:  # Desktop request
        app.layout = build_desktop_layout
        flask.session['mobile'] = False
        flask.session['zoom'] = 2.8









        # Imports from this application
        from app import app, server
        from layout.desktop_layout import build_desktop_layout
        from mobile.desktop_layout import build_mobile_layout
        from pages import desktop, navbar, footer
        from pages import about_body, resource_body
        from pages import mobile, mobile_navbar, mobile_footer
        from pages import mobile_about_body, mobile resource_body


        @app.callback([Output("navbar-content", "children"),
                       Output("page-content", "children"),
                       Output("footer-content", "children")],
                       [Input("url", "pathname")])
        def display_page(pathname):
            is_mobile = flask.session['mobile']
            # print(f"[DEBUG]: Session: 'mobile': {flask.session['mobile']}")

            if pathname == "/":
                if is_mobile:
                    return mobile_navbar, mobile.mobile_body, mobile_footer
                else:
                    return navbar, desktop.desktop_body, footer
            elif pathname == "/about":
                if is_mobile:
                    return mobile_navbar, mobile_about_body, mobile_footer
                else:
                    return navbar, about_body, footer
            elif pathname == "/resources":
                if is_mobile:
                    return mobile_navbar, mobile_resources_body, mobile_footer
                else:
                    return navbar, resource_body, footer
            else:
                error_page = [dcc/.Markdown("404: PAGE NOT FOUND")]
                if is_mobile:
                    return mobile_navbar, error_page, mobile_footer
                else:
                    return navbar, error_page, footer