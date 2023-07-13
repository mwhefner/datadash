"""
Module/Script Name: containertop.py
Author: M. W. Hefner

Created: 7/01/2023
Last Modified: 7/12/2023

Project: RIEEE DataDash
Project Version Id: 1.0

Script Description: This script defines the style, layout, and callback functionality of the contentcontainertop.

Exceptional notes about this script:
(none)

Callback methods: 0

~~~

This Dash application component was created using the template provided by the Research Institute for Environment, Energy, and Economics at Appalachian State University.

"""

# Component ID (Should be the same as the title of this file)
component_id = "containertop"

# Import Dependencies
import dash.html
# import components.examplesubcomponent as examplesubcomponent
import components.utils.constants as d
import components.utils.login

# STYLES (CSS DICT)
styles = {
    'component' : {
        # Behavior
        'display' : 'flex',
        'flex-flow' : 'row nowrap',

        'align-items' : 'center',
        'justify-content' : 'space-between',

        'margin': '0px',
        'padding': '10px',

        #'height': d.header_height,
        'color': 'white',
        'border-bottom': '3px solid ' + d.appstate_gold,
        'background-color' : 'black',
        'border-top-left-radius': '10px',
        'border-top-right-radius': '10px',
    },

    'h2' : {
        'margin' : '0', 
        'padding' : '0',
    }
}

# DYNAMIC LAYOUT (Think of this component as starting here)
def dynamic_layout(application_type) :

    # Get appropriate strings for the different application display area types:
    if (application_type == "publicdashboards") :
        # Display public dashboards
        title = "Public Dashboards"
        information = "These applications are available without a Shibboleth login."
        altxt = information
    elif (application_type == "myapplications") :
        # My Applications
        title = components.utils.login.loggedInAs + "'s Applications"
        information = "These applications are directly associated with your user account.  Public applications are indicated with a globe icon."
        altxt = information
    elif (application_type == 'backend') :
        # Backend for Admin only
        title = "Backend Applications (Admin View)"
        information = "This application view is for ITS and RIEEE technical administrators only.  Please contact RIEEE if you believe to be viewing this in error."
        altxt = information
    elif (application_type == 'adminall') :
        # All for Admin only
        title = "All Applications (Admin View)"
        information = "This application view is for ITS and RIEEE technical administrators only.  Please contact RIEEE if you believe to be viewing this in error."
        altxt = information
    else :
        title = "Unknown Application Type"
        information = "Something went wrong.  Please contact RIEEE if you believe to be viewing this in error."
        altxt = information

    # Return appropriate heading for the application display
    return dash.html.Div(
    id = application_type + component_id,
    style = styles['component'],
    children= [
        dash.html.H2(title, style = styles['h2']),
        dash.html.Img(src="./assets/icons/information_BW.png", title = information, alt = altxt, style = {'height' : '32px'}) # Info icon set to H1 Height
    ]
)

# CALLBACKS (0)